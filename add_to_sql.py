from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pathlib import Path
from search_engine import DATABASE, PASSWORD, SERVER, USERNAME
import json
import mysql.connector 
import multiprocessing

mydb = mysql.connector.connect (host='localhost',user='root',passwd='root',database='prateekb')
base_path=Path(__file__)
my_cursor=mydb.cursor()
# db_path = app.config['SQLALCHEMY_DATABASE_URI']
# e = create_engine(db_path)
# s = Session(e)
def convertdictToTuples(diction):
    temp=list(diction.values())
    temp[-1]=json.dumps(temp[-1])
    temp[-2]=json.dumps(temp[-2])
    temp[-3]=json.dumps(temp[-3])
    temp=tuple(temp)
    return temp
def add_business():
    path_to_json = (base_path / "../yelp_academic_dataset_business.json").resolve()
    with open(path_to_json, encoding='utf-8') as f:
        business_data= json.load(f)
    resultTupList=list(map(convertdictToTuples,business_data))
    sql = "INSERT INTO business ( business_id,name,address,city,state,postal_code,latitude,longitude,stars,review_count,is_open,attributes,categories,hours) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    my_cursor.executemany(sql,resultTupList)
    mydb.commit()

def add_tips():
    path_to_json = (base_path / "../yelp_academic_dataset_tip.json").resolve()
    with open(path_to_json, encoding='utf-8') as f:
        tips_data= json.load(f)
    resultTupList=list(map(convertdictToTuples,tips_data))
    print(resultTupList[0])
    sql = "INSERT INTO tips ( user_id, business_id, text, date, compliment_count) VALUES (%s, %s, %s, %s, %s)"
    my_cursor.executemany(sql,resultTupList)
    mydb.commit()

# def add_user():
#     path_to_json = (base_path / "../yelp_academic_dataset_user.json").resolve()
#     with open(path_to_json, encoding='utf-8') as f:
#         business_data= json.load(f)
#     resultTupList=list(map(convertdictToTuples,business_data))
#     sql = "INSERT INTO business ( business_id,name,address,city,state,postal_code,latitude,longitude,stars,review_count,is_open,attributes,categories,hours) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     my_cursor.executemany(sql,resultTupList)
#     mydb.commit()


if __name__=='__main__':
    p1= multiprocessing.Process(target=add_business)
    p2 = multiprocessing.Process(target=add_tips)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
