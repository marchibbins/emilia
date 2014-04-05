from flask import request
from wtforms.validators import ValidationError
import os


class UniqueValidator(object):

    """ Validates uniqueness of field on model, used by forms. """

    def __init__(self, model, field):
        self.model = model
        self.field = field
        self.message = u'%s with this %s already exists.' % (model.__name__, field.name)

    def __call__(self, form, field):
        obj_id = form.data.get('id')
        if self.model.query.filter(self.model.id != obj_id, self.field == field.data).count() > 0:
            raise ValidationError(self.message)


def env_var(key, default=None, required=False, integer=False):
    """ Parses environment variables based on type and requirement, used in configuration. """
    if required:
        # Throw KeyError for missing requirements
        val = os.environ[key]
    else:
        # Use default or None
        val = os.environ.get(key, default)

    # Replace booleans
    if val == 'True':
        val = True
    elif val == 'False':
        val = False

    if integer:
        return int(val)
    else:
        return val


def full_path_cache_key_prefix():
    return 'view/%s' % request.full_path


def lowercase_filter(data):
    """ Converts string data to lowercase, used by forms. """
    if data:
        return data.lower()
    else:
        return data


def format_time_filter(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if h > 0:
        return '%d:%02d:%02d' % (h, m, s)
    else:
        return '%02d:%02d' % (m, s)
