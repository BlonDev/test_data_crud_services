import json
from flask import Response
from flask import Blueprint
from bson import json_util
from fake_data_crud_service.core.dao import DAO
from fake_data_crud_service.config.settings import parameters as C


books = Blueprint('books', __name__)


@books.route('/')
def get():
    dao = DAO(C['username'], C['password'], C['host'], C['port'], C['db_name'])
    out = json.dumps(dao.get('books'), sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')


@books.route('/<id>/')
def get_by_id(id):
    dao = DAO(C['username'], C['password'], C['host'], C['port'], C['db_name'])
    out = json.dumps(dao.get_by_id('books', id), sort_keys=True, indent=4, default=json_util.default)
    return Response(out, content_type='application/json; charset=utf-8')
