from flask import Flask, redirect, url_for, render_template, request, flash
import sys
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

app = Flask(__name__)

users = {'user1': 'password1', 'user2': 'password2'}

"""
def hello():
    return open('C:/Users/Mulle/Desktop/Python-Dorset/Flask_Blog/test.txt').read()

"""
@app.route("/") #routing page to directory
#whatever written under will be saved in the directory above

def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])



class RegistrationForm(FlaskForm): 
    username = StringField('Username',validators=[DataRequired(), Length (min=2, max=20)]) 
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Successful login
        print("username : %s | mdp : %s" %(username, password), file=sys.stderr)
        return render_template('welcomepage.html')
    else:
        # Failed login
        print("username : %s | mdp : %s" %(username, password), file=sys.stderr)
        app.logger.info('testing info log')
        return 'Invalid username or password. Please try again.'


if __name__ == '__main__':
    app.run(debug=True)