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
        response = self.tester.get('/books/', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['ISBN'], '0-436-20305-7')
        self.assertEquals(data[0]['author'], 'Howard Marks')
        self.assertEquals(data[0]['genre'], 'non-fiction')
        self.assertEquals(data[0]['pages'], 466)
        self.assertEquals(data[0]['title'], 'Mr. Nice')
