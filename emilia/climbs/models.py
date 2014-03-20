from sqlalchemy import Column

from emilia.extensions import db


class Climb(db.Model):

    """ Represents a single Climb object. """

    NAME_STR_MAX = 64
    LENGTH_STR_MAX = 64

    id = Column(db.Integer, primary_key=True)
    number = Column(db.Integer)
    name = Column(db.String(NAME_STR_MAX))
    location = Column(db.String(LENGTH_STR_MAX))

    def serialize(self):
        """ Returns the object as an easily serializeable object. """
        return {
            'id': self.id,
            'number': self.number,
            'name': self.name,
            'location': self.location,
        }

    def __init__(self, number, name, location):
        """ Populates model properties. """
        self.number = number
        self.name = name
        self.location = location

    def __repr__(self):
        """ Returns the Climb object representation. """
        return '<Climb %r>' % self.name

    def __unicode__(self):
        """ Returns a string representation of the Climb object. """
        return '%s. %s' % (self.number, self.name)
