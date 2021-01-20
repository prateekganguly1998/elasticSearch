from search_engine import app
from search_engine.models import User, Tips, Business
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
    print()
    return jsonify(message="Hello")

@app.route('/insert')
def insert():
    base_path=Path(__file__).parent
    print(db_path)
    path_to_json = (base_path / "../yelp_academic_dataset_business.json").resolve()
    with open(path_to_json, mode="r" , encoding='utf-8') as f:
        business_data= json.load(f)
    s.bulk_insert_mappings(Business,business_data['businesses'],)
    s.commit()
    return jsonify(message="Done")

@app.route('/insert_final')
def insert_final():
    base_path=Path(__file__).parent
    my_cursor=mydb.cursor()
    path_to_json = (base_path / "../yelp_academic_dataset_business.json").resolve()
    with open(path_to_json, mode="r" , encoding='utf-8') as f:
        business_data= json.load(f)
    def convertdictToTuples(diction):
        temp[-1]=json.dumps(temp[-1])
        temp[-2]=json.dumps(temp[-2])
        temp[-3]=json.dumps(temp[-3])
        temp=tuple(temp)
        return temp
    resultTupList=list(map(convertdictToTuples,business_data))
    sql = "INSERT INTO business ( business_id,name,address,city,state,postal_code,latitude,longitude,stars,review_count,is_open,attributes,categories) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    print(type(resultTupList[0][10]))
    my_cursor.executemany(sql,resultTupList)
    mydb.commit()
    return jsonify(message = 'done')
