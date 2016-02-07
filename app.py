from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)

@app.route("/")
def hello():
  client = MongoClient('mongodb://kalimaha:Ce09114238@ds059145.mongolab.com:59145/kalimadata')
  db = client['kalimadata']
  collection = db['books']
  return collection.find()

if __name__ == "__main__":
  app.run() 
