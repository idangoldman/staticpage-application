from flask_mongoengine import MongoEngine
db = MongoEngine()


# Define mongoengine documents
class User(db.Document):
    name = db.StringField(max_length=100)
    password = db.StringField(max_length=40)
    def __unicode__(self):
        return self.name