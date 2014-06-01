angular.module('emilia')
    .controller('emilia-app', ['$scope', function ($scope) {
        var hasSvg = !!document.createElementNS && !!document.createElementNS('http://www.w3.org/2000/svg', 'svg').createSVGRect;
        if (hasSvg) {
            angular.element(document.documentElement).addClass('svg');
        }
    }]);
