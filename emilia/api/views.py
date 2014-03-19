from flask import Blueprint, render_template, jsonify

from emilia.climbs.models import Climb


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def index():
    """ Render full list of Climbs as JSON. """
    climbs = Climb.query.all()
    return jsonify(status='success', climbs=[i.serialize() for i in climbs])


@api.errorhandler(404)
def page_not_found(error):
    """ Custom 404 for this blueprint. Note: only handles exceptions
        raised by view functions, not missing routes under this url prefix. """
    # http://flask.pocoo.org/docs/api/#flask.Blueprint.errorhandler
    return jsonify(status='error', description='Not found'), 404
