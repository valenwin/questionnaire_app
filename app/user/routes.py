from flask import render_template, redirect, url_for
from flask import request
from flask import session

from . import user_page
from .forms import RegisterForm, LoginForm
from .models import User
from .. import db


@user_page.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User(name=name,
                    email=email,
                    password=User.make_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_page.login'))
    return render_template('user/register.html',
                           form=form)


@user_page.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    error = None
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.is_password_valid(form.password.data):
            session['user'] = user.email
            return redirect(url_for('index'))
        else:
            user = None
        if not user:
            error = 'Your email or password was entered incorrectly'
    return render_template('user/login.html',
                           form=form,
                           error=error)


@user_page.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('user_page.login'))


@user_page.route('/users')
def users():
    users_lst = User.query.all()
    return render_template('user/users.html',
                           users=users_lst)
