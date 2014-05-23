from flask import abort, Blueprint, jsonify, request
from itertools import chain

from emilia.climbs.models import Book, Climb
from emilia.climbs.strava import strava
from emilia.config import Config
from emilia.extensions import cache
from emilia.utils import full_path_cache_key_prefix


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
@cache.cached(timeout=Config.CACHE_API_TIMEOUT)
def index():
    """ Renders API index. """
    return json_response()


@api.route('/books')
@cache.cached(timeout=Config.CACHE_API_TIMEOUT)
def book_list():
    """ Renders a full list of Books as JSON. """
    context = {
        'books': [item.serialize() for item in Book.query.all()]
    }
    return json_response(**context)


@api.route('/books/<slug>')
@cache.cached(timeout=Config.CACHE_API_TIMEOUT)
def book_detail(slug):
    """ Renders a detail view for the Book, matching slug, as JSON. """
    context = {
        'book': Book.query.filter_by(slug=slug).first_or_404().serialize()
    }
    return json_response(**context)


@api.route('/books/<slug>/climbs')
@cache.cached(timeout=Config.CACHE_API_TIMEOUT)
def book_climbs(slug):
    """ Renders a list of Climbs view for the Book, matching slug, as JSON. """
    book = Book.query.filter_by(slug=slug).first_or_404()
    context = {
        'book': book.serialize_summary(),
        'climbs': [item.serialize_summary() for item in book.climbs.order_by('number')]
    }
    return json_response(**context)


@api.route('/climbs')
@cache.cached(timeout=Config.CACHE_API_TIMEOUT)
def climb_list():
    """ Renders a full list of Climbs as JSON. """
    context = {
        'climbs': [item.serialize_summary() for item in Climb.query.all()]
    }
    return json_response(**context)


@api.route('/climbs/<slug>')
@cache.cached(timeout=Config.CACHE_STRAVA_TIMEOUT)
def climb_detail(slug):
    """ Renders a detail view for the Climb, matching slug, as JSON. """
    climb = Climb.query.filter_by(slug=slug).first_or_404()
    context = {
        'climb': climb.serialize(),
        'male_club_leaders': strava.get_segment_club_leaders(climb.strava_id, gender='M').serialize(),
        'female_club_leaders': strava.get_segment_club_leaders(climb.strava_id, gender='F').serialize(),
    }
    return json_response(**context)


@api.route('/climbs/<slug>/<leaderboard>')
@api.route('/climbs/<slug>/<leaderboard>/<gender>')
@cache.cached(timeout=Config.CACHE_STRAVA_TIMEOUT, key_prefix=full_path_cache_key_prefix)
def climb_leaderboard(slug, leaderboard, gender=None):
    """ Renders top Climb club leaders, matching slug, as JSON. """
    climb = Climb.query.filter_by(slug=slug).first_or_404()
    context = {
        'climb': {
            'id': climb.id,
            'slug': climb.slug,
            'strava_id': climb.strava_id,
        }
    }

    resources = {
        'club_leaders': 'get_segment_club_leaders',
        'club_leaderboard': 'get_segment_club_leaderboard',
        'leaders': 'get_segment_leaders',
        'leaderboard': 'get_segment_leaderboard',
    }

    try:
        resource = getattr(strava, resources[leaderboard])
    except KeyError:
        abort(404)

    if gender and gender not in ('male', 'female'):
        abort(404) # Enforce options

    if leaderboard not in ('club_leaders', 'leaders'):
        page = request.args.get('page')
    else:
        page = None # Pagination not allowed

    if gender != 'female':
        context['male_%s' % leaderboard] = resource(climb.strava_id, page=page, gender='M').serialize()

    if gender != 'male':
        context['female_%s' % leaderboard] = resource(climb.strava_id, page=page, gender='F').serialize()

    return json_response(**context)


@api.route('/climbs/<slug>/stream')
@cache.cached(timeout=Config.CACHE_STRAVA_TIMEOUT)
def climb_stream(slug):
    """ Renders a segment stream the Climb, matching slug, as JSON. """
    climb = Climb.query.filter_by(slug=slug).first_or_404()
    context = {
        'climb': climb.serialize(),
        'stream': strava.get_segment_stream(climb.strava_id).serialize(),
    }
    return json_response(**context)


@api.errorhandler(404)
def page_not_found(error):
    """ Custom 404 for this blueprint. Note: only handles exceptions
        raised by view functions, not missing routes under this url prefix. """
    # http://flask.pocoo.org/docs/api/#flask.Blueprint.errorhandler
    return json_response(404, description='Not found')
