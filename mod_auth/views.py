
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from flask_login import LoginManager, login_user, logout_user

from mod_auth.models import User

mod_auth = Blueprint('auth',__name__, url_prefix='/auth')

'''
LOGIN VIEW
'''
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