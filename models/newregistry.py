from google.appengine.ext import ndb

class NewRegistry(ndb.Model):
    student_item = ndb.StringProperty()
    student_contents = ndb.StringProperty()
    student_email = ndb.StringProperty()