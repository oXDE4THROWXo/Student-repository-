import jinja_env
import logging
import webapp2

from models import home

class HomeHandler(webapp2.RequestHandler):
    def get(self):