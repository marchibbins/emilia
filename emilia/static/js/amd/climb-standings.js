define([
    'leaderboards',
    '$'
],
function(
    Leaderboards,
    $
) {
    var data = {
            climbSlug: 'data-climb-slug'
        };

    function init(el) {
        var slug = el.getAttribute(data.climbSlug),
            leaderboards = new Leaderboards({
                type: 'leaderboard',
                slug: slug
            }).create();

        $(el).html(leaderboards);
    }

    return {
        init: init
    };
});
