/*global emilia:true */
require([], function() {
    document.documentElement.className = document.documentElement.className.replace(/\bjs-off\b/g, '') + 'js-on';
});