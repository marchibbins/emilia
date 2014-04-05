require([
    '$',
    'domready',
    'climb-leaders'
],
function(
    $,
    domready,
    ClimbLeaders
) {
    // Remove no-js class
    document.documentElement.className = "js-on";

    domready(function () {
        $('.js-climb-leaders').each(function (el) {
            ClimbLeaders.init(el);
        });
    });
});
