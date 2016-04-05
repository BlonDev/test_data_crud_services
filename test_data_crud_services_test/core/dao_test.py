import unittest
from test_data_crud_services.core.dao import DAO
from test_data_crud_services.core.dao import get_dao
from test_data_crud_services.config.settings import test as t
from test_data_crud_services.config.settings import production as p
from test_data_crud_services.resources.test_book import book_1 as test_book
from test_data_crud_services.resources.test_book import book_2 as update_book


class TestDataCRUDServicesTest(unittest.TestCase):

    def setUp(self):
        dao = DAO(t['username'], t['password'], t['host'], t['port'], t['db_name'])
        dao.drop_collection('books')

    def test_get_dao(self):
        dao = get_dao('production')
        self.assertEqual(dao.username, p['username'])
        self.assertEqual(dao.password, p['password'])
        self.assertEqual(dao.host, p['host'])
        self.assertEqual(dao.port, p['port'])
        self.assertEqual(dao.db, p['db_name'])
        dao = get_dao('test')
        self.assertEqual(dao.username, t['username'])
        self.assertEqual(dao.password, t['password'])
        self.assertEqual(dao.host, t['host'])
        self.assertEqual(dao.port, t['port'])
        self.assertEqual(dao.db, t['db_name'])

    def test_create_connection_uri(self):
        dao = get_dao('test')
        uri = dao.create_connection_uri()
        self.assertEqual(uri, 'mongodb://kalimaha:Ce09114238@ds061375.mongolab.com:61375/kalimatest')

    def test_create_item(self):
        dao = get_dao('test')
        inserted_id = dao.create('books', test_book)
        self.assertIsNotNone(inserted_id)

    def test_get(self):
        dao = get_dao('test')
        dao.create('books', test_book)
        items = dao.get('books')
        self.assertEqual(len(items), 1)

    def test_get_by_id(self):
        dao = get_dao('test')
        inserted_id = dao.create('books', test_book)
        item = dao.get_by_id('books', inserted_id)
        self.assertIsNotNone(item)
        self.assertEqual(item['ISBN'], '0436203057')
        self.assertEqual(len(item['authors']), 1)
        self.assertEqual(item['authors'][0], 'Howard Marks')
        self.assertEqual(item['genre'], 'non-fiction')
        self.assertEqual(item['title'], 'Mr. Nice')
        self.assertEqual(item['pages'], 466)

    def test_delete(self):
        dao = get_dao('test')
        inserted_id = dao.create('books', test_book)
        ack = dao.delete('books', inserted_id)
        self.assertEqual(1, ack['ok'])
        self.assertEqual(1, ack['n'])

    def test_update(self):
        dao = get_dao('test')
        inserted_id = dao.create('books', test_book)
        item = dao.get_by_id('books', inserted_id)
        self.assertIsNotNone(item)
        self.assertEqual(item['ISBN'], '0436203057')
        self.assertEqual(len(item['authors']), 1)
        self.assertEqual(item['authors'][0], 'Howard Marks')
        self.assertEqual(item['genre'], 'non-fiction')
        self.assertEqual(item['title'], 'Mr. Nice')
        self.assertEqual(item['pages'], 466)
        dao.update('books', inserted_id, update_book)
        item = dao.get_by_id('books', inserted_id)
        self.assertIsNotNone(item)
        self.assertEqual(item['ISBN'], '0439708184')
        self.assertEqual(len(item['authors']), 1)
        self.assertEqual(item['authors'][0], 'J. K. Rowling')
        self.assertEqual(item['genre'], 'fiction')
        self.assertEqual(item['title'], 'Harry Potter and the Sorcerer\'s Stone')
        self.assertEqual(item['pages'], 322)
