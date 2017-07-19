import jinja_env
import logging
import webapp2

from google.appengine.ext import ndb
from models import newregistry

class ViewHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("NewRegistry")
        items = newregistry.NewRegistry.query().fetch()
        

        content_str = ""
        for item in items:
            logging.info("Key =" + str(item.key.id()))
            content_str += "<input name= keyid type= \"checkbox\" value=\""+ item.key.urlsafe() + "\">"
            content_str += "<h3>Item : " + item.student_item + "</h3>"
            content_str += "<p>" + item.student_contents + "</p>"
            content_str += "</input>"



        html_params = {
            "title": "Main Title",
            "html_item": content_str,
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
