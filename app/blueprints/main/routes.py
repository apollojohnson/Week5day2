from . import bp as main
from flask import render_template
from app.blueprints.blog.models import Post

@main.route('/')
def index():
    context = {
       'title': 'HOME',
       'posts': Post.query.all()
    }
    return render_template('index.html', **context)