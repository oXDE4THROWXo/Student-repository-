import jinja_env
import logging
import webapp2

from models import userstu

class UserstuHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("Userstu")
        html_params = {
            "title": "Main Title",
            "content": "Welcome"
        }
        template = jinja_env.env.get_template('templates/logintemplate.html')
        self.response.out.write(template.render(html_params))
    