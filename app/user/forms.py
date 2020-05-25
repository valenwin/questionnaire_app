from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import validators
from wtforms.fields.html5 import EmailField


class RegisterForm(FlaskForm):
    class Meta:
        csrf = False

    name = StringField('Name',
                       validators=[validators.DataRequired(),
                                   validators.Length(min=2, max=80)])
    email = EmailField('Email',
                       validators=[validators.DataRequired(),
                                   validators.Email()])
    password = PasswordField('Password',
                             validators=[validators.DataRequired(),
                                         validators.EqualTo('confirm_password',
                                                            message='Password must match')])
    confirm_password = PasswordField('Confirm password',
                                     validators=[validators.DataRequired()])


class LoginForm(FlaskForm):
    class Meta:
        csrf = False

    email = EmailField('Email',
                       validators=[validators.DataRequired(),
                                   validators.Email()])
    password = PasswordField('Password',
                             validators=[validators.DataRequired()])
