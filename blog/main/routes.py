from flask import Blueprint, render_template, request
from blog.models import Post


main = Blueprint('main', __name__)

@main.route("/landingpage")
def landingPage():
        return render_template('landingPage.html', title='Portflio Project Landing Page')


@main.route("/")
@main.route("/home")
def home():
        page = request.args.get('page', 1, type=int)

        posts = Post.query.order_by(Post.date_created.desc()).paginate(page=page, per_page=6)
        return render_template('home.html', posts=posts)

@main.route("/about")
def about():
        return render_template('about.html', title='about')