from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.database import User, Model, ModelPhoto, ModelPrice


class ModelForm(FlaskForm):
    name = StringField('Naziv', validators=[DataRequired()])
    description = TextAreaField('Opis', validators=[DataRequired()])
    # dodati model_image
    submit = SubmitField('Objavi')



