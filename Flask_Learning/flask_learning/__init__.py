#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:41:08 2020

@author: praveen
"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_learning.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    ''' 
    Below are the extension for applications so instead of directly defining as db = SQLAlchemy(app)
    We declare them independent to app and call init_app method on them.
    
    '''
    db.init_app(app) 
    bcrypt.init_app(app)
    
    from flask_learning.user.routes import users
    from flask_learning.posts.routes import posts
    from flask_learning.main.routes import main
    from flask_learning.errors.handlers import errors
    
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    
    ''' 
    import app as 'from flask import current_app' if needed
    except in run.py file where in we import this function and call it.
    '''
    return app