from search_engine import app
from search_engine.models import User, Tips, Business, BusinessSchema, TipsSchema
from flask import jsonify
import json
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import mysql.connector

mydb = mysql.connector.connect (host="localhost",user="root",passwd="root",database="prateekb"

)

db_path = app.config['SQLALCHEMY_DATABASE_URI']
e = create_engine(db_path, echo=True)
s = Session(e)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=e))
@app.route('/')
def hello():
    tips_data=Tips.query[:5]
    tip_schema = TipsSchema()
    tips_schema = TipsSchema(many=True)
    result = tips_schema.dump(tips_data)
    return jsonify(result)

