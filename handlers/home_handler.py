import jinja_env
import logging
import webapp2



class HomeHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("MainHandler")
        html_params = {
            "title": "Main Title",
            "content": "Hello",
            
        }

   

        template = jinja_env.env.get_template('templates/home.html')
        self.response.out.write(template.render(html_params))

        

