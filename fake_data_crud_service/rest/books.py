import json
from flask import Response
from flask import Blueprint
from bson import json_util
from fake_data_crud_service.core.dao import get_dao


books = Blueprint('books', __name__)


@books.route('/<environment>/')
def get(environment):
    dao = get_dao(environment)
    out = json.dumps(dao.get('books'), sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')


@books.route('/<environment>/<id>/')
def get_by_id(environment, id):
    dao = get_dao(environment)
    out = json.dumps(dao.get_by_id('books', id), sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')
