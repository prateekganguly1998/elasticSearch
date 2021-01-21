from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pathlib import Path
from search_engine import DATABASE, PASSWORD, SERVER, USERNAME
import json
import mysql.connector 
import pymysql.cursors
import multiprocessing

mydb = pymysql.connect(host='localhost',user='root',passwd='root',database='prateekb', cursorclass=pymysql.cursors.DictCursor)
base_path=Path(__file__)
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
    with mydb:
        with mydb.cursor() as cursor:
            sql = "INSERT INTO business ( business_id,name,address,city,state,postal_code,latitude,longitude,stars,review_count,is_open,attributes,categories,hours) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.executemany(sql,resultTupList)
            mydb.commit()
    print('Added Business Data')
    

def add_tips():
    path_to_json = (base_path / "../yelp_academic_dataset_tip.json").resolve()
    with open(path_to_json, encoding='utf-8') as f:
        tips_data= json.load(f)
    resultTupList=list(map(convertdictToTuples,tips_data))
    print(resultTupList[0])
    with mydb:
        with mydb.cursor() as cursor:
             sql = "INSERT INTO tips ( user_id, business_id, text, date, compliment_count) VALUES (%s, %s, %s, %s, %s)"
             cursor.executemany(sql,resultTupList)
             mydb.commit()
    print('Added Tips Data')
#code to add foreign key to none   
def add_foreign_key_check():
    with mydb:
        with mydb.cursor() as cursor:
            sql = "SET GLOBAL FOREIGN_KEY_CHECKS = 0"
            cursor.execute(sql)    
            mydb.commit()
    print("added check")


#add users to sql
def add_user():
    path_to_json = (base_path / "../user_dataset.json").resolve()
    with open(path_to_json, encoding='utf-8') as f:
        user_data= json.load(f)
    resultTupList=list(map(convertdictToTuples,user_data))
    with mydb:
        with mydb.cursor() as cursor:
            sql = "INSERT INTO user ( user_id,name,review_count,yelping_since, useful, funny , cool , elite, friends , fans , average_stars , compliment_hot , compliment_more,compliment_profile,compliment_cute,compliment_list,compliment_note,compliment_plain,compliment_cool,compliment_funny,compliment_writer, compliment_photos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.executemany(sql,resultTupList)
            mydb.commit()
    print('Done adding user')

    


if __name__=='__main__':
    # p1 = multiprocessing.Process(target=add_foreign_key_check)
    # p2= multiprocessing.Process(target=add_business)
    # p3 = multiprocessing.Process(target=add_tips)
    # p1.start()
    # p1.join()
    # p2.start()
    # p3.start()
    # p3.join()
    # p2.join()
    add_user()
