import os
import unittest
from app import app , db
from app.inmates.models import *

class InmateTestCase(unittest.TestCase):

	def setUp(self):
		app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()


    def tearDown(self):
    	db.session.remove()
    	db.drop_all()


'''	
	A test is supposed to run some function of the application that has a known outcome, 
	and should assert if the result is different than the expected one.
'''

    def test_earliest_possible(self):
    	exptected = True
    	x = True
    	assert  x = expected





if __name__ == '__main__:
	unnittest.main()