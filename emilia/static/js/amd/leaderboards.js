define([
    'reqwest',
    '$'
],
function(
    reqwest,
    $
) {
    'use strict';
    function Leaderboards(settings) {

        var el,
            config = {
                type: '',
                slug: '',
                classes: '',
                label: '',
                limit: null,
                page: 1
            };

        for (var prop in settings) {
            config[prop] = settings[prop];
        }

        this.create = function() {
            el = $.create('<div>');
            el.loading = true;

            var url = '/api/climbs/:slug/:type'.replace(':slug', config.slug).replace(':type', config.type);
            if (config.page > 1) {
                url += '?page=' + config.page;
            }

            reqwest({
                scope: this,
                url: url,
                error: this.handlApiError,
                success: this.handleApiResponse
            });

            return el;
        };

        this.handleApiResponse = function(response) {
            var maleObj = 'male_' + config.type,
                femaleObj = 'female_' + config.type,

                maleLabel = this.scope.label('Male'),
                femaleLabel = this.scope.label('Female'),

                maleLeaderboard = $.create(this.scope.createHtml(maleLabel, response[maleObj])),
                femaleLeaderboard = $.create(this.scope.createHtml(femaleLabel, response[femaleObj]));

            el.replaceWith(maleLeaderboard);
            maleLeaderboard.after(femaleLeaderboard);

            el.loading = false;
        };

        this.handlApiError = function(error) {
            //
        };

        this.createHtml = function(label, data) {
            var index = 0,
                items = '',
                pagination = '',
                count = config.limit || Math.max(data.entries.length, 1),
                entry;

            for (index; index < count; index++) {
                entry = data.entries[index];
                if (entry) {
                    items += '<li>' + entry.athlete_name + ': ' + this.formatTime(entry.elapsed_time) + '</li>';
                } else {
                    items += '<li>None</li>';
                }
            }

            if (data.entry_count > count) {
                pagination = '<div>Showing ' + count + ' of ' + data.entry_count + '</div>';
            }

            return '<div class="js-leaderboard leaderboard ' + config.classes + '">' +
                       '<h2>' + label + '</h2>' + '<ol>' + items + '</ol>' + pagination +
                   '</div>';
        };

        this.label = function(gender) {
            return gender + ' ' + (config.label || config.type);
        };

        this.formatTime = function(time) {
            var hours = parseInt(time / 3600, 10) % 24,
                minutes = parseInt(time / 60, 10) % 60,
                seconds = parseInt(time, 10) % 60;
            return (hours > 0 ? hours + ':' : '') +
                   (minutes < 10 ? '0' + minutes : minutes) +
                   ':' + (seconds < 10 ? '0' + seconds : seconds);
        };
    }

    return Leaderboards;

});
