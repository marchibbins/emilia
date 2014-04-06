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
                slug: slug,
                label: 'overall standings'
            }).create(),

            club_leaderboards = new Leaderboards({
                type: 'club_leaderboard',
                slug: slug,
                label: 'club standings'
            }).create();

        $(el).prepend(leaderboards);
        $(el).prepend(club_leaderboards);
    }

    return {
        init: init
    };
});
