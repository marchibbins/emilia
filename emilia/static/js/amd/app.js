require([
    '$',
    'domready',
    'climb-leaders',
    'climb-standings'
],
function(
    $,
    domready,
    ClimbLeaders,
    ClimbStandings
) {
    // Remove no-js class
    document.documentElement.className = "js-on";

    domready(function () {
        $('.js-climb-leaders').each(function (el) {
            ClimbLeaders.init(el);
        });
        $('.js-climb-standings').each(function (el) {
            ClimbStandings.init(el);
        });
    });
});
