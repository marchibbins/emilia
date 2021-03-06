from flask.ext.script import Manager, Shell

from emilia import init
from emilia.climbs import fixtures as climb_fixtures
from emilia.extensions import db
from emilia.user import fixtures as user_fixtures


app = init()
manager = Manager(app)


@manager.command
def run():
    """ Runs application locally, host and port set by configuration. """
    app.run()


@manager.command
def setup():
    """ Inits database, installing fixture data. """
    db.drop_all()
    db.create_all()

    # Install fixutres
    climb_fixtures.install()
    user_fixtures.install()


@manager.shell
def make_shell_context():
    """ Configures shell setup. """
    # http://flask-script.readthedocs.org/en/latest/#default-commands
    return dict(app=app, db=db)


if __name__ == "__main__":
    manager.run()
