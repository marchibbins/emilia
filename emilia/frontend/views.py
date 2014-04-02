from flask import Blueprint, render_template

from emilia.climbs.models import Book, Climb
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
    books = Book.query.all()
    return render_template('frontend/climbs/book_list.html', books=books)


@frontend.route('/books/<slug>')
@cache.cached()
def book_detail(slug):
    """ Renders a detail view for the Book, matching slug. """
    book = Book.query.filter_by(slug=slug).first_or_404()
    return render_template('frontend/climbs/book_detail.html', book=book)


@frontend.route('/climbs/<slug>')
@cache.cached()
def climb_detail(slug):
    """ Renders a detail view for the Climb, matching slug. """
    climb = Climb.query.filter_by(slug=slug).first_or_404()
    segment = strava.get_segment(climb.strava_id)
    return render_template('frontend/climbs/climb_detail.html', climb=climb, segment=segment)
