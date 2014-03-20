from emilia.climbs.models import Book, Climb
from emilia.extensions import db


def install():
    """ Adds Book and Climb data to database. """
    fixtures = [
        {
            'book': ('100 Greatest Cycling Climbs',),
            'climbs': [
                (1, 'Cheddar Gorge', 'Cheddar, Somerset'),
                (2, 'Weston Hill', 'Weston, Bath'),
                (3, 'Crowcombe Combe', 'Crowcombe, Somerset'),
            ]
        },
        {
            'book': ('Another 100 Greatest Cycling Climbs',),
            'climbs': [
                (101, 'Gold Hill', 'Shaftesbury, Dorset'),
                (102, 'Zig Zag Hill', 'Shaftesbury, Dorset'),
                (103, 'Park Hill', 'Longleat, Dorset'),
            ]
        },
    ]

    for obj in fixtures:
        book = Book(*obj['book'])
        db.session.add(book)

        for climb in obj['climbs']:
            climb = Climb(*climb, book=book)
            db.session.add(climb)
