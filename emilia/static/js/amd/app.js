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
        $('.js-leaders').each(function (el) {
            leaderboards.init(el);
        });
    });
});
