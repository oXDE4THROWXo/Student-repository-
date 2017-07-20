import jinja_env
import logging
import webapp2

from models import newregistry
from models import userstu
from google.appengine.api import users

class NewRegistryHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user == None:
            self.redirect("/")
            return
        logging.info("NewRegistry")
        items = newregistry.NewRegistry.query().fetch()
        student = userstu.Userstu.query(user.email()==userstu.Userstu.student_email).get()

        content_str = ""
        for item in items:
            content_str += "<div>"
            content_str += "<h3>Item : " + item.student_item + "</h3>"
            content_str += "<p>" + item.student_contents + "</p>"
            content_str += "</div>"



        html_params = {
            "title": "Main Title",
            "html_item": content_str,
            "user_name": student.student_name,
        }
        template = jinja_env.env.get_template('templates/newregistrytemplate.html')
        self.response.out.write(template.render(html_params))


    def post(self):
        logging.info("There was a post")
        r_item = self.request.get("form_item")
        r_contents = self.request.get("form_contents")
        logging.info(r_item)
        logging.info(r_contents)
        
        
        output = newregistry.NewRegistry(
            student_item = r_item,
            student_contents = r_contents,
            student_email = "fixthislater"
        )
        output.put()
        self.redirect("/newregistry")
