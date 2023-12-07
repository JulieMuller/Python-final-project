from flask import Flask, render_template, url_for, request, redirect, flash
import sys
import pandas as pd
from forms import RegistrationForm, LoginForm_client, LoginForm_employee, UserRegistrationHandler
app = Flask(__name__)

app.config['SECRET_KEY'] = '9c383dc88513191312f9fa9317ce3100'

users ={
    'first_name': ['Sherlock', 'manon', 'test'],
    'last_name': ['Holmes', 'merel', 'test'],
    'mail': ['email@email.com', 'email@email.com', 'test@'],
    'password': ['toto23', 'toto23', 'test'],
    'account_number': ["11", '11', "11"] }
users_df = pd.DataFrame(users)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = 'Welcome')

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST':
        UserRegistrationHandler.add_user(form.first_name.data, form.last_name.data, form.mail.data, form.password.data, users_df)
        print("first : %s | last : %s | mdp : %s" %(form.first_name.data, form.last_name.data, form.password.data), file=sys.stderr)    
        return redirect(url_for('/login_client'))
    else:
        print("nope")
    
    return render_template('register.html', title = 'Register', form=form)

@app.route("/login_client", methods=['GET', 'POST'])
def login_client():
    forms = LoginForm_client()

    if request.method == 'POST':
        ac_number = request.form.get('account_number') 
        password = request.form.get('password') 

        print('password %s - account number %s'%(users_df.iloc['account_number' == ac_number]['password'], request.form.get('password') ))

        if ac_number in users_df and users_df.iloc['account_number' == ac_number]['password'] == password:
            flash('Registration successful. Please log in.')
            return redirect(url_for('/accounts'))
        else:
            return redirect(url_for('home'))
    else:
        print(forms.validate()) 
        print(forms.errors)
        print("nope")

        
        
    return render_template('login_client.html', title = 'Login client', form=forms)

@app.route("/login_employee", methods=['GET', 'POST'])
def login_employee():
    forms = LoginForm_employee()
    return render_template('login_employee.html', title = 'Login employee', form=forms)


@app.route("/account", methods=['GET', 'POST'])
def accounts():
    return render_template('account.html', title = 'Accounts')

if __name__ == '__main__':
  app.run(debug=True)