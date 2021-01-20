from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DATABASE = 'prateekb'
SERVER = 'localhost'
USERNAME = 'root'
PASSWORD = 'root'

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f311ff320d8b4c9091f1e2451114998b'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:root@localhost/prateekb'



db = SQLAlchemy(app)


from search_engine import routes