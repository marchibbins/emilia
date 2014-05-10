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
                console.log('Error:', status);
            });

        $scope.selectBook = function(bookId) {
            $scope.currentBook = $scope.books[bookId];
        };

        $scope.selectClimb = function(climbId) {
            $scope.currentClimb = _.findWhere($scope.climbs, {id: climbId});
        };

        $scope.clickMarker = function($markerModel) {
            $scope.selectClimb($markerModel.id);
            $scope.$apply();
        };

        var init = function(data) {
            $scope.climbs = data.climbs;

            // Book data is already on page
            _.each(document.querySelectorAll('[data-book-id]'), function(el) {
                var bookId = el.getAttribute('data-book-id'),
                    bookName = el.textContent;

                // Create book objects
                $scope.books[bookId] = {
                    id: bookId,
                    short_name: bookName,
                    climbs: [],
                    regions: []
                };

                // Bind buttons
                angular.element(el).on('click', function() {
                    $scope.selectBook(bookId);
                    $scope.$apply();
                });
            });

            // Assign climbs to book
            _.each($scope.climbs, function(climb) {
                // Parse coords for markers
                climb.coords = {
                    latitude: climb.segment.start_latitude,
                    longitude: climb.segment.start_longitude
                };

                book = $scope.books[climb.book_id];
                book.climbs.push(climb);

                // Add region object to book (without duplicates)
                if (!_.findWhere(book.regions, {id: climb.region_id})) {
                    book.regions.push(_.findWhere(Emilia.regions, {id: climb.region_id}));
                }
            });

            $scope.selectBook(DEFAULT_BOOK_ID);
        };
    });
