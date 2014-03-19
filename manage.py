from flask.ext.script import Manager, Shell

from emilia import init
from emilia.extensions import db
from emilia.user import models as user_models

app = init()
manager = Manager(app)


@manager.command
def run():
    """ Run locally, host and port set by configuration. """
    app.run()


@manager.command
def setup():
    """ Init database and admin user. """
    db.drop_all()
    db.create_all()

    # Admin user
    admin = user_models.User(username=u'admin', password=u'password')
    db.session.add(admin)

    db.session.commit()


@manager.shell
def make_shell_context():
    """ Configure shell setup. """
    # http://flask-script.readthedocs.org/en/latest/#default-commands
    return dict(app=app, db=db)


if __name__ == "__main__":
    manager.run()