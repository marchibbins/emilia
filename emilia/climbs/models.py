from sqlalchemy import Column

from emilia.extensions import db


class Book(db.Model):

    """ Represents a single Book object. """

    SLUG_STR_MAX = 32
    NAME_STR_MAX = 128

    id = Column(db.Integer, primary_key=True)
    slug = Column(db.String(SLUG_STR_MAX), unique=True, nullable=False)
    short_name = Column(db.String(NAME_STR_MAX), nullable=False)
    long_name = Column(db.String(NAME_STR_MAX), nullable=False)

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
    LOCATION_STR_MAX = 64

    id = Column(db.Integer, primary_key=True)
    slug = Column(db.String(SLUG_STR_MAX), unique=True, nullable=False)
    number = Column(db.Integer, nullable=False)
    name = Column(db.String(NAME_STR_MAX), nullable=False)
    location = Column(db.String(LOCATION_STR_MAX), nullable=False)
    strava_id = Column(db.Integer, nullable=False)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book', backref=db.backref('climbs', lazy='dynamic'))

    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    region = db.relationship('Region', backref=db.backref('climbs', lazy='dynamic'))

    def serialize(self):
        """ Returns the object as an easily serializeable object. """
        return {
            'id': self.id,
            'slug': self.slug,
            'number': self.number,
            'name': self.name,
            'location': self.location,
            'strava_id': self.strava_id,
            'book_id': self.book_id,
            'region_id': self.region_id,
        }

    def __init__(self, slug, number, name, location, strava_id, book=None, region=None):
        """ Populates model properties. """
        self.slug = slug
        self.number = number
        self.name = name
        self.location = location
        self.strava_id = strava_id
        self.book = book
        self.region = region

    def __repr__(self):
        """ Returns the Climb object representation. """
        return '<Climb %r>' % self.name

    def __unicode__(self):
        """ Returns a string representation of the Climb object. """
        return '%s' % self.name


class Region(db.Model):

    """ Represents a single Region object. """

    SLUG_STR_MAX = 32
    NAME_STR_MAX = 64

    id = Column(db.Integer, primary_key=True)
    slug = Column(db.String(SLUG_STR_MAX), unique=True, nullable=False)
    name = Column(db.String(NAME_STR_MAX), nullable=False)

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
