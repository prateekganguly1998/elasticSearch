from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SECRET_KEY'] = 'f311ff320d8b4c9091f1e2451114998b'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///E:/projects/elastic_search/site.db'



db = SQLAlchemy(app)


from search_engine import routes