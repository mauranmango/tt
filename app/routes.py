import inspect
from app import app
from flask import render_template, request, session, redirect, flash, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
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
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user: {form.username.data} -- remember_me:{form.remember_me.data}")
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)


@app.route('/api')
def show_api():
    return f'API_KEY= {app.config.get("API_KEY")}, ' \
           f'SECRET_KEY= {app.config.get("SECRET_KEY")},'


@app.route('/thank_you')
def thank_you():
    # text = dict(request.headers)  # save all headers as a dictionary
    return render_template('thank_you.html', title='Thank You')
