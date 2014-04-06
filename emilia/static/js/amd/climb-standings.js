define([
    'leaderboards',
    'bean',
    '$'
],
function(
    Leaderboards,
    bean,
    $
) {
    var dom = {},
        togglePending = false;

    function init(el) {
        dom.el = el;
        addLeaderboards();
        addToggle();
    }

    function addLeaderboards() {
        var slug = dom.el.getAttribute('data-climb-slug');

        dom.leaderboards = new Leaderboards({
            type: 'leaderboard',
            slug: slug,
            classes: 'is-hidden',
            label: 'overall standings'
        }).create();

        dom.club_leaderboards = new Leaderboards({
            type: 'club_leaderboard',
            slug: slug,
            label: 'club standings'
        }).create();

        $(dom.el).prepend(dom.leaderboards);
        $(dom.el).prepend(dom.club_leaderboards);
    }

    function addToggle() {
        dom.toggle = $.create('<a href="#toggle-standings" title="" class="js-standings-toggle" data-toggle-text="Show club standings">Show overall standings</a>');
        $(dom.el).append(dom.toggle);
        bean.on(dom.toggle[0], 'click', clickToggle);
    }

    function clickToggle(event) {
        event.preventDefault();
        if (dom.leaderboards.loading === true) {
            togglePending = true;
            addLoading();
        } else {
            toggleLeaderboards();
        }
    }

    function toggleLeaderboards() {
        $('.js-leaderboard', dom.el).toggleClass('is-hidden');

        var toggleText = dom.toggle.attr('data-toggle-text'),
            text = dom.toggle.text();

        dom.toggle.text(toggleText).attr('data-toggle-text', text);
    }

    function addLoading() {
        dom.loading = $.create('<div class="js-standings-loading">Loading</div>');
        dom.toggle.after(dom.loading).hide();
    }

    function removeLoading() {
        dom.toggle.show();
        dom.loading.hide();
    }

    return {
        init: init
    };
});
