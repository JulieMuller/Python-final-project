# Create a new file as forms.py
from flask_wtf import FlaskForm
import pandas as pd
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField, FloatField
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


class withdrawcurrent(FlaskForm):
  amount_current = FloatField('Amount')
  withdraw_current = SubmitField('Withdraw')

class depositcurrent(FlaskForm):
  deposit_current = SubmitField('Deposit')


class withdrawsavings(FlaskForm):
  amount_savings = FloatField('Amount')
  withdraw_current = SubmitField('Withdraw')

class depositsavings(FlaskForm):
  deposit_savings = SubmitField('Deposit')