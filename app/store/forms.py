from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, DecimalField
from wtforms.validators import DataRequired, InputRequired, NumberRange
from app.database import User, Model, ModelPhoto, ModelPrice


class ModelForm(FlaskForm):
    name = StringField('Naziv', validators=[DataRequired()])
    description = TextAreaField('Opis', validators=[DataRequired()])
    image = FileField('Slika ili nacrt',validators=[FileRequired()])
    dimension_1 = DecimalField('Dimenzija 1', validators=[DataRequired(), NumberRange(min=1)])
    dimension_2 = DecimalField('Dimenzija 2', validators=[DataRequired(), NumberRange(min=1)])
    dimension_3 = DecimalField('Dimenzija 3', validators=[DataRequired(), NumberRange(min=1)])
    colors = StringField('Boje', validators=[DataRequired()])
    submit = SubmitField('Naruči')

#form za stvaranje ponude
class ModelPriceForm(FlaskForm):
    material = StringField('Materijal', validators=[DataRequired()])
    price = DecimalField('Cijena', validators=[DataRequired(), NumberRange(min=1)])
    pr_submit = SubmitField('Spremi')

class MaterialForm(FlaskForm):
    material_input = SelectField('Materijal', choices=["Aluminij", "Zeljezo", "Drvo"], validators=[InputRequired()])
    m_submit = SubmitField('Primijeni')


