from flask.ext.wtf import Form
from wtforms import FloatField, IntegerField, TextField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, NumberRange

from emilia.climbs.models import Book, Climb, Region
from emilia.utils import lowercase_filter, UniqueValidator


class BookForm(Form):

    """ Primary Book create and edit form. """

    slug = TextField(u'Slug', [DataRequired(), UniqueValidator(Book, Book.slug), Length(max=Book.SLUG_STR_MAX)], filters=[lowercase_filter], description=u'Url-safe identifier, for example: "100-climbs"')
    short_name = TextField(u'Short name', [DataRequired(), Length(max=Book.NAME_STR_MAX)], description=u'For example: "100 Climbs"')
    long_name = TextField(u'Long name', [DataRequired(), Length(max=Book.NAME_STR_MAX)], description=u'For example: "100 Greatest Cycling Climbs: A Road Cyclist\'s Guide to Britain\'s Hills"')


class ClimbForm(Form):

    """ Primary Climb create and edit form. """

    slug = TextField(u'Slug', [DataRequired(), UniqueValidator(Climb, Climb.slug), Length(max=Climb.SLUG_STR_MAX)], filters=[lowercase_filter], description=u'Url-safe identifier, for example: "zig-zag-hill"')
    number = IntegerField(u'Climb number', [DataRequired(), NumberRange(min=1)], description=u'For example: "101"')
    name = TextField(u'Climb name', [DataRequired(), Length(max=Climb.NAME_STR_MAX)], description=u'For example: "Leith Hill"')
    location = TextField(u'Full location', [DataRequired(), Length(max=Climb.LOCATION_STR_MAX)], description=u'For example: "Cheddar, Somerset"')
    latitude = FloatField(u'Latitude', [DataRequired()])
    longitude = FloatField(u'Latitude', [DataRequired()])
    strava_id = IntegerField(u'Strava segment id', [DataRequired()], description='For example: "944629"')

    book = QuerySelectField(query_factory=lambda:Book.query.all())
    region = QuerySelectField(query_factory=lambda:Region.query.all())


class RegionForm(Form):

    """ Primary Region create and edit form. """

    slug = TextField(u'Slug', [DataRequired(), UniqueValidator(Region, Region.slug), Length(max=Region.SLUG_STR_MAX)], filters=[lowercase_filter], description=u'Url-safe identifier, for example: "south-west"')
    name = TextField(u'Name', [DataRequired(), Length(max=Region.NAME_STR_MAX)], description=u'For example: "South-west"')
