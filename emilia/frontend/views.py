from flask import Blueprint, render_template

from emilia.climbs.models import Climb


frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    """ Render full list of Climbs. """
    climbs = Climb.query.all()
    return render_template('frontend/index.html', climbs=climbs)
