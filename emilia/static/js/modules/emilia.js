angular.module('emilia', ['google-maps'])
    .controller('emilia-map', ['$scope', '$window', '$http', function ($scope, $window, $http) {
        // Cloak
        var el = document.body.querySelector('[ng-app="emilia"]');
        angular.element(el).removeClass('hidden');

        // Global namespace
        $scope.Emilia = $window.Emilia;

        // Settings
        var DEFAULT_CENTER = {
                latitude: 54.5,
                longitude: -4
            },

            DEFAULT_DRAGGABLE = true,
            DEFAULT_CLIMB_ZOOM = 12,
            DEFAULT_MIN_ZOOM = 6,
            DEFAULT_ZOOM = 6,

            DEFAULT_BOOK_ID = 1;

        // Map config
        $scope.map = {
            center: DEFAULT_CENTER,
            control: {},
            draggable: DEFAULT_DRAGGABLE,
            options: {
                minZoom: DEFAULT_MIN_ZOOM
            },
            zoom: DEFAULT_ZOOM
        };

        // Populate data
        $scope.books = {};
        $scope.climbs = [];

        // UI bindings
        $scope.currentBook = {};
        $scope.currentRegion = {};
        $scope.currentClimb = null;
        $scope.showClubLeaders = true;
        $scope.showClubLeaderboard = true;

        $scope.selectBook = function (bookId) {
            if (bookId !== $scope.currentBook.id) {
                $scope.currentRegion = {};
            }
            $scope.currentClimb = null;
            $scope.currentBook = $scope.books[bookId];
        };

        $scope.selectClimb = function (climbId) {
            // Force region bounds reset
            $scope.currentRegion = {};
            $scope.showClubLeaders = true;
            $scope.showClubLeaderboard = true;

            $scope.currentClimb = _.findWhere($scope.climbs, {id: climbId});
            loadLeaderboards($scope.currentClimb);

            $scope.map.control.refresh($scope.currentClimb.coords);
            $scope.map.zoom = DEFAULT_CLIMB_ZOOM;

            // $scope.currentClimb.polyline.visible = true;
        };

        $scope.deselectClimb = function () {
            $scope.selectRegion($scope.currentClimb.region_id);
            $scope.currentClimb = null;
        };

        $scope.selectRegion = function (regionId, toggle) {
            if (toggle === true && regionId === $scope.currentRegion.id) {
                $scope.currentRegion = {};
            } else {
                $scope.currentRegion = _.findWhere($scope.currentBook.regions, {id: regionId});
            }
        };

        $scope.toggle = function (variable) {
            $scope[variable] = !$scope[variable];
        };

        $scope.clickMarker = function (climb) {
            $scope.selectClimb(climb.id);
            $scope.$apply();
        };

        $scope.parseDistance = function (distance, kms) {
            var points = 0,
                units = 'm';

            if (kms && distance > 1000) {
                distance /= 1000;
                points = 2;
                units = 'km';
            }

            return distance.toFixed(points) + units;
        };

        $scope.parseSeconds = function (seconds) {
            var hours = parseInt(seconds / 3600) % 24,
                min = parseInt(seconds / 60) % 60,
                sec = parseInt(seconds % 60, 10);

            return (hours > 0 ? hours + ":" : '') + (min < 10 ? "0" + min : min) + ":" + (sec < 10 ? "0" + sec : sec);
        };

        $scope.parseSpeed = function (seconds, distance) {
            return (distance/seconds * 3.6).toFixed(1) + "km/h"; // 60*60 / 1000
        };

        $scope.clickMarker.$inject = ['$markerModel'];

        var allez = function () {
            // Create books object
            _.each(Emilia.books, function (book) {
                $scope.books[book.id] = _.extend({
                    loading: true,
                    climbs: [],
                    regions: []
                }, book);
            });

            $scope.selectBook(DEFAULT_BOOK_ID);
            loadBook(DEFAULT_BOOK_ID);
        },

        loadBook = function (bookId) {
            // Load the data book by book
            var url = '/api/books/' + $scope.books[bookId].slug + '/climbs';
            $http({method: 'GET', url: url})
                .success(function (data, status, headers, config) {
                    parseBook(data);

                    // Load data for next book
                    var nextBook = _.findWhere($scope.books, {loading: true});
                    if (nextBook) {
                        loadBook(nextBook.id);
                    }
                })
                .error(function (data, status, headers, config) {
                    console.log('Error loading book ' + bookId, status);
                });
        },

        parseBook = function (data) {
            // Parse climbs and attach to book object
            var book = $scope.books[data.book.id];
            book.loading = false;

            book.markers = _.map(data.climbs, function(climb) {
                // Region data already on page
                var region = _.findWhere(Emilia.regions, {id: climb.region_id});

                // Add some shortcuts
                climb.coords = {
                    latitude: climb.segment.start_latitude,
                    longitude: climb.segment.start_longitude
                };
                climb.bg_colour = region.bg_colour;
                climb.text_colour = region.text_colour;

                return {
                    id: climb.id,
                    number: climb.number,
                    coords: climb.coords,
                    icon: '/static/img/marker-' + region.slug + '.png',
                    hiddenIcon: '/static/img/marker-hidden.png'
                    /*polyline: {
                        path: _.map(google.maps.geometry.encoding.decodePath(climb.segment.map_polyline), function(point) {
                            return {
                                longitude: point.A,
                                latitude: point.k
                            };
                        }),
                        stroke: {
                            color: '#' + region.bg_colour,
                            weight: 3
                        },
                        visible: false
                    }*/
                };
            });

            book.climbs = data.climbs;

            // Attach region data per book
            book.regions = _.map(_.uniq(_.pluck(book.climbs, 'region_id')), function (region_id) {
                var region = _.findWhere(Emilia.regions, {id: region_id});
                return _.extend({
                    climbs: _.where(book.climbs, {region_id: region_id}),
                }, region);
            });

            $scope.climbs = $scope.climbs.concat(book.climbs);
        },

        loadLeaderboards = function (climb) {
            // Retrieve leaderboards sequentially
            _.each(['club_leaderboard', 'leaderboard'], function(leaderboard) {
                if (!climb[leaderboard]) {
                    var url = '/api/climbs/' + climb.slug + '/' + leaderboard;
                    $http({method: 'GET', url: url})
                        .success(function (data, status, headers, config) {
                            parseLeaderboard(data, leaderboard);
                        })
                        .error(function (data, status, headers, config) {
                            console.log('Error loading climb ' + climb.id, status);
                        });
                }
            });
        },

        parseLeaderboard = function (data, leaderboard) {
            // Attach leaderboard data to existing object
            var climb = _.findWhere($scope.climbs, {id: data.climb.id});
            climb[leaderboard] = true;
            climb['male_' + leaderboard] = data['male_' + leaderboard];
            climb['female_' + leaderboard] = data['female_' + leaderboard];
        };

        allez();
    }]);
