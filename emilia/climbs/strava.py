from stravalib import Client
from stravalib.model import Segment
import requests

from emilia.utils import env_var


class Stravalib(object):

    """ Wrapper class for Stravalib Client. """

    def init_app(self, app):
        access_token = app.config['STRAVA_ACCESS_TOKEN']
        self.client = Client(access_token=access_token)

    def get_segment(self, *args, **kwargs):
        try:
            return self.client.get_segment(*args, **kwargs)
        except requests.exceptions.HTTPError, error:
            raise RuntimeError(error)

    def get_segment_leaderboard(self, *args, **kwargs):
        try:
            return self.client.get_segment_leaderboard(*args, **kwargs)
        except requests.exceptions.HTTPError, error:
            raise RuntimeError(error)


def serialize_segment(self):
    """ Returns basic object data for serialization. """
    return {
        'distance': self.distance.num,
        'average_grade': self.average_grade,
        'maximum_grade': self.maximum_grade,
        'total_elevation_gain': self.total_elevation_gain.num,
    }

Segment.serialize = serialize_segment


strava = Stravalib()
