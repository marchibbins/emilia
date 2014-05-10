angular.module('emilia', ['google-maps'])
    .controller('emilia-map', function ($scope, $http) {
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
            .success(function(data, status, headers, config) {
                init(data);
            })
            .error(function(data, status, headers, config) {
                console.log("Error:", status);
            });

        $scope.selectBook = function(bookId) {
            $scope.currentBook = $scope.books[bookId];
        };

        $scope.selectClimb = function(climbId) {
            $scope.currentClimb = _.findWhere($scope.climbs, {id: climbId});
            $scope.$apply();
        };

        $scope.clickMarker = function($markerModel) {
            $scope.selectClimb($markerModel.id);
        };

        var init = function(data) {
            $scope.climbs = data.climbs;

            // Create book objects
            var bookIds = _.uniq(_.pluck($scope.climbs, 'book_id'));
            _.each(bookIds, function(id) {
                $scope.books[id] = {
                    id: id,
                    climbs: []
                };
            });

            // Assign climbs to book
            _.each($scope.climbs, function(climb) {
                // Parse coords for markers
                climb.coords = {
                    latitude: climb.segment.start_latitude,
                    longitude: climb.segment.start_longitude
                };
                $scope.books[climb.book_id].climbs.push(climb);
            });

            $scope.selectBook(DEFAULT_BOOK_ID);
        };
    });
