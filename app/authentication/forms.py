from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.database import User


class RegistrationForm(FlaskForm):
    username = StringField('Korisničko ime', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Lozinka', validators=[DataRequired()])
    confirmPassword = PasswordField('Potvrdi lozinku', validators=[DataRequired(), EqualTo(password)])
    submit = SubmitField('Registriraj me')

    def validate_username(self, username):
        fromdb = User.query.filter_by(username=username.data).first()
        if fromdb:
            raise ValidationError('Ovo korisničko ime je zauzeto')
        return

    def validate_email(self, email):
        fromdb = User.query.filter_by(email=email.data).first()
        if fromdb:
            raise ValidationError('Račun s ovom email adresom već postoji.')
        return


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Lozinka', validators=[DataRequired()])
    remember = BooleanField('Zapamti me')
    submit = SubmitField('Prijava')
