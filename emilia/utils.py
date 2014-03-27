from wtforms.validators import ValidationError
import os


class UniqueValidator(object):

    """ Validates uniqueness of field on model, used by forms. """

    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'%s with this %s already exists.' % (model.__name__, field.name)
        self.message = message

    def __call__(self, form, field):
        if self.model.query.filter(self.field == field.data).count() > 0:
            raise ValidationError(self.message)


def env_var(key, default=None, required=False):
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

    return val


def lowercase_filter(data):
    """ Converts string data to lowercase, used by forms. """
    if data:
        return data.lower()
    else:
        return data