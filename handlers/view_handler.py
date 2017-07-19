import jinja_env
import logging
import webapp2

from google.appengine.ext import ndb
from models import newregistry
from models import userstu
from google.appengine.api import users

class ViewHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user == None:
            self.redirect("/")
            return

        logging.info("NewRegistry")
        items = newregistry.NewRegistry.query().fetch()
        

        content_str = ""
        for item in items:
            logging.info("Key =" + str(item.key.id()))
            content_str += "<input name= keyid type= \"checkbox\" value=\""+ item.key.urlsafe() + "\">"
            content_str += "<h3>Item : " + item.student_item + "</h3>"
            content_str += "<p>" + item.student_contents + "</p>"
            content_str += "</input>"

        user_query = userstu.Userstu.query(userstu.Userstu.name == user.email())
        user_obj = user_query.get()
        logging.info(user_obj)

        html_params = {
            "title": "Main Title",
            "html_item": content_str,
            "user_name": "Chris Placeholder"
        }
        template = jinja_env.env.get_template('templates/view.html')
        self.response.out.write(template.render(html_params))


    def post(self):
        logging.info("There was a post")
        r_keyid = self.request.get_all("keyid")
        #r_contents = self.request.get("form_contents")
        #logging.info(r_item)
        logging.info(r_keyid)
        for key in r_keyid:
            logging.info(ndb.Key(urlsafe=key))
            ndb.Key(urlsafe=key).delete()

        
        # output = newregistry.NewRegistry(
        #     student_item = r_item,
        #     student_contents = r_contents,
        #     student_email = "fixthislater"
        # )
        # output.put()
        self.redirect("/view")
