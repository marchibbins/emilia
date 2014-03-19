from emilia.extensions import db
from emilia.user.models import User
from emilia.utils import env_var


def install():
    """ Adds admin User to database. """
    admin = User('admin', env_var('DEFAULT_ADMIN_PASSWORD', required=True))
    db.session.add(admin)
