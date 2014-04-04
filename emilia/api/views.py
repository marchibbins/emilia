from flask import Blueprint, jsonify
from itertools import chain

from emilia.climbs.models import Book, Climb
from emilia.climbs.strava import strava
from emilia.extensions import cache


api = Blueprint('api', __name__, url_prefix='/api')


def json_response(code=200, **kwargs):
    """ Jsonify a response with status message and response code. """
    if code < 400:
        status = 'success'
    else:
        status = 'error'

    default = {
        'status': status,
    }

    response = dict(chain(default.iteritems(), kwargs.iteritems()))
    return jsonify(response), code


@api.route('/')
@cache.cached()
def index():
    """ Renders API index. """
    return json_response()


@api.route('/books')
@cache.cached()
def book_list():
    """ Renders a full list of Books as JSON. """
    context = {
        'books': [item.serialize() for item in Book.query.all()]
    }
    return json_response(**context)


@api.route('/books/<slug>')
@cache.cached()
def book_detail(slug):
    """ Renders a detail view for the Book, matching slug, as JSON. """
    context = {
        'book': Book.query.filter_by(slug=slug).first_or_404().serialize()
    }
    return json_response(**context)


@api.route('/climbs/<slug>')
@cache.cached()
def climb_detail(slug):
    """ Renders a detail view for the Climb, matching slug, as JSON. """
    climb = Climb.query.filter_by(slug=slug).first_or_404()
    context = {
        'climb': climb.serialize(),
        'segment': strava.get_segment(climb.strava_id).serialize(),
        'male_club_leaders': strava.get_segment_club_leaders(climb.strava_id, gender='M').serialize(),
        'female_club_leaders': strava.get_segment_club_leaders(climb.strava_id, gender='F').serialize(),
    }
    return json_response(**context)


@api.route('/climbs/<slug>/club_leaders')
@cache.cached()
def climb_club_leaders(slug):
    """ Renders top Climb club leaders, matching slug, as JSON. """
    climb = Climb.query.filter_by(slug=slug).first_or_404()
    context = {
        'climb': climb.serialize(),
        'male_club_leaders': strava.get_segment_club_leaders(climb.strava_id, gender='M').serialize(),
        'female_club_leaders': strava.get_segment_club_leaders(climb.strava_id, gender='F').serialize(),
    }
    return json_response(**context)


@api.route('/climbs/<slug>/leaders')
@cache.cached()
def climb_leaders(slug):
    """ Renders top Climb leaders, matching slug, as JSON. """
    climb = Climb.query.filter_by(slug=slug).first_or_404()
    context = {
        'climb': climb.serialize(),
        'male_leaders': strava.get_segment_leaders(climb.strava_id, gender='M').serialize(),
        'female_leaders': strava.get_segment_leaders(climb.strava_id, gender='F').serialize(),
    }
    return json_response(**context)


@api.route('/climbs/<slug>/leaderboard')
@cache.cached()
def climb_leaderboard(slug):
    """ Renders overall Climb leaderboard, matching slug, as JSON. """
    climb = Climb.query.filter_by(slug=slug).first_or_404()
    context = {
        'climb': climb.serialize(),
        'male_leaderboard': strava.get_segment_leaderboard(climb.strava_id, gender='M').serialize(),
        'female_leaderboard': strava.get_segment_leaderboard(climb.strava_id, gender='F').serialize(),
    }
    return json_response(**context)


@api.errorhandler(404)
def page_not_found(error):
    """ Custom 404 for this blueprint. Note: only handles exceptions
        raised by view functions, not missing routes under this url prefix. """
    # http://flask.pocoo.org/docs/api/#flask.Blueprint.errorhandler
    return json_response(404, description='Not found')
