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
    books = [item.serialize() for item in Book.query.all()]
    return json_response(books=books)


@api.route('/books/<slug>')
@cache.cached()
def book_detail(slug):
    """ Renders a detail view for the Book, matching slug, as JSON. """
    book = Book.query.filter_by(slug=slug).first_or_404().serialize()
    return json_response(book=book)


@api.route('/climbs/<slug>')
@cache.cached()
def climb_detail(slug):
    """ Renders a detail view for the Climb, matching slug, as JSON. """
    climb = Climb.query.filter_by(slug=slug).first_or_404().serialize()
    segment = strava.get_segment(climb['strava_id']).serialize()
    return json_response(climb=climb, segment=segment)


@api.errorhandler(404)
def page_not_found(error):
    """ Custom 404 for this blueprint. Note: only handles exceptions
        raised by view functions, not missing routes under this url prefix. """
    # http://flask.pocoo.org/docs/api/#flask.Blueprint.errorhandler
    return json_response(404, description='Not found')
