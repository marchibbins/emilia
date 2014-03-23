from sqlalchemy import Column

from emilia.extensions import db


class Book(db.Model):

    """ Represents a single Book object. """

    SLUG_STR_MAX = 32
    NAME_STR_MAX = 64

    id = Column(db.Integer, primary_key=True)
    slug = Column(db.String(SLUG_STR_MAX), unique=True)
    short_name = Column(db.String(NAME_STR_MAX))
    long_name = Column(db.String(NAME_STR_MAX))

    def serialize(self):
        """ Returns the object as an easily serializeable object. """
        return {
            'id': self.id,
            'slug': self.slug,
            'short_name': self.short_name,
            'long_name': self.long_name,
        }

    def __init__(self, slug, short_name, long_name):
        """ Populates model properties. """
        self.slug = slug
        self.short_name = short_name
        self.long_name = long_name

    def __repr__(self):
        """ Returns the Book object representation. """
        return '<Book %r>' % self.short_name

    def __unicode__(self):
        """ Returns a string representation of the Climb object. """
        return '%s' % self.short_name


class Climb(db.Model):

    """ Represents a single Climb object. """

    SLUG_STR_MAX = 32
    NAME_STR_MAX = 64
    LENGTH_STR_MAX = 64

    id = Column(db.Integer, primary_key=True)
    slug = Column(db.String(SLUG_STR_MAX), unique=True)
    number = Column(db.Integer)
    name = Column(db.String(NAME_STR_MAX))
    location = Column(db.String(LENGTH_STR_MAX))
    latitude = Column(db.Float)
    longitude = Column(db.Float)
    strava_id = Column(db.Integer)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book', backref=db.backref('climbs', lazy='dynamic'))

    def serialize(self):
        """ Returns the object as an easily serializeable object. """
        return {
            'id': self.id,
            'slug': self.slug,
            'number': self.number,
            'name': self.name,
            'location': self.location,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'strava_id': self.strava_id,
            'book_id': self.book_id,
        }

    def __init__(self, number, slug, name, location, latitude, longitude, strava_id, book):
        """ Populates model properties. """
        self.slug = slug
        self.number = number
        self.name = name
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
        self.strava_id = strava_id
        self.book = book

    def __repr__(self):
        """ Returns the Climb object representation. """
        return '<Climb %r>' % self.name

    def __unicode__(self):
        """ Returns a string representation of the Climb object. """
        return '%s. %s' % (self.number, self.name)


class Region(db.Model):

    """ Represents a single Region object. """

    SLUG_STR_MAX = 32
    NAME_STR_MAX = 64

    id = Column(db.Integer, primary_key=True)
    slug = Column(db.String(SLUG_STR_MAX), unique=True)
    name = Column(db.String(NAME_STR_MAX))

    def serialize(self):
        """ Returns the object as an easily serializeable object. """
        return {
            'id': self.id,
            'slug': self.slug,
            'name': self.name,
        }

    def __init__(self, slug, name):
        """ Populates model properties. """
        self.slug = slug
        self.name = name

    def __repr__(self):
        """ Returns the Region object representation. """
        return '<Region %r>' % self.name

    def __unicode__(self):
        """ Returns a string representation of the Region object. """
        return '%s' % self.name
