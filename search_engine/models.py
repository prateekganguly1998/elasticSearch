from search_engine import db
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(20), nullable = False)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}' , '{self.image_file}')"


class Business(db.Model):
    business_id = db.Column(db.String(30),primary_key=True)
    name = db.Column(db.String(150),nullable=False)
    address = db.Column(db.String(250))
    city = db.Column(db.String(150))
    state = db.Column(db.String(50))
    postal_code = db.Column(db.String(10))
    latitude = db.Column(db.Float(10))
    longitude = db.Column(db.Float(10))
    stars = db.Column(db.Float(10))
    review_count =  db.Column(db.Integer)
    is_open =  db.Column(db.Integer, default=1)
    attributes = db.Column(JSON,nullable=True)
    categories = db.Column(db.String(900),nullable=True)
    hours = db.Column(JSON,nullable=True)
    tips=db.relationship('Tips',backref='business',lazy = True)


    def __repr__(self):
        return f"Business('{self.name}', '{self.city}' , '{self.address}')"


 #db.ForeignKey('business.business_id') ,
class Tips(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.String(30), nullable = False)
    business_id = db.Column(db.String(30),  nullable = False)
    text= db.Column(db.Text, nullable = False)
    date = db.Column(db.String(30),nullable = False , default = datetime.utcnow)
    compliment_count = db.Column(db.Integer)

    def __repr__(self):
        return f"Tip('{self.user_id}', '{self.business_id}' , '{self.text}')"
