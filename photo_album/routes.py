from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import Photo
from forms import PhotoForm

@app.route('/')
def index():
    photos = Photo.query.all()  # Obtener todas las fotos de la base de datos
    return render_template('index.html', photos=photos)

@app.route('/add', methods=['GET', 'POST'])
def add_photo():
    form = PhotoForm()
    if form.validate_on_submit():  # Verificar si el formulario es válido
        title = form.title.data
        description = form.description.data
        image = form.image.data
        new_photo = Photo(title=title, description=description, image=image)
        db.session.add(new_photo)
        db.session.commit()
        flash('Foto añadida exitosamente!')
        return redirect(url_for('index'))
    return render_template('photo_form.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_photo(id):
    photo = Photo.query.get_or_404(id)  # Obtener la foto existente o devolver un error 404
    form = PhotoForm(obj=photo)  # Prellenar el formulario con los datos de la foto

    if form.validate_on_submit():  # Verificar si el formulario es válido
        photo.title = form.title.data
        photo.description = form.description.data
        photo.image = form.image.data
        db.session.commit()  # Guardar los cambios en la base de datos
        flash('Foto actualizada exitosamente!')
        return redirect(url_for('index'))

    return render_template('photo_form.html', form=form)

@app.route('/delete/<int:id>')
def delete_photo(id):
    photo = Photo.query.get(id)
    if photo:
        db.session.delete(photo)
        db.session.commit()
        flash('Foto eliminada exitosamente!')
    else:
        flash('Foto no encontrada.')
    return redirect(url_for('index'))

