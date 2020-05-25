# -*- coding: utf-8 -*-


from flask import (render_template, url_for, flash,
                   redirect, request, Blueprint)
from flask_learning import db
from flask_learning.models import Post, User
from flask_learning.posts.forms import PostForm

posts = Blueprint('posts', __name__)
   
@posts.route('/post/new', methods=['GET','POST'])
def post_new():
    form = PostForm()
    print(form.title.data)
    print(form.content.data)
    if form.validate_on_submit():
        post = Post(title = form.title.data , content = form.content.data, user_id = 1)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home_fun'))
    return render_template('create_post.html',title='Create Post', form=form,legend='New Post')

@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    print(post)
    return render_template('post.html', title = post.title, post = post)
    

@posts.route('/post/<int:post_id>/update',methods=['GET','POST'])
def update_post(post_id):
    print(request.method)
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated','success')
        return redirect(url_for('posts.get_post', post_id = post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html',title='Create Post', form=form,legend='Update Post')

@posts.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    
    return redirect(url_for('main.home_fun'))


@posts.route('/user/<string:username>')
def user_posts(username):
    
    page = request.args.get('page',1,type=int)
    user = User.query.filter_by(username = username).first_or_404()
    posts = Post.query.filter_by(author=user)\
    .order_by(Post.date_posted.desc())\
    .paginate(page=page,per_page=2)
    for page_num in posts.iter_pages():
        print(page_num)
    #print(posts[0].id)
    return render_template('home.html',posts=posts)