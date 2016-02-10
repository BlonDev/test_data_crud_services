import json
import unittest
from flask import Flask
from fake_data_crud_service.core.dao import DAO
from fake_data_crud_service.core.dao import get_dao
from fake_data_crud_service.rest.books import books
from fake_data_crud_service.config.settings import test as t
from fake_data_crud_service.resources.test_book import book as test_book


class BooksTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(books, url_prefix='/books')
        self.tester = self.app.test_client(self)
        dao = DAO(t['username'], t['password'], t['host'], t['port'], t['db_name'])
        dao.drop_collection('books')

    def test_get(self):
        dao = get_dao('test')
        dao.create('books', test_book)
        response = self.tester.get('/books/test/', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEquals(len(data), 1)

    def test_get_by_id(self):
        dao = get_dao('test')
        inserted_id = dao.create('books', test_book)
        response = self.tester.get('/books/test/' + str(inserted_id) + '/',
                                   content_type='application/json')
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEquals(data['ISBN'], '0436203057')
        self.assertEquals(len(data['authors']), 1)
        self.assertEquals(data['authors'][0], 'Howard Marks')
        self.assertEquals(data['genre'], 'non-fiction')
        self.assertEquals(data['pages'], 466)
        self.assertEquals(data['title'], 'Mr. Nice')
