import os
import webapp2

from handlers import jinja_env
from handlers import main_handler
from handlers import book_handler
from handlers import home_handler
from handlers import userstu_handler
from handlers import newregistry_handler
from handlers import SubmitThanks_handler
from handlers import recieved_handler
from handlers import view_handler


jinja_env.init(os.path.dirname(__file__))

app = webapp2.WSGIApplication([
    ('/', main_handler.MainHandler),
    ('/books', book_handler.BookHandler),
    ('/userstu', userstu_handler.UserstuHandler),
    ('/home', home_handler.HomeHandler),
    ('/newregistry', newregistry_handler.NewRegistryHandler),
    ('/submitthanks', SubmitThanks_handler.SubmitThanksHandler),
    ('/view', view_handler.ViewHandler),
    ('/recieved', recieved_handler.RecievedHandler),

], debug=True)
