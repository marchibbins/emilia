from emilia.climbs.models import Book, Climb
from emilia.extensions import db


def install():
    """ Adds Book and Climb data to database. """
    books = [
        ('100 Greatest Cycling Climbs',),
        ('Another 100 Greatest Cycling Climbs',),
    ]

    for data in books:
        book = Book(*data)
        db.session.add(book)

    climbs = [
        (1, 'Cheddar Gorge', 'Cheddar, Somerset', 1),
        (2, 'Weston Hill', 'Weston, Bath', 1),
        (3, 'Crowcombe Combe', 'Crowcombe, Somerset', 1),
    ]

    for data in climbs:
        climb = Climb(*data)
        db.session.add(climb)
