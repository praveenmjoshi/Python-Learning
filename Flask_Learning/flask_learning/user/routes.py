from flask import render_template, url_for, flash, redirect, Blueprint
from flask_learning import db, bcrypt
from flask_learning.models import User
from flask_learning.user.forms import (RegistrationForm, Login)

users = Blueprint('users', __name__)



@users.route('/register', methods=['GET','POST'])
def register_fun():
    form = RegistrationForm()
    if form.validate_on_submit():
        
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data , email= form.email.data , password= hashed_password)
        db.session.add(user)
        db.session.commit()
        
        flash('Your account has been created! You are now able to log in ','success')
        return redirect(url_for('users.login_fun'))
    return render_template('register.html', title = 'Register', form = form)
    
@users.route('/login', methods=['GET','POST'])
def login_fun():
    form = Login()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        if form.email.data == 'admin@abc.com' and form.password.data == 'root123':
                flash('You have been logged in!','success')
                return redirect(url_for('main.home_fun'))
        else:
                print('else')
                flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)



