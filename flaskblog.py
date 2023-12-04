from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
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

@app.route("/index", methods=['GET', 'POST'])
def index():
    forms = RegistrationForm()
    return render_template('login2.html', title = 'index', form=forms)

@app.route("/login", methods=['GET', 'POST'])
def login():
    forms = LoginForm()
    return render_template('login.html', title = 'Login', form=forms)

if __name__ == '__main__':
  app.run(debug=True)