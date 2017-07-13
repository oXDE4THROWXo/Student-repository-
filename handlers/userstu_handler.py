import jinja_env
import logging
import webapp2

from models import userstu

class UserstuHandler(webapp2.RequestHandler):
    def get(self):