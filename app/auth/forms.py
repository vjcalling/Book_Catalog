from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField




class RegistrationForm(FlaskForm):
    name = StringField('Name')
    email = StringField('E-mail')
    password = PasswordField('Password')
    confirm = PasswordField('Confirm')
    submit = SubmitField('Register')

