import json
from bson import json_util
from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)

@app.route("/")
def hello():
    MONGODB_URI = 'mongodb://kalimaha:Ce09114238@ds059145.mongolab.com:59145/kalimadata'
    out = []
    try:
        client = MongoClient(MONGODB_URI)
        print client
        db = client['kalimadata']
        print db
        collection = db['books']
        print collection
        books = collection.find()
        print books
        for book in books:
            out.append(book)
        return json.dumps(out, sort_keys=True, indent=4, default=json_util.default)
    except Exception, e:
        print e

if __name__ == "__main__":
  app.run()

# MONGODB_URI = 'mongodb://dev:09114238@ds059145.mongolab.com:59145/kalimadata'
# try:
#     client = MongoClient(MONGODB_URI)
#     print client
# except Exception, e:
#     print e
