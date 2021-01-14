from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class CheckoutForm(FlaskForm):
    fname = StringField('Ime i prezime', validators=[DataRequired("Ovo polje je neophodno."), Length(min=6, max=40, message="Ime i prezime moraju biti između %(min)d i %(max)d znakova dugi.")])
    email = StringField('Email', validators=[DataRequired("Ovo polje je neophodno."), Length(min=15, max=50, message="Email mora biti između %(min)d i %(max)d znakova dug.")])
    adr = StringField('Adresa', validators=[DataRequired("Ovo polje je neophodno."), Length(min=5, max=50, message="Adresa mora biti između %(min)d i %(max)d znakova duga.")])
    city = StringField('Grad', validators=[DataRequired("Ovo polje je neophodno."), Length(min=3, max=20, message="Grad mora biti između %(min)d i %(max)d znakova dug.")])
    cname = StringField('Ime na kartici', validators=[DataRequired("Ovo polje je neophodno."), Length(min=6, max=40, message="Ime na kartici mora biti između %(min)d i %(max)d znakova dugo.")])
    ccnum = StringField('Broj na kartici', validators=[DataRequired("Ovo polje je neophodno."), Length(min=18, max=20, message="Broj na kartici mora biti između %(min)d i %(max)d znakova dugo.")])
    expdate = StringField('Datum isteka', validators=[DataRequired("Ovo polje je neophodno."), Length(min=4, max=5, message="Datum isteka mora biti između %(min)d i %(max)d znakova dug.")])
    state = StringField('Država', validators=[DataRequired("Ovo polje je neophodno."), Length(min=3, max=20, message="Drava mora biti između %(min)d i %(max)d znakova duga.")])
    zip = StringField('Poštanski broj', validators=[DataRequired("Ovo polje je neophodno."), Length(min=3, max=20, message="Postanski Broj mora biti između %(min)d i %(max)d znakova dug.")])
    cvv = StringField('CVV', validators=[DataRequired("Ovo polje je neophodno."), Length(min=3, max=4, message="CVV mora biti između %(min)d i %(max)d znakova dug.")])
    remember = BooleanField('Zapamti podatke')
    submit = SubmitField('Završi s kupnjom')