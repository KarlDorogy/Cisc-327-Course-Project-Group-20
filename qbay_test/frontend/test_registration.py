from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import *

"""
This file defines all integration tests for the frontend homepage.
"""


class FrontEndHomePageTest(BaseCase):

    def test_register_success(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """

        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "test0@test.com")
        self.type("#name", "u0")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        # click enter button
        self.click('input[type="submit"]')
        
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test0@test.com")
        self.type("#password", "@Password")
        # click enter button
        self.click('input[type="submit"]')

        # after clicking on the browser (the line above)
        # the front-end code is activated
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics.
        # so we patch the backend to return a specific user instance,
        # rather than running that program. (see @ annotations above)

        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome u0!", "#welcome-header")
        # other available APIs

    def test_login_success(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # register user for login frontend login test to use
        register("Karl Dorogy", "test1@test.com", "@Password")

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test1@test.com")
        self.type("#password", "@Password")
        # click enter button
        self.click('input[type="submit"]')

        # after clicking on the browser (the line above)
        # the front-end code is activated
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics.
        # so we patch the backend to return a specific user instance,
        # rather than running that program. (see @ annotations above)

        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome Karl Dorogy!", "#welcome-header")
        # other available APIs