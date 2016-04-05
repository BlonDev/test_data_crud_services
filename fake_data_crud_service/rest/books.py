import json
from flask import request
from flask import Response
from bson import json_util
from flask import Blueprint
from flask.ext.cors import cross_origin
from fake_data_crud_service.core.dao import get_dao


books = Blueprint('books', __name__)


@books.route('/<environment>/', methods=['GET'])
@cross_origin(origins='*', headers=['Content-Type'])
def get(environment):
    dao = get_dao(environment)
    out = json.dumps(dao.get('books'), sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')


@books.route('/<environment>/<item_id>/', methods=['GET'])
@cross_origin(origins='*', headers=['Content-Type'])
def get_by_id(environment, item_id):
    dao = get_dao(environment)
    out = json.dumps(dao.get_by_id('books', item_id), sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')


@books.route('/<environment>/<item_id>/', methods=['DELETE'])
@cross_origin(origins='*', headers=['Content-Type'])
def delete(environment, item_id):
    dao = get_dao(environment)
    out = json.dumps(dao.delete('books', item_id), sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')


@books.route('/<environment>/<item_id>/', methods=['PUT'])
@cross_origin(origins='*', headers=['Content-Type'])
def update(environment, item_id):
    item = json.loads(request.data)
    dao = get_dao(environment)
    ack = dao.update('books', item_id, item)
    out = json.dumps(ack, sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')


@books.route('/<environment>/', methods=['POST'])
@cross_origin(origins='*', headers=['Content-Type'])
def create(environment):
    item = json.loads(request.data)
    dao = get_dao(environment)
    ack = dao.create('books', item)
    out = json.dumps(ack, sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')
