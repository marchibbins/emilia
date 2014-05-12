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
            DEFAULT_ZOOM = 6,

            DEFAULT_BOOK_ID = 1;

        // Map config
        $scope.map = {
            center: DEFAULT_CENTER,
            draggable: DEFAULT_DRAGGABLE,
            zoom: DEFAULT_ZOOM
        };

        // Populate data
        $scope.books = {};
        $scope.climbs = [];

        // UI bindings
        $scope.currentClimb = {};
        $scope.currentBook = {
            climbs: [] // Bound to markers
        };

        // Load all the data
        $http({method: 'GET', url: '/api/climbs'})
            .success(function (data, status, headers, config) {
                init(data);
            })
            .error(function (data, status, headers, config) {
                console.log('Error:', status);
            });

        $scope.selectBook = function (bookId) {
            $scope.currentBook = $scope.books[bookId];
        };

        $scope.selectClimb = function (climbId) {
            $scope.currentClimb = _.findWhere($scope.climbs, {id: climbId});
        };

        $scope.clickMarker = function (marker) {
            $scope.selectClimb(marker.id);
            $scope.$apply();
        };

        $scope.clickMarker.$inject = ['$markerModel'];

        var init = function (data) {
            $scope.climbs = data.climbs;

            // Parse coords for markers
            _.each($scope.climbs, function (climb) {
                climb.coords = {
                    latitude: climb.segment.start_latitude,
                    longitude: climb.segment.start_longitude
                };
            });

            // Create books object, same data different grouping
            _.each(Emilia.books, function (book) {
                var climbs = _.where($scope.climbs, {book_id: book.id}),
                    regions = _.map(_.uniq(_.pluck(climbs, 'region_id')), function (region_id) {
                        return _.findWhere(Emilia.regions, {id: region_id});
                    });

                $scope.books[book.id] = _.extend({
                    climbs: climbs,
                    regions: regions
                }, book);
            });

            $scope.selectBook(DEFAULT_BOOK_ID);
        };
    }]);
