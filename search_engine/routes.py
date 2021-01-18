from search_engine import app
from search_engine.models import User, Tips, Business
from flask import jsonify
import json
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

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
    with open(path_to_json, encoding='utf-8') as f:
        business_data= json.load(f)
    s.bulk_insert_mappings(Business,business_data['businesses'])
    s.commit()
    return jsonify(message="Done")