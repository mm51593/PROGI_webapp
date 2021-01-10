from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length


class CheckoutForm(FlaskForm):
    Ime_Prezime = StringField('Ime i prezime', validators=[Length(min=6, max=40, message="Ime i prezime moraju biti između %(min)d i %(max)d znakova dugi.")])
    Prezime = StringField('Prezime', validators=[Length(min=3, max=25, message="Prezime mora biti između %(min)d i %(max)d znakova dugo.")])
    Private_Prezime = BooleanField('Privatno')
    Datum_rodenja = DateField("Datum rodenja")
    Private_Datum = BooleanField('Privatno')
    Zivotopis = StringField('Zivotopis', validators=[Length(min=1, max=400, message="Zivotopis mora biti između %(min)d i %(max)d znakova dugo.")])
    Private_Zivotopis = BooleanField('Privatno')
    submit = SubmitField('Spremi promjene')