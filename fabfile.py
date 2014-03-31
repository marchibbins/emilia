from fabric.api import local, task
from fabric.contrib.console import confirm


def honcho(command):
    """ Run Honcho command. """
    local('honcho %s' % command)


def honcho_run(command):
    """ Run a command using Honcho. """
    honcho('run %s' % command)


@task
def run():
    """ Run with Gunicorn server. """
    honcho('start')


@task
def dev():
    """ Run with Flask server. """
    honcho_run('python manage.py run')


@task
def setup():
    """ Set up application and database. """
    if confirm('This action will completely destroy and rebuild the database. ' \
                'Are you sure you want to do this?', default=False):
        honcho_run('python manage.py setup')


@task
def shell():
    """ Start an interactive shell within application environment. """
    honcho_run('python manage.py shell')


@task
def test(pattern=''):
    """ Run tests. """
    honcho_run('python test.py %s' % pattern)


@task
def clean():
    """ Delete pyc files. """
    local('find . -name \*.pyc -delete')
