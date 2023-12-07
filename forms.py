# Create a new file as forms.py
from flask_wtf import FlaskForm
import pandas as pd
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
  first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
  last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
  mail = EmailField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')


class LoginForm_client(FlaskForm):
  first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
  last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
  account_number = StringField('Account Number', validators=[DataRequired(), Length(min=2, max=20)])
  password = PasswordField('Pin', validators=[DataRequired()])
  remember = BooleanField('Remember Me') #a programmer
  submit = SubmitField('Login')

class LoginForm_employee(FlaskForm):
  pin = PasswordField('Pin', validators=[DataRequired()])
  submit = SubmitField('Login')

class UserRegistrationHandler:
  

    @classmethod
    def add_user(cls, first_name, last_name, mail, password, confirm_password, df):
        if(password == confirm_password): 
           new_user = df([[first_name, last_name, mail, password]], columns=['first_name', 'last_name', 'mail', 'password'])
        df = df.append(new_user, ignore_index=True)