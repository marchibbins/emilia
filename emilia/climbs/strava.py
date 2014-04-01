from stravalib import Client

from emilia.utils import env_var


class Stravalib(object):

    """ Wrapper class for Stravalib Client. """

    def init_app(self, app):
        access_token = app.config['STRAVA_ACCESS_TOKEN']
        self.client = Client(access_token=access_token)

strava = Stravalib()
