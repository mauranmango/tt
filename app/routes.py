from app import app
from flask import render_template, request, session, redirect, flash, url_for
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.forms import LoginForm
from app.models import User, Post


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': "ben"}
    posts = [
        {
            'author': {'username': 'Ben'},
            'body': 'sunny day'
        },
        {
            'author': {'username': 'Miguel'},
            'body': 'flask mega tutorial'
        }
    ]
    return render_template('index.html', title='Index', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, form.remember_me.data)
        flash(f"User logged in: {form.username.data} -- remember_me:{form.remember_me.data}")
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title="Sign In", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/thank_you')
@login_required
def thank_you():
    return render_template('thank_you.html', title='Thank You')
