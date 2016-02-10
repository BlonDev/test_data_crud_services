import unittest
from fake_data_crud_service.core.dao import get_dao
from fake_data_crud_service.config.settings import test as t
from fake_data_crud_service.config.settings import production as p


class FakeDataCRUDServiceTest(unittest.TestCase):

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

    def test_get(self):
        dao = get_dao('test')
        items = dao.get('books')
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['ISBN'], '0-436-20305-7')
        self.assertEqual(items[0]['author'], 'Howard Marks')
        self.assertEqual(items[0]['genre'], 'non-fiction')
        self.assertEqual(items[0]['title'], 'Mr. Nice')
        self.assertEqual(items[0]['pages'], 466)

    def test_get_by_id(self):
        dao = get_dao('test')
        item = dao.get_by_id('books', '56b78893e4b05ba6b4983386')
        self.assertIsNotNone(item)
        self.assertEqual(item['ISBN'], '0-436-20305-7')
        self.assertEqual(item['author'], 'Howard Marks')
        self.assertEqual(item['genre'], 'non-fiction')
        self.assertEqual(item['title'], 'Mr. Nice')
        self.assertEqual(item['pages'], 466)
