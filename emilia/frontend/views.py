from flask import Blueprint, render_template

from emilia.climbs.models import Book


frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    """ Render full list of Books. """
    books = Book.query.all()
    return render_template('frontend/index.html', books=books)


@frontend.route('/book/<slug>')
def book_detail(slug):
    """ Render detail view for a Book. """
    book = Book.query.filter_by(slug=slug).first()
    return book.long_name
