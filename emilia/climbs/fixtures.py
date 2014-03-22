from emilia.climbs.models import Book, Climb
from emilia.extensions import db


def install():
    """ Adds Book and Climb data to database. """
    fixtures = [
        {
            'book': ("greatest",
                     "100 Greatest Cycling Climbs",
                     "100 Greatest Cycling Climbs: A Road Cyclist's Guide to Britain's Hills"),
            'climbs': [
                (1, "cheddar-gorge", "Cheddar Gorge", "Cheddar, Somerset"),
                (2, "weston-hill", "Weston Hill", "Weston, Bath"),
                (3, "crowcombe-combe", "Crowcombe Combe", "Crowcombe, Somerset"),
            ]
        },
        {
            'book': ("another",
                     "Another 100 Greatest Cycling Climbs",
                     "Another 100 Greatest Cycling Climbs: A Road Cyclist's Guide to Britain's Hills"),
            'climbs': [
                (101, "gold-hill", "Gold Hill", "Shaftesbury, Dorset"),
                (102, "zig-zag-hill", "Zig Zag Hill", "Shaftesbury, Dorset"),
                (103, "park-hill", "Park Hill", "Longleat, Dorset"),
            ]
        },
    ]

    for obj in fixtures:
        book = Book(*obj['book'])
        db.session.add(book)

        for climb in obj['climbs']:
            climb = Climb(*climb, book=book)
            db.session.add(climb)

    db.session.commit()
