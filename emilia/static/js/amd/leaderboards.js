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
            leaderboard: 'js-leaderboard',
            loading: 'js-leaderboard-loading',
            toggle: 'js-leaderboard-toggle'
        },
        dom = {},
        labels = {
            loading: 'Loading',
            showClubLeaders: 'Show club leaders',
            showOverallLeaders: 'Show overall leaders'
        },
        leadersCount = 3,
        apiPending = true,
        togglePending = false;

    function init(el) {
        dom.el = el;
        reqwest('/api/climbs/cheddar-gorge/leaders', handleApiResponse);
        addToggle();
    }

    function handleApiResponse(response) {
        var maleHtml = createLeaderboardHtml('Male leaders', response.male_leaders),
            femaleHtml = createLeaderboardHtml('Female leaders', response.female_leaders);

        $(dom.el).append(maleHtml + femaleHtml);
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
                items += '<li>' + entry.athlete_name + ': ' + entry.elapsed_time + '</li>';
            } else {
                items += '<li>None</li>';
            }
        }

        return '<div class="leaderboard js-leaderboard is-hidden">' +
                   '<h2>' + label +' (of ' + data.entry_count + ' total)</h2>' +
                   '<ol>' + items + '</ol>' +
               '</div>';
    }

    function toggleLeaderboards() {
        $('.' + classes.leaderboard).toggleClass('is-hidden');

        var toggleText = dom.toggle.attr('data-toggle-text'),
            text = dom.toggle.text();

        dom.toggle.text(toggleText).attr('data-toggle-text', text);
    }

    function addToggle() {
        dom.toggle = $.create('<a href="#toggle-leaders" title="" class="' + classes.toggle + '" data-toggle-text="' + labels.showClubLeaders + '">' + labels.showOverallLeaders + '</a>');
        $(dom.el).prepend(dom.toggle);

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

    return {
        init: init
    };
});
