angular.module('emilia', ['google-maps'])
    .controller('emilia-map', function ($scope) {

        var DEFAULT_CENTER = {
                latitude: 54.5,
                longitude: -4
            },

            DEFAULT_DRAGGABLE = true;
            DEFAULT_ZOOM = 6;

        // Map config
        $scope.map = {
            center: DEFAULT_CENTER,
            draggable: DEFAULT_DRAGGABLE,
            zoom: DEFAULT_ZOOM
        };
    });
