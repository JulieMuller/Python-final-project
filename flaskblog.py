from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm_client, LoginForm_employee
app = Flask(__name__)

app.config['SECRET_KEY'] = '9c383dc88513191312f9fa9317ce3100'


posts = [
    {
        'author': 'Sherlock Holmes',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 20, 2023'
    },
    {
        'author': 'Dr. John Watson',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 21, 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', pos = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    forms = RegistrationForm()
    return render_template('register.html', title = 'Register', form=forms)

@app.route("/login_client", methods=['GET', 'POST'])
def login_client():
    forms = LoginForm_client()
    return render_template('login_client.html', title = 'Login client', form=forms)

@app.route("/login_employee", methods=['GET', 'POST'])
def login_employee():
    forms = LoginForm_employee()
    return render_template('login_employee.html', title = 'Login employee', form=forms)

if __name__ == '__main__':
  app.run(debug=True)