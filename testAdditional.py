"""
Each file that starts with test... in this directory is scanned for subclasses of unittest.TestCase or testLib.RestTestCase
"""

import unittest
import os
import testLib

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "backend.settings"

class TestAddUser2(testLib.RestTestCase):
    """Test adding the same user twice"""
    def assertResponse(self, respData, count=1, errCode=testLib.RestTestCase.SUCCESS):
        """
        Check that response data dictionary matches expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count'] = count
        self.assertDictEqual(expected, respData)
        
    def testAdd2(self):
        respData = self.makeRequest("/users/add", method="POST", data = {'user' : 'user1', 'password' : 'password'})
        self.assertResponse(respData, count=1)
        respData = self.makeRequest("/users/add", method="POST", data = {'user' : 'user1', 'password' : 'blah'})
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_USER_EXISTS)

class TestAddUser3(testLib.RestTestCase):
    """Test adding two different"""
    def assertResponse(self, respData, count=1, errCode=testLib.RestTestCase.SUCCESS):
        """
        Check that response data dictionary matches expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count'] = count
        self.assertDictEqual(expected, respData)
        
    def testAdd3(self):
        respData = self.makeRequest("/users/add", method="POST", data = {'user' : 'user1', 'password' : 'password'})
        self.assertResponse(respData, count=1)
        respData = self.makeRequest("/users/add", method="POST", data = {'user' : 'user2', 'password' : 'password'})
        self.assertResponse(respData, count=1)   
        
class TestLoginUser(testLib.RestTestCase):
    """Test logging in to a non-existent user"""
    def assertResponse(self, respData, count=1, errCode=testLib.RestTestCase.SUCCESS):
        """
        Check that response data dictionary matches expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count'] = count
        self.assertDictEqual(expected, respData)
        
    def testLogin(self):
        respData = self.makeRequest("/users/login", method="POST", data = {'user' : 'user1', 'password' : 'password'})
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_CREDENTIALS)
        
class TestLoginUser2(testLib.RestTestCase):
    """Test logging in to an existing user"""
    def assertResponse(self, respData, count=1, errCode=testLib.RestTestCase.SUCCESS):
        """
        Check that response data dictionary matches expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count'] = count
        self.assertDictEqual(expected, respData)
        
    def testLogin(self):
        respData = self.makeRequest("/users/add", method="POST", data = {'user' : 'user1', 'password' : 'password'})
        self.assertResponse(respData, count=1)
        respData = self.makeRequest("/users/login", method="POST", data = {'user' : 'user1', 'password' : 'password'})
        self.assertResponse(respData, count=2)
        
class TestLoginUser3(testLib.RestTestCase):
    """Test logging in to an existing user multiple times"""
    def assertResponse(self, respData, count=1, errCode=testLib.RestTestCase.SUCCESS):
        """
        Check that response data dictionary matches expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count'] = count
        self.assertDictEqual(expected, respData)
        
    def testLogin(self):
        respData = self.makeRequest("/users/add", method="POST", data = {'user' : 'user1', 'password' : 'password'})
        self.assertResponse(respData, count=1)
        respData = self.makeRequest("/users/login", method="POST", data = {'user' : 'user1', 'password' : 'password'})
        self.assertResponse(respData, count=2)
        respData = self.makeRequest("/users/login", method="POST", data = {'user' : 'user1', 'password' : 'password'})
        self.assertResponse(respData, count=3)
        respData = self.makeRequest("/users/login", method="POST", data = {'user' : 'user1', 'password' : 'password'})
        self.assertResponse(respData, count=4)

class TestLoginUser4(testLib.RestTestCase):
    """Test logging in to an existing user with a different password"""
    def assertResponse(self, respData, count=1, errCode=testLib.RestTestCase.SUCCESS):
        """
        Check that response data dictionary matches expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count'] = count
        self.assertDictEqual(expected, respData)
        
    def testLogin(self):
        respData = self.makeRequest("/users/add", method="POST", data = {'user' : 'user1', 'password' : 'password'})
        self.assertResponse(respData, count=1)
        respData = self.makeRequest("/users/login", method="POST", data = {'user' : 'user1', 'password' : 'wrong'})
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_CREDENTIALS)
        
class TestLoginUser5(testLib.RestTestCase):
    """Test logging in to two existing users"""
    def assertResponse(self, respData, count=1, errCode=testLib.RestTestCase.SUCCESS):
        """
        Check that response data dictionary matches expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count'] = count
        self.assertDictEqual(expected, respData)
        
    def testLogin(self):
        respData = self.makeRequest("/users/add", method="POST", data = {'user' : 'user1', 'password' : 'password'})
        self.assertResponse(respData, count=1)
        respData = self.makeRequest("/users/login", method="POST", data = {'user' : 'user1', 'password' : 'password'})
        self.assertResponse(respData, 2)
        respData = self.makeRequest("/users/add", method="POST", data = {'user' : 'user2', 'password' : 'password'})
        self.assertResponse(respData, count=1)
        respData = self.makeRequest("/users/login", method="POST", data = {'user' : 'user2', 'password' : 'password'})
        self.assertResponse(respData, 2)