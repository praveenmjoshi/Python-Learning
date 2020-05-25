
from flask import render_template,request,Blueprint
from flask_learning.models import Post

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home_fun():
    
    page = request.args.get('page',1,type=int)
    
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=2)
    for page_num in posts.iter_pages():
        print(page_num)
    #print(posts[0].id)
    return render_template('home.html',posts=posts)

@main.route('/about')
def about_fun():
    return render_template('about.html', title = 'About')

