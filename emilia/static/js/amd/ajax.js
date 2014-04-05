define([
    'reqwest'
], function (
    reqwest
) {
    function ajax(params) {
        return ajax.reqwest(params);
    }

    return ajax;

});
