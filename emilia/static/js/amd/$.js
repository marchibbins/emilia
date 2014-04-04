define(['bonzo', 'qwery'], function(bonzo, qwery) {
    return function $(selector, context) {
        return bonzo(qwery(selector, context));
    };
});
