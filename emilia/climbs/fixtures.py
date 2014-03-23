from emilia.climbs.models import Book, Climb, Region
from emilia.extensions import db


def install():
    """ Adds Book, Climb and Region data to database. """
    fixtures = [
        {
            'book': ("greatest",
                     "100 Greatest Cycling Climbs",
                     "100 Greatest Cycling Climbs: A Road Cyclist's Guide to Britain's Hills"),
            'climbs': [
                (1, "cheddar-gorge", "Cheddar Gorge", "Cheddar, Somerset", 51.5072, -0.1275, 944629),
                (2, "weston-hill", "Weston Hill", "Weston, Bath", 51.5072, -0.1275, 944629),
                (3, "crowcombe-combe", "Crowcombe Combe", "Crowcombe, Somerset", 51.5072, -0.1275, 944629),
            ]
        },
        {
            'book': ("another",
                     "Another 100 Greatest Cycling Climbs",
                     "Another 100 Greatest Cycling Climbs: A Road Cyclist's Guide to Britain's Hills"),
            'climbs': [
                (101, "gold-hill", "Gold Hill", "Shaftesbury, Dorset", 51.5072, -0.1275, 944629),
                (102, "zig-zag-hill", "Zig Zag Hill", "Shaftesbury, Dorset", 51.5072, -0.1275, 944629),
                (103, "park-hill", "Park Hill", "Longleat, Dorset", 51.5072, -0.1275, 944629),
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

    fixtures = [
        {
            'region': ('south-west', 'South-west'),
            'climbs': [
                'cheddar-gorge',
                'weston-hill',
            ],
        },
        {
            'region': ('south-east', 'South-east'),
            'climbs': [
                'crowcombe-combe',
                'gold-hill',
            ],
        },
        {
            'region': ('midlands', 'Midlands'),
            'climbs': [
                'zig-zag-hill',
                'park-hill',
            ],
        },
    ]

    for obj in fixtures:
        region = Region(*obj['region'])
        db.session.add(region)

        for slug in obj['climbs']:
            climb = Climb.query.filter_by(slug=slug).first()
            climb.region = region
            db.session.add(climb)

    db.session.commit()
