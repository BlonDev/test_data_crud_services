import json
from flask import Flask
from bson import json_util
from flask.ext.cors import CORS
from test_data_crud_services.rest.books import books
from test_data_crud_services.resources.schema import schema


# Initiate Flask framework
app = Flask(__name__)

# Initiate and configure CORS filters
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Register blueprints
app.register_blueprint(books, url_prefix='/books')


@app.route('/', methods=['GET'])
def json_schema_service():
    return json.dumps(schema, sort_keys=True, indent=4, default=json_util.default), \
           200, \
           {'Content-Type': 'application/schema+json; charset=utf-8'}


if __name__ == '__main__':
    app.run()
