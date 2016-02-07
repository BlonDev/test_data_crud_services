import json
from bson import json_util
from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)

@app.route("/")
def hello():
  client = MongoClient('mongodb://kalimaha:Ce09114238@ds059145.mongolab.com:59145/kalimadata')
  db = client['kalimadata']
  collection = db['books']
  books = collection.find()
  books = json.dumps(books, sort_keys=True, indent=4, default=json_util.default)
  return Response(books, content_type='application/json; charset=utf-8')

if __name__ == "__main__":
  app.run() 
