import jinja_env
import logging
import webapp2

from models import book

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.env.get_template('templates/aboutus.html')
        self.response.out.write(template.render())