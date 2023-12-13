import inspect
from app import app
from flask import render_template


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


@app.route('/')
@app.route('/login')
def login():
    names = ['ben', 'tim', 'sarah', 'jim', 'tom']
    return render_template('login.html', names=names)


@app.route('/api')
def show_api():
    return f'API_KEY= {app.config.get("API_KEY")}, ' \
           f'SECRET_KEY= {app.config.get("SECRET_KEY")},'
