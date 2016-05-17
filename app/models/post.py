from ferris import BasicModel
from google.appengine.ext import ndb


class Post(BasicModel):
    title = ndb.StringProperty()
    content = ndb.TextProperty()