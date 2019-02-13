from flask import Blueprint, render_template

from blog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html')

@main.route('/snippet')
def snippet():
    return render_template('materialize.html')