import unittest
from fake_data_crud_service.core.dao import DAO


class FakeDataCRUDServiceTest(unittest.TestCase):

    def test_create_connection_uri(self):
        dao = DAO('kalimaha', 'Ce09114238', 'ds059145.mongolab.com', '59145', 'kalimadata')
        uri = dao.create_connection_uri()
        self.assertEqual(uri, 'mongodb://kalimaha:Ce09114238@ds059145.mongolab.com:59145/kalimadata')

    def test_get(self):
        dao = DAO('kalimaha', 'Ce09114238', 'ds059145.mongolab.com', '59145', 'kalimadata')
        items = dao.get('books')
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['ISBN'], '0-436-20305-7')
        self.assertEqual(items[0]['author'], 'Howard Marks')
        self.assertEqual(items[0]['genre'], 'non-fiction')
        self.assertEqual(items[0]['title'], 'Mr. Nice')
        self.assertEqual(items[0]['pages'], 466)

    def test_get_by_id(self):
        dao = DAO('kalimaha', 'Ce09114238', 'ds059145.mongolab.com', '59145', 'kalimadata')
        item = dao.get_by_id('books', '56b78893e4b05ba6b4983386')
        self.assertIsNotNone(item)
        self.assertEqual(item['ISBN'], '0-436-20305-7')
        self.assertEqual(item['author'], 'Howard Marks')
        self.assertEqual(item['genre'], 'non-fiction')
        self.assertEqual(item['title'], 'Mr. Nice')
        self.assertEqual(item['pages'], 466)