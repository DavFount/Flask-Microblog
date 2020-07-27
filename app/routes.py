from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David'}
    posts = [
        {
            'author': {'username': 'David'},
            'body': 'Beautiful day in Sacramento!'
        },
        {
            'author': {'username': 'Katie'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)