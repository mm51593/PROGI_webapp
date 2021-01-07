from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, NumberRange
from app.database import User, Model, ModelPhoto, ModelPrice


class ModelForm(FlaskForm):
    name = StringField('Naziv', validators=[DataRequired()])
    description = TextAreaField('Opis', validators=[DataRequired()])
    #image_name = 
    #video_name = 
    
    submit = SubmitField('Objavi')

#form za stvaranje ponude
class ModelPriceForm(FlaskForm):
    material = StringField('Materijal', validators=[DataRequired()])
    price = IntegerField('Cijena', validators=[DataRequired(), NumberRange(min=1)])
    pr_submit = SubmitField('Spremi')

class MaterialForm(FlaskForm):
    material_input = SelectField('Materijal', choices=["Aluminij", "Zeljezo", "Drvo"], validators=[InputRequired()])
    m_submit = SubmitField('Primijeni')


