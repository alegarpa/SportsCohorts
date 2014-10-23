"""
Each file that starts with test... in this directory is scanned for subclasses of unittest.TestCase or testLib.RestTestCase
"""

import unittest
import os
import testLib
from users.models import FriendRequest

class TestUserProfile(testLib.RestTestCase):
    """Testing UserProfile"""
    testDict = {"username": "JD", "password":"123456", "email":"JD@example.com",
                "firstName": "John", "lastName": "Doe", "friend": "Jim"}

    def assertResponse(self, respData, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        self.assertDictEqual(expected, respData)

    def testRegister(self):
        """
        Tests adding a user.
        """
        respData = self.makeRequest("/user/register", method="POST", data = TestUserProfile.testDict )
        self.assertResponse(respData)

    def testRegisterLongUsername(self):
        """
        Test that giving a long (> 128 char) username will return INVALID_USERNAME 
        error.
        """
        goodUsername = "A" * testLib.RestTestCase.MAX_USERNAME_LENGTH
        badUsername = goodUsername + "A"
        newDict = self.testDict.copy()
        
        newDict["username"] = goodUsername
        respData = self.makeRequest("/user/register", method="POST", data = newDict )
        self.assertResponse(respData)
        

        newDict["username"] = badUsername
        respData = self.makeRequest("/user/register", method="POST", data = newDict )
        self.assertResponse(respData, errCode=testLib.RestTestCase.INVALID_USERNAME)

    def testRegisterEmptyUsername(self):
        """
        Test that giving an empty username will return INVALID_USERNAME error.
        """
        newDict = self.testDict.copy()
        newDict["username"] = ""
        respData = self.makeRequest("/user/register", method="POST", data = newDict )
        self.assertResponse(respData, errCode=testLib.RestTestCase.INVALID_USERNAME)


    def testRegisterExistingUsername(self):
        """
        Tests registering the same user will return USER_EXISTS error.
        """
        self.makeRequest("/user/register", method="POST", data = TestUserProfile.testDict)
        respData = self.makeRequest("/user/register", method="POST", data = TestUserProfile.testDict)
        self.assertResponse(respData, errCode=testLib.RestTestCase.USER_EXISTS)

    def testRegisterLongPassword(self):
        """
        Tests that giving a long (> 128 char) password will return INVALID_PASSWORD
        """
        longPassword = "A" * 129
        newDict = self.testDict.copy()
        newDict["password"] = longPassword
        respData = self.makeRequest("/user/register", method="POST", data = newDict )
        self.assertResponse(respData, errCode=testLib.RestTestCase.INVALID_PASSWORD)

    def testLoginSuccess(self):
        """
        Tests login in a user.
        """
        self.makeRequest("/user/register", method="POST", data = TestUserProfile.testDict )
        respData = self.makeRequest("/user/login", method="POST", data = TestUserProfile.testDict )
        self.assertResponse(respData)

    def testLoginBadUsername(self):
        """
        Tests that you cannot login in with a non-exitance username/user.
        """
        respData = self.makeRequest("/user/login", method="POST", data = TestUserProfile.testDict )
        self.assertResponse(respData, errCode=testLib.RestTestCase.INVALID_CREDENTIALS)

    def testLoginBadPassword(self):
        """
        Tests that you cannot login in with an incorrect password.
        """
        self.makeRequest("/user/register", method="POST", data = TestUserProfile.testDict )
        newDict = self.testDict.copy()
        newDict["password"] = "WRONG_PW"
        respData = self.makeRequest("/user/login", method="POST", data = newDict )
        self.assertResponse(respData, errCode=testLib.RestTestCase.INVALID_CREDENTIALS)


    def testFriendRequest(self):
        """
        Tests the ability to send a friend request. 
        """
        newDict = {"username": "Jim", "password": "PW", "email": "Jim@example.com"}
        self.makeRequest("/user/register", method="POST", data = TestUserProfile.testDict )
        self.makeRequest("/user/register", method="POST", data = newDict )
        respData = self.makeRequest("/user/requestFriend", method="POST", data = TestUserProfile.testDict )
        self.assertResponse(respData)



    def BROKENATMtestLoginBeforeAdd(self):
        """
        Tests that an error returns if you try to login as an unregistered user
        """
        respData = self.makeRequest("/users/login/", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        self.assertResponse(respData, count=None, errCode=testLib.RestTestCase.ERR_BAD_CREDENTIALS)