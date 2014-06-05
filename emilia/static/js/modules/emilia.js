angular.module('emilia', ['google-maps'])
    .controller('emilia-map', ['$scope', '$window', '$http', '$timeout', function ($scope, $window, $http, $timeout) {
        // Cloak
        var el = document.body.querySelector('[ng-controller="emilia-map"]');
        angular.element(el).removeClass('hidden');

        // Global namespace
        $scope.Emilia = $window.Emilia;

        // Settings
        var DEFAULT_CENTER = {
                latitude: 54.5,
                longitude: -4
            },

            DEFAULT_DRAGGABLE = true,
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

        $scope.leaderboardPerPage = 10;

        $scope.selectBook = function (bookId) {
            // Check whether current region is in next book
            var currentRegionId = $scope.currentRegion.id ? $scope.currentRegion.id : $scope.currentClimb ? $scope.currentClimb.region_id : null,
                nextRegion = _.findWhere($scope.books[bookId].regions, {id: currentRegionId});

            if (bookId !== $scope.currentBook.id) {
                // Reset if not
                if (!nextRegion) {
                    $scope.currentRegion = {};
                }
            } else if ($scope.currentClimb) {
                // Reselect region if book is the same
                $scope.selectRegion($scope.currentClimb.region_id);
            }

            $scope.currentClimb = null;
            $scope.currentBook = $scope.books[bookId];

            // Select region if book has changed
            if (nextRegion && nextRegion.id) {
                $scope.selectRegion(nextRegion.id);
            }
        };

        $scope.selectClimb = function (climbId) {
            // Force region bounds reset
            $scope.currentRegion = {};
            $scope.showClubLeaders = true;
            $scope.showClubLeaderboard = true;
            $scope.currentClimb = _.findWhere($scope.climbs, {id: climbId});
            loadLeaderboards($scope.currentClimb);

            // Show polyline after climb has been set
            $timeout(function() {
                $scope.currentClimb.polyline.visible = true;
            }, 100);
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

        $scope.clickMarker = function (climb) {
            $scope.selectClimb(climb.id);
            $scope.$apply();
        };

        $scope.clickMarker.$inject = ['$markerModel'];

        $scope.selectPage = function(leaderboard, page) {
            if (leaderboard.disabled !== true) {
                if (leaderboard.pages.indexOf(page) === -1) {
                    leaderboard.disabled = true;
                    var url = '/api/climbs/' + leaderboard.climb.slug + '/' + leaderboard.type + '/' + leaderboard.gender;
                    $http({method: 'GET', url: url, params: {page: page}})
                        .success(function (data, status, headers, config) {
                            parseLeaderboardPage(data, leaderboard, page);
                            leaderboard.page = page;
                            leaderboard.disabled = false;
                        })
                        .error(function (data, status, headers, config) {
                            console.error(status, 'Error loading leaderboard page ' + page + ' for ' + leaderboard.climb.slug);
                        });
                } else {
                    leaderboard.page = page;
                }
            }
        };

        $scope.range = function (num) {
            return new Array(num);
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

        $scope.parseName = function (name) {
            // Crude cleaning attempt
            _.each([' - ', '#', '@'], function(character) {
                name = name.split(character)[0];
            });
            _.each([' ', '-'], function(join) {
                name = _.map(name.split(join), function(string) {
                    if (string === string.toUpperCase()) {
                        return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
                    } else {
                        return string;
                    }
                }).join(join);
            });
            return name.replace(/ *\([^)]*\) */g, "");
        };

        $scope.parseSeconds = function (seconds) {
            var hours = parseInt(seconds / 3600) % 24,
                min = parseInt(seconds / 60) % 60,
                sec = parseInt(seconds % 60, 10);

            return (hours > 0 ? hours + ":" : '') + (hours > 0 && min < 10 ? "0" + min : min) + ":" + (sec < 10 ? "0" + sec : sec);
        };

        $scope.parseSpeed = function (seconds, distance) {
            return (distance/seconds * 3.6).toFixed(1); // 60*60 / 1000
        };

        $scope.toggle = function (variable) {
            $scope[variable] = !$scope[variable];
        };

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
            var slug = $scope.books[bookId].slug,
                url = '/api/books/' + slug + '/climbs';

            $http({method: 'GET', url: url})
                .success(function (data, status, headers, config) {
                    parseBook(data);

                    // Load data for next book
                    var nextBook = _.findWhere($scope.books, {loading: true});
                    if (nextBook) {
                        loadBook(nextBook.id);
                    } else {
                        fin();
                    }
                })
                .error(function (data, status, headers, config) {
                    console.error(status, 'Error loading book for ' + slug);
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
                climb.polyline = {
                    path: _.map(google.maps.geometry.encoding.decodePath(climb.segment.map_polyline), function(point) {
                        return {
                            longitude: point.A,
                            latitude: point.k
                        };
                    }),
                    stroke: {
                        color: '#' + region.bg_colour,
                        opacity: 0.75,
                        weight: 4
                    },
                    visible: false
                };

                return {
                    id: climb.id,
                    number: climb.number,
                    coords: climb.coords,
                    icon: '/static/img/marker-' + region.slug + '.png',
                    hiddenIcon: '/static/img/marker-hidden.png'
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
                            console.error(status, 'Error loading climb leaderboards for ' + climb.slug);
                            climb[leaderboard + "_error"] = true;
                        });
                }
            });
        },

        parseLeaderboard = function (data, leaderboard) {
            // Attach leaderboard data to existing object
            var climb = _.findWhere($scope.climbs, {id: data.climb.id}),
                obj = {
                    climb: data.climb,
                    type: leaderboard,
                    page: 1,
                    pages: [1]
                };

            climb[leaderboard] = true;

            climb['male_' + leaderboard] = _.extend(_.extend({
                gender: 'male',
                totalPages: Math.ceil(data['male_' + leaderboard].entry_count / $scope.leaderboardPerPage)
            }, _.clone(obj)), data['male_' + leaderboard]);

            climb['female_' + leaderboard] = _.extend(_.extend({
                gender: 'female',
                totalPages: Math.ceil(data['female_' + leaderboard].entry_count / $scope.leaderboardPerPage)
            }, _.clone(obj)), data['female_' + leaderboard]);
        },

        parseLeaderboardPage = function(data, leaderboard, page) {
            leaderboard.pages.push(page);
            _.each(data[leaderboard.gender + '_' + leaderboard.type].entries, function(entry, i) {
                leaderboard.entries[i + (page - 1) * 10] = entry;
            });
        },

        fin = function() {
            // Chapeau
            $window.Emilia = null;
        };

        allez();
    }])

    .directive('hoverColours', function() {
        return {
            scope: true,
            link: function ($scope, $element, $attrs) {
                $element.bind('mouseenter', function() {
                    angular.element($element).css({
                        'backgroundColor': $attrs.hoverColor,
                        'borderColor': $attrs.hoverBorderColor,
                        'color': $attrs.hoverTextColor
                    });
                });
                $element.bind('mouseleave', function() {
                    angular.element($element).css({
                        'backgroundColor': '',
                        'borderColor': '',
                        'color': ''
                    });
                });
            }
        };
    });
