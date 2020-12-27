from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class UpdateForm(FlaskForm):
    Ime = StringField('Ime', validators=[DataRequired("Ovo polje je neophodno."), Length(min=3, max=25, message="Ime mora biti između %(min)d i %(max)d znakova dugo.")])
    Private_Ime = BooleanField('Privatno')
    Prezime = StringField('Prezime', validators=[DataRequired("Ovo polje je neophodno."), Length(min=3, max=25, message="Prezime mora biti između %(min)d i %(max)d znakova dugo.")])
    Private_Prezime = BooleanField('Privatno')
    Datum_rodenja = DateField("Datum rodenja", validators=[DataRequired("Datum rodenja mora biti oznacen")], format='%d/%m/%Y')
    Private_Datum = BooleanField('Privatno')
    Zivotopis = StringField('Zivotopis', validators=[DataRequired("Ovo polje je neophodno."), Length(min=1, max=400, message="Zivotopis mora biti između %(min)d i %(max)d znakova dugo.")])
    Private_Zivotopis = BooleanField('Privatno')
    submit = SubmitField('Spremi promjene')
