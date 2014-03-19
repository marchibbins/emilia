from flask import Blueprint, jsonify
from itertools import chain

from emilia.climbs.models import Climb


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
def index():
    """ Render full list of Climbs as JSON. """
    climbs = [climb.serialize() for climb in Climb.query.all()]
    return json_response(climbs=climbs)


@api.errorhandler(404)
def page_not_found(error):
    """ Custom 404 for this blueprint. Note: only handles exceptions
        raised by view functions, not missing routes under this url prefix. """
    # http://flask.pocoo.org/docs/api/#flask.Blueprint.errorhandler
    return json_response(404, description='Not found')
