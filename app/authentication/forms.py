from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.database import User


class RegistrationForm(FlaskForm):
    username = StringField('Korisničko ime', validators=[DataRequired("Ovo polje je neophodno."), Length(min=3, max=25, message="Korisničko ime mora biti između %(min)d i %(max)d znakova dugo.")])
    email = StringField('Email', validators=[DataRequired("Ovo polje je neophodno."), Email(message="Pogrešan format E-mail adrese.")])
    password = PasswordField('Lozinka', validators=[DataRequired("Ovo polje je neophodno."), Length(min=8, message="Lozinka mora biti barem %(min)d znakova duga.")])
    confirm_password = PasswordField('Potvrdi lozinku', validators=[DataRequired("Ovo polje je neophodno."), EqualTo('password', message="Lozinke se ne podudaraju.")])
    submit = SubmitField('Registriraj me')

    def validate_username(self, username):
        fromdb = User.query.filter_by(username=username.data).first()
        if fromdb:
            raise ValidationError('Ovo korisničko ime je zauzeto.')
        return

    def validate_email(self, email):
        fromdb = User.query.filter_by(email=email.data).first()
        if fromdb:
            raise ValidationError('Račun s ovom email adresom već postoji.')
        return


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Ovo polje je neophodno."), Email("Pogrešan format E-mail adrese.")])
    password = PasswordField('Lozinka', validators=[DataRequired("Ovo polje je neophodno.")])
    remember = BooleanField('Zapamti me')
    submit = SubmitField('Prijava')

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

    