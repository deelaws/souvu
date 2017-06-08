
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from flask_login import LoginManager, login_user, logout_user, \
                        login_required

from app.app import db
from mod_auth.models import User
from mod_auth.forms import SignupForm

mod_auth = Blueprint('auth',__name__, url_prefix='/auth')

"""
Login view
"""
@mod_auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        user = User.query.filter_by(email=login_form.user_name.data).first()
        if user is None:
            login_form.user_name.errors.append('Invalid Username or password') 
        else:
            # log the user *in* :)
            print(user.email)
            print(type(user))
            if not user.check_password(login_form.password.data):
                # Incorrect password :(
                # TODO: FIXME: implement brute force protection a.k.a  rate limiting
                login_form.password.errors.append('Invalid Username or password')
            else:
                # Yay! User information is correct
                flash('Logged in successfully.')
                login_user(user, remember=True)
                return load_main_page(user)

    return render_template('auth/login.html', form=login_form)

"""
Logout View
"""
@mod_auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    flash('Logged out successfully.')
    logout_user()
    return redirect(url_for('hello'))

"""
Signup User
"""
@mod_auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    print(form.password.data)
    if request.method == 'POST' and form.validate():
        # Check whether the user name is unique
        user_name_taken = db.session.query(User.email).filter_by(email=form.user_name.data).scalar() is not None
        print("heo")
        if user_name_taken:
            form.user_name.errors.append('Username taken')
        else:
            user = User(email=form.user_name.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Thanks for registering')
            # TODO: send email to the user for registration signup
            return redirect(url_for('hello'))
    return render_template('auth/signup.html', form=form)

@mod_auth.route('/mems', methods=['GET', 'POST'])
def hello():
    print("Hello there I am here")
    return "Fooo Bar"