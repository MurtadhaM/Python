# Author: Murtadha Marzouq
# Date: 2020-11-24
# Group: 15 
# Assignment: Final Project
from forms import LoginForm
from forms import RegisterForm
import bcrypt
from flask import session
from models import User as User
from database import db
from flask import url_for
from flask import redirect
from flask import request
from flask import render_template
import os  # os is used to get environment variables IP & PORT
from flask import Flask, render_template

app = Flask(__name__)  # create an app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Travel_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'GROUPROJECT'
app.config["IMAGE_UPLOADS"] = "static"
db.init_app(app)
with app.app_context():
    db.create_all()  
@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        the_user = db.session.query(User).filter_by(
            email=request.form['email']).one()
        if bcrypt.checkpw(request.form['password'].encode('utf-8'), the_user.password):
            session['user'] = the_user.first_name
            session['user_id'] = the_user.id
            return redirect(url_for('index'))
        login_form.password.errors = ["Incorrect username or password."]
        return render_template("login.html", form=login_form)
    else:
        return render_template("login.html", form=login_form)


@app.route('/logout')
def logout():
    if session.get('user'):
        session.clear()

    return redirect(url_for('login'))


# REGISTRATION PAGE #
@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        # salt and hash password
        h_password = bcrypt.hashpw(
            request.form['password'].encode('utf-8'), bcrypt.gensalt())
        # get entered user data
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        # create user model
        new_user = User(first_name, last_name,
                        request.form['email'], h_password)
        db.session.add(new_user)
        db.session.commit()
        session['user'] = first_name
        session['user_id'] = new_user.id
        return redirect(url_for('index'))

    return render_template('register.html', form=form)


@app.route('/index')
def index():
    if session.get('user'):
        return render_template("index.html", user=session['user'])
    else:
        return redirect(url_for('login'))


@app.route('/profile/userID')
def profile():
    # insert code
    if session.get('user'):
        user = db.session.query(User).filter_by(id=session['user_id']).one()
        return render_template("profile.html", user=user)
    else:
        return redirect(url_for('login'))
