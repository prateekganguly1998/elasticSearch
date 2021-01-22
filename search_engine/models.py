from search_engine import db, ma
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime


class User(db.Model):
    user_id = db.Column(db.String(30),primary_key=True, nullable = False)
    name = db.Column(db.String(100),nullable=False)
    review_count = db.Column(db.Integer)
    yelping_since = db.Column(db.String(30))
    useful = db.Column(db.Integer)
    funny =  db.Column(db.Integer)
    cool =  db.Column(db.Integer)
    elite = db.Column(db.Text)
    friends = db.Column(db.Text(4294000000))
    fans = db.Column(db.Integer)
    average_stars = db.Column(db.Float(10))
    compliment_hot = db.Column(db.Integer)
    compliment_more = db.Column(db.Integer)
    compliment_profile = db.Column(db.Integer)
    compliment_cute = db.Column(db.Integer)
    compliment_list = db.Column(db.Integer)
    compliment_note = db.Column(db.Integer)
    compliment_plain = db.Column(db.Integer)
    compliment_cool = db.Column(db.Integer)
    compliment_funny = db.Column(db.Integer)
    compliment_writer = db.Column(db.Integer)
    compliment_photos = db.Column(db.Integer)
    tips = db.relationship('Tips',backref='user',lazy = True)

    def __repr__(self):
        return f"User('{self.name}', '{self.yelping_since}' , '{self.review_count}')"


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


 #
class Tips(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.String(30), db.ForeignKey('user.user_id'), nullable = False)
    business_id = db.Column(db.String(30), db.ForeignKey('business.business_id') ,  nullable = False)
    text= db.Column(db.Text, nullable = False)
    date = db.Column(db.String(30),nullable = False , default = datetime.utcnow)
    compliment_count = db.Column(db.Integer)

    def __repr__(self):
        return f"Tip('{self.user_id}', '{self.business_id}' , '{self.text}')"



class TipsSchema(ma.Schema):
    class Meta:
        fields = ('business_id','user_id','text','date','compliment_count')


class BusinessSchema(ma.Schema):
    tips = ma.Nested(TipsSchema, many = True)
    class Meta:
        fields = ('business_id','name','address','city','state','postal_code','latitude','longitude','stars','review_count','is_open','attributes','categories','hours', 'tips')
  




