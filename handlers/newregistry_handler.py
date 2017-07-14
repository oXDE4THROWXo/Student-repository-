import jinja_env
import logging
import webapp2

from models import newregistry

class NewRegistryHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("NewRegistry")
        html_params = {
            "title": "Main Title",
            "content": "Hello"
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))