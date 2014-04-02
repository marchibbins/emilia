from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask.ext.login import login_required

from emilia.climbs.forms import BookForm, ClimbForm, RegionForm
from emilia.climbs.models import Book, Climb, Region
from emilia.extensions import db


admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
@login_required
def index():
    """ Admin home, lists all Books and Climbs. """
    books = Book.query.all()
    climbs = Climb.query.all()
    regions = Region.query.all()
    return render_template('admin/index.html', books=books, climbs=climbs, regions=regions)


@admin.route('/book/add', methods=['GET', 'POST'])
@login_required
def book_add():
    """ Creates a new Book object. """
    return model_add_view(Book, BookForm)


@admin.route('/book/<int:id>', methods=['GET', 'POST'])
@login_required
def book_edit(id):
    """ Edits a Book object. """
    return model_edit_view(Book, BookForm, id)


@admin.route('/book/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def book_delete(id):
    """ Deletes a Book object (on POST, confirm on GET). """
    return model_delete_view(Book, id)


@admin.route('/climb/add', methods=['GET', 'POST'])
@login_required
def climb_add():
    """ Creates a new Climb object. """
    return model_add_view(Climb, ClimbForm)


@admin.route('/climb/<int:id>', methods=['GET', 'POST'])
@login_required
def climb_edit(id):
    """ Edits a Climb object. """
    return model_edit_view(Climb, ClimbForm, id)


@admin.route('/climb/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def climb_delete(id):
    """ Deletes a Climb object (on POST, confirm on GET). """
    return model_delete_view(Climb, id)


@admin.route('/region/add', methods=['GET', 'POST'])
@login_required
def region_add():
    """ Creates a new Region object. """
    return model_add_view(Region, RegionForm)


@admin.route('/region/<int:id>', methods=['GET', 'POST'])
@login_required
def region_edit(id):
    """ Edits a Region object. """
    return model_edit_view(Region, RegionForm, id)


@admin.route('/region/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def region_delete(id):
    """ Deletes a Region object (on POST, confirm on GET). """
    return model_delete_view(Region, id)


def model_add_view(model, form):
    """ Renders a generic form-based model create view. """
    name = model.__name__
    form = form()

    if form.validate_on_submit():
        data = dict((k, v) for k, v in form.data.iteritems() if v)
        obj = model(**data)
        db.session.add(obj)
        db.session.commit()
        flash('%s created.' % name, 'success')
        return redirect(url_for('admin.index'))

    return render_template('admin/model/add.html', name=name, form=form)


def model_edit_view(model, form, id):
    """ Renders a generic form-based model edit view. """
    name = model.__name__
    obj = model.query.get_or_404(id)
    form = form(obj=obj)

    if form.validate_on_submit():
        form.populate_obj(obj)
        db.session.add(obj)
        db.session.commit()
        flash('%s updated.' % name, 'success')
        return redirect(url_for('admin.index'))

    return render_template('admin/model/edit.html', name=name, form=form)


def model_delete_view(model, id):
    """ Renders a generic form-based model delete view. """
    name = model.__name__
    obj = model.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(obj)
        db.session.commit()
        flash('%s deleted.' % name, 'success')
        return redirect(url_for('admin.index'))

    return render_template('admin/model/delete.html', name=name, obj=obj)
