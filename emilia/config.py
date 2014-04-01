import os

from emilia.utils import env_var


class Config(object):

    """ Creates a config objectbased on envionment variables. """

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = env_var('DEBUG', default=False)
    SERVER_NAME = env_var('SERVER_NAME', required=True)

    # Logging
    LOG_FOLDER = env_var('LOG_FOLDER', default='logs')
    FILE_LOGGING = True

    try:
        if not os.path.exists(LOG_FOLDER) or not os.access(LOG_FOLDER, os.W_OK):
            os.mkdir(LOG_FOLDER)
    except Exception, e:
        FILE_LOGGING = False

    LOG_NAME = env_var('LOG_NAME', default='info.log')
    LOG_PATH = os.path.join(LOG_FOLDER, LOG_NAME)
    LOG_MAX_BYTES = env_var('LOG_MAX_BYTES', default='info.log')
    LOG_BACKUP_COUNT = env_var('LOG_BACKUP_COUNT', default='info.log')

    # Flask-Cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = env_var('CACHE_TYPE', default='simple')
    CACHE_DEFAULT_TIMEOUT = env_var('CACHE_DEFAULT_TIMEOUT', default=60)

    # Flask-SQLAlchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
    SQLALCHEMY_DATABASE_URI = env_var('SQLALCHEMY_DATABASE_URI', required=True)
    SQLALCHEMY_ECHO = env_var('SQLALCHEMY_ECHO', default=False)

    # Flask-Login: http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = env_var('SECRET_KEY', required=True)

    # Stravalib: https://github.com/hozn/stravalib
    STRAVA_ACCESS_TOKEN = env_var('STRAVA_ACCESS_TOKEN', required=True)
