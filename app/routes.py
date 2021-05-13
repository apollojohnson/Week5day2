from flask import current_app as app, render_template
from app.blueprints.blog.models import Post

@app.route('/')
def index():
    context = {
       'title': 'HOME',
       'posts': Post.query.all()
    }
    return render_template('index.html', **context)
