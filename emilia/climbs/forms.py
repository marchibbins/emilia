from flask.ext.wtf import Form
from wtforms import IntegerField, TextField
from wtforms.validators import DataRequired, Length, NumberRange

from emilia.climbs.models import Climb


class ClimbForm(Form):

    """ Primary Climb create and edit form. """

    number = IntegerField(u'Climb number', [NumberRange(min=1)], description=u'For example: "101"')
    name = TextField(u'Climb name', [DataRequired(), Length(max=Climb.NAME_STR_MAX)], description=u'For example: "Leith Hill"')
    location = TextField(u'Full location', [DataRequired(), Length(max=Climb.LENGTH_STR_MAX)], description=u'For example: "Cheddar, Somerset"')
