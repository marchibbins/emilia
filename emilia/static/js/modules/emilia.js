angular.module('emilia', ['google-maps'])
    .controller('emilia-map', ['$scope', '$window', '$http', function ($scope, $window, $http) {
        // Global namespace
        $scope.Emilia = $window.Emilia;

        // Settings
        var DEFAULT_CENTER = {
                latitude: 54.5,
                longitude: -4
            },

            DEFAULT_DRAGGABLE = true,
            DEFAULT_CLIMB_ZOOM = 14,
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

        $scope.selectBook = function (bookId) {
            if (bookId !== $scope.currentBook.id) {
                $scope.currentRegion = {};
            }
            $scope.currentClimb = null;
            $scope.currentBook = $scope.books[bookId];
        };

        $scope.selectClimb = function (climbId) {
            $scope.currentClimb = _.findWhere($scope.climbs, {id: climbId});
            $scope.map.control.refresh($scope.currentClimb.coords);
            $scope.map.zoom = DEFAULT_CLIMB_ZOOM;
            $scope.currentClimb.polyline.visible = true;
        };

        $scope.selectRegion = function (regionId, toggle) {
            if (toggle === true && regionId === $scope.currentRegion.id) {
                $scope.currentRegion = {};
            } else {
                $scope.currentRegion = _.findWhere($scope.currentBook.regions, {id: regionId});
            }
        };

        $scope.clickMarker = function (marker) {
            $scope.selectClimb(marker.id);
            $scope.$apply();
        };

        $scope.clickMarker.$inject = ['$markerModel'];

        var init = function () {
            // Create books object
            _.each(Emilia.books, function (book) {
                $scope.books[book.id] = _.extend({
                    loading: true,
                    climbs: [],
                    regions: []
                }, book);
            });

            $scope.selectBook(DEFAULT_BOOK_ID);
            load(DEFAULT_BOOK_ID);
        },

        load = function (bookId) {
            // Load the data book by book
            var url = '/api/books/' + $scope.books[bookId].slug + '/climbs';

            $http({method: 'GET', url: url})
                .success(function (data, status, headers, config) {
                    parse(data);

                    // Load data for next book
                    var nextBook = _.findWhere($scope.books, {loading: true});
                    if (nextBook) {
                        load(nextBook.id);
                    }
                })
                .error(function (data, status, headers, config) {
                    console.log('Error:', status);
                });
        },

        parse = function (data) {
            // Parse climbs and attach to book object
            var book = $scope.books[data.book.id];
            book.loading = false;

            book.climbs = _.map(data.climbs, function(climb) {
                var region = _.findWhere(Emilia.regions, {id: climb.region_id});
                return _.extend({
                    coords: {
                        latitude: climb.segment.start_latitude,
                        longitude: climb.segment.start_longitude
                    },
                    icon: '/static/img/marker-' + region.slug + '.png',
                    hiddenIcon: '/static/img/marker-hidden.png',
                    polyline: {
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
                    }
                }, climb);
            });

            // Attach region data per book
            book.regions = _.map(_.uniq(_.pluck(book.climbs, 'region_id')), function (region_id) {
                var region = _.findWhere(Emilia.regions, {id: region_id});
                return _.extend({
                    climbs: _.where(book.climbs, {region_id: region_id}),
                }, region);
            });

            $scope.climbs = $scope.climbs.concat(book.climbs);
        };

        init();
    }]);
