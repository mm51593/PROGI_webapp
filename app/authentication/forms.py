from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
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
    password = PasswordField('Lozinka', validators=[DataRequired("Ovo polje je neophodno."), Length(min=8, message="Lozinka mora biti barem %(min)d znakova duga.")])
    remember = BooleanField('Zapamti me')
    submit = SubmitField('Prijava')
