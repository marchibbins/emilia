from stravalib import Client
from stravalib.model import Segment, SegmentLeaderboard, SegmentLeaderboardEntry
import requests

from emilia.extensions import cache
from emilia.utils import env_var


class Stravalib(object):

    """ Wrapper class for Stravalib Client. """

    CLUB_ID = 52733
    NUMBER_OF_LEADERS = 3

    def init_app(self, app):
        """ Inits Stravalib client, with token from env. """
        access_token = app.config['STRAVA_ACCESS_TOKEN']
        self.client = Client(access_token=access_token)

    def get_or_cache_call(self, cls, resource, *args, **kwargs):
        """ Retrives object from cache or Strava, marshalling as required. """
        cache_key = '%s_%s_%s' % (resource, '_'.join(str(i) for i in args), '_'.join(str(i) for i in kwargs.itervalues()))
        obj = cache.get(cache_key)
        if obj is None:
            try:
                obj = getattr(self.client, resource)(*args, **kwargs).serialize()
                cache.set(cache_key, obj)
            except requests.exceptions.HTTPError, error:
                raise RuntimeError(error)
        return cls.deserialize(obj)

    def get_segment(self, *args, **kwargs):
        """ Retrives Segment info from cache or Strava. """
        return self.get_or_cache_call(Segment, 'get_segment', *args, **kwargs)

    def get_segment_leaderboard(self, *args, **kwargs):
        """ Retrives Segment Leaderboard info from cache or Strava. """
        return self.get_or_cache_call(SegmentLeaderboard, 'get_segment_leaderboard', *args, **kwargs)

    def get_segment_leaders(self, *args, **kwargs):
        """ Retrives Segment Leaderboard info from cache or Strava. """
        kwargs['top_results_limit'] = self.NUMBER_OF_LEADERS
        return self.get_segment_leaderboard(*args, **kwargs)

    def get_segment_club_leaders(self, *args, **kwargs):
        """ Retrives Segment Leaderboard info from cache or Strava. """
        kwargs['club_id'] = self.CLUB_ID
        return self.get_segment_leaders(*args, **kwargs)


def serialize_segment(self):
    """ Returns basic Segment data for serialization. """
    return {
        'id': self.id,
        'distance': self.distance.num,
        'average_grade': self.average_grade,
        'maximum_grade': self.maximum_grade,
        'total_elevation_gain': self.total_elevation_gain.num,
    }


def serialize_segment_leaderboard(self):
    """ Returns basic SegmentLeaderboard data for serialization. """
    return {
        'entry_count': self.entry_count,
        'entries': [entry.serialize() for entry in self.entries],
    }


def serialize_segment_leaderboard_entry(self):
    """ Returns basic SegmentLeaderboardEntry data for serialization. """
    return {
        'effort_id': self.effort_id,
        'athlete_id': self.athlete_id,
        'athlete_name': self.athlete_name,
        'elapsed_time': self.elapsed_time.seconds,
    }


Segment.serialize = serialize_segment
SegmentLeaderboard.serialize = serialize_segment_leaderboard
SegmentLeaderboardEntry.serialize = serialize_segment_leaderboard_entry


strava = Stravalib()
