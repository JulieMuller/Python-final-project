# Create a new file as forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  mail = EmailField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')

class LoginForm_client(FlaskForm):
  first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
  last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
  account_number = StringField('Account Number', validators=[DataRequired(), Length(min=2, max=20)])
  pin = PasswordField('Pin', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')

class LoginForm_employee(FlaskForm):
  pin = PasswordField('Pin', validators=[DataRequired()])
  submit = SubmitField('Login')