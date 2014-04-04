from stravalib import Client
from stravalib.model import Segment, SegmentLeaderboard, SegmentLeaderboardEntry
import requests

from emilia.extensions import cache
from emilia.utils import env_var


class Stravalib(object):

    """ Wrapper class for Stravalib Client - patches some unfinished methods, adds some serialization helpers. """

    CLUB_ID = 52733
    NUMBER_OF_LEADERS = 3

    def init_app(self, app):
        """ Inits Stravalib client, with token from env. """
        access_token = app.config['STRAVA_ACCESS_TOKEN']
        self.client = Client(access_token=access_token)

    def get_or_cache_call(self, cls, resource, *args, **kwargs):
        """ Retrives object from cache or Strava, marshalling as required. """
        cache_key = '%s_%s_%s' % (resource, '_'.join('%s' % i for i in args), '_'.join('%s:%s' % (k, v) for k, v in kwargs.items() if v))
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


def get_segment_leaderboard(self, segment_id, gender=None, club_id=None, page=None, top_results_limit=None):
    """ Gets the leaderboard for a segment. Overrides default method to take page parameter, ignoring unused others. """
    params = {}
    if gender is not None:
        if gender.upper() not in ('M', 'F'):
            raise ValueError("Invalid gender: {0}. Possible values: 'M' or 'F'".format(gender))
        params['gender'] = gender

    if club_id is not None:
        params['club_id'] = club_id

    if page is not None:
        params['page'] = page

    if top_results_limit is not None:
        params['per_page'] = top_results_limit

    return SegmentLeaderboard.deserialize(self.protocol.get('/segments/{id}/leaderboard', id=segment_id, **params), bind_client=self)


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


Client.get_segment_leaderboard = get_segment_leaderboard
Segment.serialize = serialize_segment
SegmentLeaderboard.serialize = serialize_segment_leaderboard
SegmentLeaderboardEntry.serialize = serialize_segment_leaderboard_entry


strava = Stravalib()
