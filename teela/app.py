from flask import Flask, render_template
from logging.handlers import RotatingFileHandler
import logging

from teela.admin import admin
from teela.api import api
from teela.config import Config
from teela.extensions import cache, db, login_manager
from teela.frontend import frontend
from teela.user import user, user_loader


def init():
    """ Create a Flask app. """
    app = Flask(__name__)

    configure_app(app)
    configure_extensions(app)
    configure_blueprints(app)
    configure_logging(app)
    configure_error_handlers(app)

    return app


def configure_app(app):
    """ Configure app with config object. """
    # http://flask.pocoo.org/docs/api/#configuration
    app.config.from_object(Config)


def configure_extensions(app):
    """ Configure Flask extensions. """
    # flask-cache
    cache.init_app(app)

    # flask-sqlalchemy
    db.init_app(app)

    # flask-login
    @login_manager.user_loader
    def load_user(id):
        return user_loader(id)

    login_manager.login_message = u'Please log in to access this page.'
    login_manager.login_view = 'user.login'
    login_manager.refresh_message = u'Please reauthenticate to access this page.'
    login_manager.refresh_view = 'user.reauth'
    login_manager.setup_app(app)


def configure_blueprints(app):
    """ Configure blueprints. """
    app.register_blueprint(admin)
    app.register_blueprint(api)
    app.register_blueprint(frontend)
    app.register_blueprint(user)


def configure_logging(app):
    """ Configure logging. """
    # Skip logging configuration for debug mode.
    if app.debug:
        return

    # http://flask.pocoo.org/docs/errorhandling/
    app.logger.setLevel(logging.INFO)

    log_file_handler = RotatingFileHandler(Config.LOG_PATH, Config.LOG_MAX_BYTES, Config.LOG_BACKUP_COUNT)
    log_file_handler.setLevel(logging.INFO)
    log_file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(log_file_handler)


def configure_error_handlers(app):
    """ Configure error templates. """
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template('errors/500.html'), 500
