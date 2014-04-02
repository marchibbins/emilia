from stravalib import Client
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


strava = Stravalib()
