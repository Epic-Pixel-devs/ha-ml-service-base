# -*- coding: utf-8 -*-
import mock, os, sys
import mongomock
from mongoengine import connect, get_connection


from unittest import TestCase, main


sys.path.append(os.path.abspath(os.getcwd()))
from services.pymongo_service import PymongoService


def inc(x):
    """
    This is an example python test
    """
    return x + 1


class DatabaseTest(TestCase):
    """
    @see: https://docs.mongoengine.org/guide/mongomock.html
    """
    def setUp(self) -> None:
        connect('mongoenginetest',
                host='mongodb://localhost:27017/?uuidRepresentation=standard', 
                mongo_client_class=mongomock.MongoClient, 
                alias='testdb')
        
        self.mock = mock.Mock()
        self.conn = get_connection('testdb')

        return super().setUp()
    
    def test_should_be_four(self):
        """
        This is an example python test - the method 'should_be_four' should be have the result four
        """
        assert 4 == inc(3)
    

    @mock.patch('services.pymongo_service.PymongoService')
    def test_should_be_not_null_when_call_health(self, pymongo_service):
       """
       @see: https://stackoverflow.com/questions/24617397/how-do-i-print-to-console-in-pytest
       """
       self.assertIsNotNone(pymongo_service)
       self.assertIsNotNone(PymongoService().get_mongo_client().admin.command('ping'))


if __name__ == '__main__':
    main()
