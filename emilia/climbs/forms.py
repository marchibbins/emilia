from flask.ext.wtf import Form
from wtforms import FloatField, IntegerField, TextField
from wtforms.validators import DataRequired, Length, NumberRange

from emilia.climbs.models import Climb


class ClimbForm(Form):

    """ Primary Climb create and edit form. """

    slug = TextField(u'Slug', [DataRequired(), Length(max=Climb.SLUG_STR_MAX)], description=u'Url-safe identifier, for example: "zig-zag-hill"')
    number = IntegerField(u'Climb number', [DataRequired(), NumberRange(min=1)], description=u'For example: "101"')
    name = TextField(u'Climb name', [DataRequired(), Length(max=Climb.NAME_STR_MAX)], description=u'For example: "Leith Hill"')
    location = TextField(u'Full location', [DataRequired(), Length(max=Climb.LENGTH_STR_MAX)], description=u'For example: "Cheddar, Somerset"')
    latitude = FloatField(u'Latitude', [DataRequired()])
    longitude = FloatField(u'Latitude', [DataRequired()])
    strava_id = IntegerField(u'Strava segment id', [DataRequired()], description='For example: "944629"')
