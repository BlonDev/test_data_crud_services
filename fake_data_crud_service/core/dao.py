from pymongo import MongoClient


class DAO:

    def __init__(self, username, password, host, port, db):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.db = db
        self.uri = self.create_connection_uri()
        self.client = MongoClient(self.uri)

    def get(self, collection_name):
        out = []
        db = self.client[self.db]
        collection = db[collection_name]
        items = collection.find()
        for item in items:
            out.append(item)
        return out

    def create_connection_uri(self):
        return 'mongodb://' + self.username + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.db
