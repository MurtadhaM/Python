# Author: Group 15
# Date: 2020-11-24
# Group: 15 
# Assignment: Final Project
# 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField
from wtforms.validators import Length, Regexp, DataRequired, EqualTo, Email
from wtforms import ValidationError
from models import User
from database import db

# THIS FORM WILL BE USED TO CREATE A NEW USER 
class RegisterForm(FlaskForm):
    class Meta:
        # THIS SHIT IS CRAWLING AND USING IT BREAKS SQLMAP IN MY EXPERIENCE
        csrf = False
    # First Name Field
    firstname = StringField('First Name', validators=[Length(1, 10)])
    # Last Name Field
    lastname = StringField('Last Name', validators=[Length(1, 20)])
    # Email Field
    email = StringField('Email', [
        Email(message='Email format is not valid.'),
        DataRequired()])
    # Password Field
    password = PasswordField('Password', [
        DataRequired(message="Enter a password."),
        EqualTo('confirmPassword', message='Passwords invalid')
    ])
    # Confirm Password Field
    confirmPassword = PasswordField('Confirm Password', validators=[
        Length(min=6, max=15)
    ])
    # Submit Button
    submit = SubmitField('Submit')

    def validate_email(self, field):
        if db.session.query(User).filter_by(email=field.data).count() != 0:
            raise ValidationError('Username Exists.')

# THIS FORM WILL BE USED TO LOGIN A USER
class LoginForm(FlaskForm):
    class Meta:
        csrf = False
    # Email Field
    email = StringField('Email', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    # Password Field
    password = PasswordField('Password', [
        DataRequired(message="Please enter a password.")])
    # Submit Button
    submit = SubmitField('Log In')
    # function for checking if user exists
    def validate_email(self, field):
        if db.session.query(User).filter_by(email=field.data).count() == 0:
            raise ValidationError('Incorrect Credentials.')
