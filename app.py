import json
from flask import Flask
from bson import json_util
from fake_data_crud_service.rest.books import books
from fake_data_crud_service.resources.schema import schema


app = Flask(__name__)
app.register_blueprint(books, url_prefix='/books')


@app.route('/', methods=['GET'])
def json_schema_service():
    return json.dumps(schema, sort_keys=True, indent=4, default=json_util.default), \
           200, \
           {'Content-Type': 'application/schema+json; charset=utf-8'}


if __name__ == '__main__':
    app.run()
