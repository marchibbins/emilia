from flask.ext.wtf import Form
from wtforms import FloatField, IntegerField, TextField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

from emilia.climbs.models import Book, Climb, Region


class UniqueValidator(object):

    """ Validates uniqueness of field on model. """

    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'%s with this %s already exists.' % (model.__name__, field.name)
        self.message = message

    def __call__(self, form, field):
        if self.model.query.filter(self.field == field.data).count() > 0:
            raise ValidationError(self.message)


def lowercase_filter(data):
    """ Converts string data to lowercase. """
    if data:
        return data.lower()
    else:
        return data


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
    location = TextField(u'Full location', [DataRequired(), Length(max=Climb.LENGTH_STR_MAX)], description=u'For example: "Cheddar, Somerset"')
    latitude = FloatField(u'Latitude', [DataRequired()])
    longitude = FloatField(u'Latitude', [DataRequired()])
    strava_id = IntegerField(u'Strava segment id', [DataRequired()], description='For example: "944629"')

    book = QuerySelectField(query_factory=lambda:Book.query.all())
    region = QuerySelectField(query_factory=lambda:Region.query.all())


class RegionForm(Form):

    """ Primary Region create and edit form. """

    slug = TextField(u'Slug', [DataRequired(), UniqueValidator(Region, Region.slug), Length(max=Region.SLUG_STR_MAX)], filters=[lowercase_filter], description=u'Url-safe identifier, for example: "south-west"')
    name = TextField(u'Name', [DataRequired(), Length(max=Region.NAME_STR_MAX)], description=u'For example: "South-west"')
