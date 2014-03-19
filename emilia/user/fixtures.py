from emilia.user.models import User
from emilia.extensions import db


def install():
    """ Adds User data to database. """
    users = [
        ('admin', 'password'),
    ]

    for data in users:
        user = User(*data)
        db.session.add(user)
