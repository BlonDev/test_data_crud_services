import json
import unittest
from flask import Flask
from fake_data_crud_service.core.dao import DAO
from fake_data_crud_service.core.dao import get_dao
from fake_data_crud_service.rest.books import books
from fake_data_crud_service.config.settings import test as t
from fake_data_crud_service.resources.test_book import book_1 as test_book
from fake_data_crud_service.resources.test_book import book_2 as update_book


class BooksTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(books, url_prefix='/books')
        self.tester = self.app.test_client(self)
        dao = DAO(t['username'], t['password'], t['host'], t['port'], t['db_name'])
        dao.drop_collection('books')
        self.dao = get_dao('test')

    def test_get(self):
        self.dao.create('books', test_book)
        response = self.tester.get('/books/test/', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEquals(len(data), 1)

    def test_get_by_id(self):
        inserted_id = self.dao.create('books', test_book)
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

    def test_delete(self):
        inserted_id = self.dao.create('books', test_book)
        response = self.tester.delete('/books/test/' + str(inserted_id) + '/',
                                      content_type='application/json')
        self.assertEquals(response.status_code, 200)
        ack = json.loads(response.data)
        self.assertEqual(1, ack['ok'])
        self.assertEqual(1, ack['n'])

    def test_update(self):
        inserted_id = self.dao.create('books', test_book)
        response = self.tester.put('/books/test/' + str(inserted_id) + '/',
                                   data=json.dumps(update_book),
                                   content_type='application/json')
        self.assertEquals(response.status_code, 200)
        ack = json.loads(response.data)
        self.assertEqual(1, ack['ok'])
        self.assertEqual(1, ack['n'])

    def test_create(self):
        data = None
        try:
            data = json.dumps(test_book)
        except Exception, e:
            print e
        response = self.tester.post('/books/test/',
                                    data=data,
                                    content_type='application/json')
        self.assertEquals(response.status_code, 200)
        ack = json.loads(response.data)
        self.assertIsNotNone(ack['$oid'])
        self.assertEqual(1, len(self.dao.get('books')))
