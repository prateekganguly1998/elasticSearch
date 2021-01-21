from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pathlib import Path
from search_engine import DATABASE, PASSWORD, SERVER, USERNAME
import json
import mysql.connector 
import pymysql.cursors
import multiprocessing


def add_user_to_sql():
    base_path=Path(__file__)
    path_to_json = (base_path / "../yelp_academic_dataset_user.json").resolve()
    dictArr_from_INVjson = list()
    with open(path_to_json, encoding='utf-8') as f:
        for line in f:
            line = json.loads(line)
            dictArr_from_INVjson.append(line)
    out_file = open("user_dataset.json", "w")
    json.dump(dictArr_from_INVjson,out_file,indent=4)
    print("Done adding users to valid json")


if __name__ == '__main__':
    add_user_to_sql()


