from . import bp as main
from flask import render_template
from flask_login import login_required

@main.route('/')
def index():
    context = {
       'title': 'HOME',
    }
    return render_template('index.html', **context)