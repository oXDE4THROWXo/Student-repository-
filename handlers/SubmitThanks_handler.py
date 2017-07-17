import jinja_env
import logging
import webapp2


class SubmitThanksHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.env.get_template('templates/submitthanks.html')
        self.response.out.write(template.render())