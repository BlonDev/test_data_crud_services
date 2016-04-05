import json
from flask import Response
from flask import request
from flask import Blueprint
from bson import json_util
from fake_data_crud_service.core.dao import get_dao


books = Blueprint('books', __name__)


@books.route('/<environment>/', methods=['GET'])
def get(environment):
    dao = get_dao(environment)
    out = json.dumps(dao.get('books'), sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')


@books.route('/<environment>/<item_id>/', methods=['GET'])
def get_by_id(environment, item_id):
    dao = get_dao(environment)
    out = json.dumps(dao.get_by_id('books', item_id), sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')


@books.route('/<environment>/<item_id>/', methods=['DELETE'])
def delete(environment, item_id):
    dao = get_dao(environment)
    out = json.dumps(dao.delete('books', item_id), sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')


@books.route('/<environment>/<item_id>/', methods=['PUT'])
def update(environment, item_id):
    item = json.loads(request.data)
    dao = get_dao(environment)
    ack = dao.update('books', item_id, item)
    out = json.dumps(ack, sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')


@books.route('/<environment>/', methods=['POST'])
def create(environment):
    item = json.loads(request.data)
    dao = get_dao(environment)
    ack = dao.create('books', item)
    out = json.dumps(ack, sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')
