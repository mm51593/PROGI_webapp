from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class UpdateForm(FlaskForm):
    Ime = StringField('Ime')
    Private_Ime = BooleanField('Privatno')
    Prezime = StringField('Prezime')
    Private_Prezime = BooleanField('Privatno')
    Datum_rodenja = DateField("Datum rodenja")
    Private_Datum = BooleanField('Privatno')
    Zivotopis = StringField('Zivotopis')
    Private_Zivotopis = BooleanField('Privatno')
    submit = SubmitField('Spremi promjene')
