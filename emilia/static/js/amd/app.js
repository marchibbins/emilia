require(['$', 'domready'], function($, domready) {
    // Remove noscript class
    $('html').removeClass('js-off');

    domready(function () {
        console.log('domready');
    });
});