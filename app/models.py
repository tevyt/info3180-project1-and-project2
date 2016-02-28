from . import db
from random import getrandbits

class User(db.Model):
    user_id = db.Column(db.String(10) , primary_key = True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(10))

    def generate_user_id(self):
        return '6200%d' % getrandbits(16)

    def __init__(self , firstname , lastname , age , sex):
        self.user_id = self.generate_user_id()
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex

    def __repr__(self):
        return '<User %r %r %r %d %r>' % (self.user_id , self.firstname , self.lastname , self.age , self.sex)

