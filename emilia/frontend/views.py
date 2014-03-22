from flask import Blueprint, render_template

from emilia.climbs.models import Book


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
    book = Book.query.filter_by(slug=slug).first()
    return render_template('frontend/climbs/book_detail.html', book=book)
