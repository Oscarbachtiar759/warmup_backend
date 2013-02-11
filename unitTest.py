"""
Unit tests for the UsersModel
"""

import unittest
import sys
import os

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "backend.settings"

from LoginCounter.models import UsersModel


class TestUsersModel(unittest.TestCase):
    """
    Unittests for the Users model class
    """
    def setUp(self):
        #self.users = server.UsersModel ()
        #self.users.reset ()
		UsersModel.objects.all().delete()

        
    def testAdd1(self):
        """
        Tests that adding a user works
        """
        self.assertEquals(1, UsersModel.add("user1", "password1"))

    def testAddExists(self):
        """
        Tests that adding a duplicate user name fails
        """
        self.assertEquals(1, UsersModel.add("user1", "password"))
        self.assertEquals(-2, UsersModel.add("user1", "password"))

    def testAdd2(self):
        """
        Tests that adding two users works
        """
        self.assertEquals(1, UsersModel.add("user1", "password"))
        self.assertEquals(1, UsersModel.add("user2", "password"))

    def testAddEmptyUsername(self):
        """
        Tests that adding an user with empty username fails
        """
        self.assertEquals(-3, UsersModel.add("", "password"))
		
    def testLogin1(self):
		"""
		Tests that login after adding a user works and count is properly updated
		"""
		self.assertEquals(1, UsersModel.add("user1", "password"))
		self.assertEquals(2, UsersModel.login("user1", "password"))
    
    def testLogin2(self):
        """
        Tests that login twice after adding a user works and count is properly updated
        """
        self.assertEquals(1, UsersModel.add("user1", "password"))
        self.assertEquals(2, UsersModel.login("user1", "password"))
        self.assertEquals(3, UsersModel.login("user1", "password"))
        
    def testNonExistentLogin(self):
		"""
		Tests that login for a user that doesn't exist fails
		"""
		self.assertEquals(-1, UsersModel.login("user1", "password"))
        
    def testLoginDifferentPassword(self):
		"""
		Tests that login with a different password for the same username fails
		"""
		self.assertEquals(1, UsersModel.add("user1", "password"))
		self.assertEquals(-1, UsersModel.login("user1", "wrong"))
        
    def testLoginDifferentUser(self):
		"""
		Tests that login with different usernames for the same password fails
		"""
		self.assertEquals(1, UsersModel.add("user1", "password"))
		self.assertEquals(-1, UsersModel.login("user2", "password"))        
		
    def testLogin3(self):
        """
        Tests that logging in works for 2 newly created users, and counters properly updated
        """
        self.assertEquals(1, UsersModel.add("user1", "password"))
        self.assertEquals(1, UsersModel.add("user2", "password"))
        self.assertEquals(2, UsersModel.login("user1", "password"))	
        self.assertEquals(2, UsersModel.login("user2", "password"))

    def testLogin4(self):
		"""
		Tests that login with an empty password works
		"""
		self.assertEquals(1, UsersModel.add("user1", ""))
		self.assertEquals(2, UsersModel.login("user1", ""))

# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
