require([
    '$',
    'domready',
    'leaderboards'
],
function(
    $,
    domready,
    leaderboards
) {
    // Remove noscript class
    $('html').removeClass('js-off');

    domready(function () {
        $('.js-leaderboard').each(function (el) {
            leaderboards.render(el);
        });
    });
});