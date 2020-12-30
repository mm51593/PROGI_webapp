from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from app.database import User, Model, ModelPhoto, ModelPrice


class ModelForm(FlaskForm):
    name = StringField('Naziv', validators=[DataRequired()])
    description = TextAreaField('Opis', validators=[DataRequired()])
    #image_name = 
    #video_name = 
    
    submit = SubmitField('Objavi')

class MaterialForm(FlaskForm):
    material = SelectField('Materijal', choices=[(1, "Aluminij"), (2, "Zeljezo"), (3, "Drvo")], validators=[InputRequired()])



