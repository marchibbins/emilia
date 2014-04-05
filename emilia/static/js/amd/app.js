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
    // Remove noscript class
    $('html').removeClass('js-off');

    domready(function () {
        $('.js-climb-leaders').each(function (el) {
            ClimbLeaders.init(el);
        });
    });
});
