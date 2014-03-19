from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask.ext.login import login_required

from emilia.climbs.forms import ClimbForm
from emilia.climbs.models import Climb
from emilia.extensions import db


admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
@login_required
def index():
    """ Admin home, lists all Climbs. """
    climbs = Climb.query.all()
    return render_template('admin/index.html', climbs=climbs)


@admin.route('/climb/add', methods=['GET', 'POST'])
@login_required
def climb_add():
    """ Create a new Climb object. """
    form = ClimbForm()
    title = "Add climb"

    if form.validate_on_submit():
        climb = Climb(number=form.number.data, name=form.name.data, location=form.location.data)
        db.session.add(climb)
        db.session.commit()
        flash('Climb created.', 'success')
        return redirect(url_for('admin.index'))

    return render_template('admin/climbs/climb_add.html', form=form, title=title)


@admin.route('/climb/<int:climb_id>', methods=['GET', 'POST'])
@login_required
def climb_edit(climb_id):
    """ Edit a Climb object. """
    climb = Climb.query.filter_by(id=climb_id).first_or_404()
    form = ClimbForm(obj=climb)
    title = "Edit climb"

    if form.validate_on_submit():
        form.populate_obj(climb)
        db.session.add(climb)
        db.session.commit()
        flash('Climb updated.', 'success')

    return render_template('admin/climbs/climb_edit.html', climb=climb, form=form, title=title)


@admin.route('/climb/<int:climb_id>/delete', methods=['GET', 'POST'])
@login_required
def climb_delete(climb_id):
    """ Delete a climb object (on POST, confirm on GET). """
    climb = Climb.query.filter_by(id=climb_id).first_or_404()

    if request.method == 'POST':
        db.session.delete(climb)
        db.session.commit()
        flash('Climb deleted.', 'success')
        return redirect(url_for('admin.index'))

    return render_template('admin/climbs/climb_delete.html', climb=climb)
