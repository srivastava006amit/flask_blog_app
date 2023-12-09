from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegisterForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
import os

#TEMPLATE_DIR = os.path.abspath('templates')
#STATIC_DIR = os.path.abspath('static')

app = Flask(__name__)
#app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

app.config['SECRET_KEY'] = 'd26eae7e94a894cd29be700b1b06acef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

posts=[{'author': 'amit',
        'title': 'Blog post 1',
        'content': 'hey this is post content',
        'post_date': 'May 01, 2023'},
       {'author': 'jerry',
        'title': 'Blog post 2',
        'content': 'hey this is post content 2',
        'post_date': 'May 02, 2023'},
       {'author': 'tom',
        'title': 'Blog post 3',
        'content': 'hey this is post content 2',
        'post_date': 'May 02, 2023'}
       ]

# Routes
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='home')

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print("submit pressed")
            flash(f"Account created for user {form.username.data}!" , "success")
            return redirect(url_for('home'))
        else:
            redirect(url_for('register'))
    print("submit not pressed")
    return render_template('register.html', form=form, title='Register')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print(form.email)
            print(form.password)
            if form.email.data == "admin@blog.com" and form.password.data == "password":
                print("Logged in ")
                flash(f"{form.email.data} have logged in successfully!" , 'success')
                return redirect(url_for('home'))
            else:
                flash(f"Login Failed! Please check email and password." , 'danger')
        else:
            redirect(url_for('login'))
    else:
        redirect(url_for('login'))
    return render_template('login.html', form=form, title='Login')

# run call
if __name__ == "__main__":
    app.run(debug=True)