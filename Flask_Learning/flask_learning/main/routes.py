
from flask import render_template,request,Blueprint, jsonify
from flask_learning.models import Post

main = Blueprint('main', __name__)

class InvalidUsage(Exception):
    status_code = 410
    print('inside exception class', Exception)
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        print(rv)
        return rv
  
    
@main.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    print(response)
    return response


@main.route('/')
@main.route('/home')
def home_fun():
    
    page = request.args.get('page',1,type=int)
    
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=4)
    for page_num in posts.iter_pages():
        print(page_num)
    #print(posts[0].id)
    return render_template('home.html',posts=posts)

@main.route('/about')
def about_fun():
    return render_template('about.html', title = 'About')
    #raise InvalidUsage('This view is gone', status_code=410)

