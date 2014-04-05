define([
    'bean',
    'reqwest',
    '$'
],
function(
    bean,
    reqwest,
    $
) {
    var classes = {
            hidden: 'is-hidden',
            leaderboard: 'js-leaders',
            loading: 'js-leaders-loading',
            toggle: 'js-leaders-toggle'
        },
        data = {
            climbSlug: 'data-climb-slug',
            toggleText: 'data-toggle-text'
        },
        dom = {},
        labels = {
            loading: 'Loading',
            maleOverallLeaders: 'Male overall leaders',
            femaleOverallLeaders: 'Female overall leaders',
            showClubLeaders: 'Show club leaders',
            showOverallLeaders: 'Show overall leaders'
        },
        leadersCount = 3,
        apiPending = true,
        togglePending = false;

    function init(el) {
        dom.el = el;

        var slug = dom.el.getAttribute(data.climbSlug),
            url = '/api/climbs/:slug/leaders'.replace(':slug', slug);

        reqwest(url, handleApiResponse);
        addToggle();
    }

    function handleApiResponse(response) {
        var maleHtml = createLeaderboardHtml(labels.maleOverallLeaders, response.male_leaders),
            femaleHtml = createLeaderboardHtml(labels.femaleOverallLeaders, response.female_leaders);

        $('.' + classes.leaderboard).last().after(maleHtml + femaleHtml);
        apiPending = false;

        if (togglePending) {
            toggleLeaderboards();
            removeLoading();
        }
    }

    function createLeaderboardHtml(label, data) {
        var index = 0,
            items = '',
            count = Math.max(data.entries.length, leadersCount),
            entry;

        for (index; index < count; ++index) {
            entry = data.entries[index];
            if (entry) {
                items += '<li>' + entry.athlete_name + ': ' + formatTime(entry.elapsed_time) + '</li>';
            } else {
                items += '<li>None</li>';
            }
        }

        return '<div class="leaderboard ' + classes.leaderboard + ' ' + classes.hidden + '">' +
                   '<h2>' + label + '</h2>' + '<ol>' + items + '</ol>' +
               '</div>';
    }

    function toggleLeaderboards() {
        $('.' + classes.leaderboard).toggleClass(classes.hidden);

        var toggleText = dom.toggle.attr(data.toggleText),
            text = dom.toggle.text();

        dom.toggle.text(toggleText).attr(data.toggleText, text);
    }

    function addToggle() {
        dom.toggle = $.create('<a href="#toggle-leaders" title="" class="' + classes.toggle + '" ' + data.toggleText + '="' + labels.showClubLeaders + '">' + labels.showOverallLeaders + '</a>');
        $(dom.el).append(dom.toggle);

        bean.on(dom.toggle[0], 'click', function (event) {
            event.preventDefault();
            if (apiPending === true) {
                togglePending = true;
                addLoading();
            } else {
                toggleLeaderboards();
            }
        });
    }

    function addLoading() {
        dom.loading = $.create('<div class="' + classes.loading + '">' + labels.loading + '</div>');
        dom.toggle.after(dom.loading).hide();
    }

    function removeLoading() {
        dom.toggle.show();
        dom.loading.hide();
    }

    function formatTime(time) {
        var hours = parseInt(time / 3600, 10) % 24,
            minutes = parseInt(time / 60, 10) % 60,
            seconds = parseInt(time, 10) % 60;
        return (hours > 0 ? hours + ":" : '') + (minutes < 10 ? '0' + minutes : minutes) + ':' + (seconds < 10 ? '0' + seconds : seconds);
    }

    return {
        init: init
    };
});
