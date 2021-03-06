import jinja_env
import logging
import webapp2

from models import userstu
from google.appengine.api import users

class UserstuHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("Userstu")


        html_params = {
            "content": "Welcome"
        }
        template = jinja_env.env.get_template('templates/logintemplate.html')
        self.response.out.write(template.render(html_params))


    def post(self):
        user = users.get_current_user()
        if user == None:
            self.redirect("/")
            return
        logging.info("There was a post")
        r_age = self.request.get("form_age")
        r_name = self.request.get("form_name")
        r_gender = self.request.get("form_gender")
        r_school = self.request.get("form_school")
        r_year = self.request.get("form_year")
        logging.info(r_year)
        logging.info(r_name)
        logging.info(r_gender)
        
        output = userstu.Userstu(
            student_name = r_name,
            student_age = r_age,
            student_gender = r_gender,
            student_school = r_school,
            student_year = r_year,
            student_email = user.email(),
        )
        output.put()
        self.redirect("/home")


