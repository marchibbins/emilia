define([
    '$'
],
function(
    $
) {
    function render(el) {
        console.log('render');
    }

    return {
        render: render
    };
});