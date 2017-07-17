from google.appengine.ext import ndb




class Userstu(ndb.Model):
    student_name = ndb.StringProperty()
    student_age = ndb.StringProperty()
    student_gender = ndb.StringProperty()
    student_school = ndb.StringProperty()
    student_year = ndb.StringProperty()
    student_email = ndb.StringProperty()
    
