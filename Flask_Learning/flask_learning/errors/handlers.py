# -*- coding: utf-8 -*-

from flask import Blueprint

errors = Blueprint('errors', __name__)



@errors.app_errorhandler(404)
def error_404(error):
    print('hello from error handler ')
    return '<h1>Resource is Unknown, Sorry!</h1>'


@errors.app_errorhandler(400)
def error_400(error):
    print('hello from error handler ')
    return '<h1>Bad Request, try again</h1>'


@errors.app_errorhandler(500)
def error_500(error):
    print('hello from error handler ')
    return '<h1>Internal server error</h1>'