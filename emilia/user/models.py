from flask.ext.login import UserMixin
from sqlalchemy import Column
from werkzeug import generate_password_hash, check_password_hash

from emilia.extensions import db


class User(db.Model, UserMixin):

    """ Basic User model, username and encrypted password. """

    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(64), nullable=False, unique=True)
    password_store = Column('password', db.String(), nullable=False)

    def get_password(self):
        return self.password_store

    def set_password(self, password):
        self.password_store = generate_password_hash(password)

    def check_password(self, password):
        if self.password is None:
            return False

        return check_password_hash(self.password, password)

    password = db.synonym('password_store',
                          descriptor=property(get_password, set_password))

    @classmethod
    def authenticate(self, username, password):
        """ Attempts User select by username and password match. """
        user = self.query.filter_by(username=username).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False

        return user, authenticated

    def __init__(self, username, password):
        """ Populates model properties. """
        self.username = username
        self.password = password

    def __repr__(self):
        """ Returns the User object representation. """
        return '<User %r>' % self.username

    def __unicode__(self):
        """ Returns a string representation of the User object. """
        return '%s' % self.username


def user_loader(id):
    """ Loads (or reloads) a User object, used by LoginManager. """
    return User.query.get(id)
