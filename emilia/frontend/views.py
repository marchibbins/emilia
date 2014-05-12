from flask import Blueprint, render_template

from emilia.climbs.models import Book, Climb, Region
from emilia.climbs.strava import strava
from emilia.extensions import cache


frontend = Blueprint('frontend', __name__)


@frontend.route('/')
@cache.cached()
def index():
    """ Renders the Home page. """
    return render_template('frontend/index.html')


@frontend.route('/books')
@cache.cached()
def book_list():
    """ Renders a full list of Books. """
    context = {
        'books': Book.query.all()
    }
    return render_template('frontend/climbs/book_list.html', **context)


@frontend.route('/books/<slug>')
@cache.cached()
def book_detail(slug):
    """ Renders a detail view for the Book, matching slug. """
    context = {
        'book': Book.query.filter_by(slug=slug).first_or_404()
    }
    return render_template('frontend/climbs/book_detail.html', **context)


@frontend.route('/climbs/<slug>')
@cache.cached()
def climb_detail(slug):
    """ Renders a detail view for the Climb, matching slug. """
    climb = Climb.query.filter_by(slug=slug).first_or_404()
    context = {
        'climb': climb,
        'male_club_leaders': strava.get_segment_club_leaders(climb.strava_id, gender='M'),
        'female_club_leaders': strava.get_segment_club_leaders(climb.strava_id, gender='F'),
    }
    return render_template('frontend/climbs/climb_detail.html', **context)


@frontend.route('/map')
# @cache.cached()
def map():
    """ """
    context = {
        'books': [item.serialize() for item in Book.query.all()],
        'regions': [item.serialize() for item in Region.query.all()]
    }
    return render_template('frontend/map.html', **context)
