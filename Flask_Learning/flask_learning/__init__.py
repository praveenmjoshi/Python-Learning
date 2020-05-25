#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:41:08 2020

@author: praveen
"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c4f0fb87dc671f00262836821a8af65d' #generated from command line secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from flask_learning.user.routes import users
from flask_learning.posts.routes import posts
from flask_learning.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)