from flask import Blueprint, render_template

from emilia.climbs.models import Book, Climb


frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    """ Renders the Home page. """
    return render_template('frontend/index.html')


@frontend.route('/books')
def book_list():
    """ Renders a full list of Books. """
    books = Book.query.all()
    return render_template('frontend/climbs/book_list.html', books=books)


@frontend.route('/books/<slug>')
def book_detail(slug):
    """ Renders a detail view for the Book, matching slug. """
    book = Book.query.filter_by(slug=slug).first_or_404()
    return render_template('frontend/climbs/book_detail.html', book=book)


@frontend.route('/books/<book_slug>/<climb_number>')
def climb_detail(book_slug, climb_number):
    """ Renders a detail view for the Climb, matching book slug and climb number. """
    climb = Climb.query.join(Book).filter(Book.slug == book_slug, Climb.number == climb_number).first_or_404()
    return render_template('frontend/climbs/climb_detail.html', climb=climb)
