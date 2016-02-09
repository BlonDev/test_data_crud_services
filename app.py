import json
from bson import json_util
from flask import Flask
from pymongo import MongoClient
from flask import Flask
from fake_data_crud_service.rest.books import books
from fake_data_crud_service.resources.schema import schema


class RootREST:

    def __init__(self, host, run_flask):
        self.host = host
        self.run_flask = run_flask
        self.app = Flask(__name__)
        self.app.register_blueprint(books, url_prefix='/books')

        # # Root service.
        @self.app.route('/', methods=['GET'])
        def say_hello_service():
            return json.dumps(schema, sort_keys=True, indent=4, default=json_util.default),\
                   200,\
                   {'Content-Type': 'application/schema+json; charset=utf-8'}

        # Run Flask.
        if self.run_flask:                              # pragma: no cover
            self.app.run(host=self.host, debug=True)    # pragma: no cover


def run_engine(host):                                   # pragma: no cover
    RootREST(host, True)                                # pragma: no cover

if __name__ == '__main__':                              # pragma: no cover
    run_engine('localhost')                             # pragma: no cover