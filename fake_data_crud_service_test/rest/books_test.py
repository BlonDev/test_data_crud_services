import json
import unittest
from flask import Flask
from fake_data_crud_service.rest.books import books


class BooksTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(books, url_prefix='/books')
        self.tester = self.app.test_client(self)

    def test_get(self):
        response = self.tester.get('/books/test/', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEquals(len(data), 1)

    def test_get_by_id(self):
        response = self.tester.get('/books/test/56b78893e4b05ba6b4983386/', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEquals(data['ISBN'], '0-436-20305-7')
        self.assertEquals(data['author'], 'Howard Marks')
        self.assertEquals(data['genre'], 'non-fiction')
        self.assertEquals(data['pages'], 466)
        self.assertEquals(data['title'], 'Mr. Nice')
