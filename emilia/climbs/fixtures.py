from emilia.climbs.models import Climb
from emilia.extensions import db


def install():
    """ Adds Climb data to database. """
    climbs = [
        (1, 'Cheddar Gorge', 'Cheddar, Somerset'),
        (2, 'Weston Hill', 'Weston, Bath'),
        (3, 'Crowcombe Combe', 'Crowcombe, Somerset'),
    ]

    for data in climbs:
        climb = Climb(*data)
        db.session.add(climb)
