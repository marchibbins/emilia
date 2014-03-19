import os


def env_var(key, default=None, required=False):
    """ Parses environment variables based on type and requirement. """
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
