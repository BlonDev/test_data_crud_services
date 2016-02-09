import unittest
from fake_data_crud_service.core.dao import DAO


class FakeDataCRUDServiceTest(unittest.TestCase):

    def test_create_connection_uri(self):
        dao = DAO('kalimaha', 'Ce09114238', 'ds059145.mongolab.com', '59145', 'kalimadata')
        uri = dao.create_connection_uri()
        self.assertEqual(uri, 'mongodb://kalimaha:Ce09114238@ds059145.mongolab.com:59145/kalimadata')
