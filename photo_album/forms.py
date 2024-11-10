from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class PhotoForm(FlaskForm):
    id = HiddenField()  # Agregar campo oculto para el ID de la foto
    title = StringField('Título', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    image = StringField('URL de la imagen', validators=[DataRequired()])
    submit = SubmitField('Agregar Foto')
