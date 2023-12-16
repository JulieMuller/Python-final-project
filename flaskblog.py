from flask import Flask, render_template, url_for, request, redirect, flash
from User import User
import sys
import pandas as pd
from forms import RegistrationForm, LoginForm_client, LoginForm_employee, depositsavings, withdrawcurrent, withdrawsavings, depositcurrent
app = Flask(__name__)

app.config['SECRET_KEY'] = '9c383dc88513191312f9fa9317ce3100'

active_user_index = 0
#active_user = User('-1', '-1', "-1", '-1', '-1', 0.0, 0.0)

'''
users ={
    'first_name': ['Sherlock', 'manon', 'test'],
    'last_name': ['Holmes', 'merel', 'test'],
    'account_number': ["12", '13', "14"],
    'password': ['toto23', 'toto23', 'test'],
    'mail': ['email@email.com', 'email@email.com', 'test@']
    }
users_df = pd.DataFrame(users)


users_list =[User('test', 'test', "test@", '11', 'test'), 
             User('Fanny', 'Coursier', "fc@email.com", '11', 'jaimeLesVieux')]'''

#import users from file
users_list = User.load_users_from_file()

#verify if users load correctly in console
for users in users_list:
    print("nb de users:%s" %len(users_list))
    users.display_info()

@app.route("/")

# HOME PAGE
@app.route("/home")
def home():
    return render_template('home.html', title = 'Welcome')

# REGISTER PAGE
@app.route("/register", methods=['GET', 'POST'])
def register():
    register = RegistrationForm()

    if request.method == 'POST':

        first_name = register.first_name.data
        last_name = register.last_name.data
        mail = register.mail.data
        password = register.password.data    
        new_user = User(first_name, last_name, mail, "17", password)

        if new_user.already_exist(users_list) == False:
            print("first : %s | last : %s | mdp : %s" %(register.first_name.data, register.last_name.data, register.password.data), file=sys.stderr)    
            #users_list.append(new_user)
            new_user.user_update(users_list)
            return redirect(url_for('login_client'))        
        else:
            print("nope")
    
    return render_template('register.html', title = 'Register', form=register)

# CLIENT LOGIN PAGE
@app.route("/login_client", methods=['POST', 'GET'])
def login_client():
    login = LoginForm_client()

    if request.method == 'POST':

        ac_number = request.form.get('account_number')
        first_name = login.first_name.data
        last_name = login.last_name.data
        password = login.password.data
        temp_user = User(first_name, last_name, "mail", ac_number, password)

        if  temp_user.login_form_validation(users_list)[0]:
            flash('Login successful.')
            active_user_index = temp_user.login_form_validation(users_list)[1]
            users_list[active_user_index].Copy(users_list[active_user_index])
            return redirect(url_for('accounts'))

        else:
            flash('log in failed.')
            return redirect(url_for('home'))
    else:
        print(login.validate()) 
        print(login.errors)    
        
    return render_template('login_client.html', title = 'Login client', form=login)

# EMPLOYEE LOGIN PAGE
@app.route("/login_employee", methods=['GET', 'POST'])
def login_employee():
    login = LoginForm_employee()
    return render_template('login_employee.html', title = 'Login employee', form=login)

# ACCOUNT PAGE
@app.route("/account", methods=['GET', 'POST'])
def accounts():

    # Get the current and savings amounts in the active user 
    current = users_list[active_user_index].current_account
    savings = users_list[active_user_index].savings_account

    # Creates a deposit and withdraw button and an integerfield
    deposit_current = depositcurrent()
    withdraw_current = withdrawcurrent()
    deposit_savings = depositsavings()
    withdraw_savings = withdrawsavings()

    if request.method == 'POST':

        # manages the different button actions on the page
        if  deposit_current.is_submitted() and isinstance(withdraw_current.amount_current.data, float) :
            users_list[active_user_index].deposit("current", withdraw_current.amount_current.data)
            return redirect(url_for('accounts'))
        if  withdraw_current.is_submitted() and isinstance(withdraw_current.amount_current.data, float):
            users_list[active_user_index].withdraw("current", withdraw_current.amount_current.data)
            return redirect(url_for('accounts'))
        
        if  deposit_savings.is_submitted() and isinstance(withdraw_savings.amount_savings.data, float):
            users_list[active_user_index].deposit("savings", withdraw_savings.amount_savings.data)
            return redirect(url_for('accounts'))
        if  withdraw_savings.is_submitted() and isinstance(withdraw_savings.amount_savings.data, float):
            users_list[active_user_index].withdraw("savings", withdraw_savings.amount_savings.data)
            return redirect(url_for('accounts'))
        else:
            flash('deposit/withdraw failed.')
            return redirect(url_for('accounts'))
        
    else:
        print('form error') 
    
    print("saving")
    users_list[active_user_index].user_update(users_list)
    return render_template('account.html', title = 'Accounts', 
                           current = users_list[active_user_index].current_account, 
                           savings = users_list[active_user_index].savings_account,
                           deposit_current = deposit_current,
                           withdraw_current = withdraw_current,
                           deposit_savings  = deposit_savings,
                           withdraw_savings = withdraw_savings)

if __name__ == '__main__':
  app.run(debug=True)