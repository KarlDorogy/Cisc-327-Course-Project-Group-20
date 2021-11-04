from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import *

"""
This file defines all integration tests for the frontend homepage.
"""


class FrontEndHomePageTest(BaseCase):

    def test_login__frontend_r2_1(self, *_):
        """
        This is BlackBox Functionality Testing for R2-1:
        A user can log in using her/his email address and the password.
        """
        # register new user for frontend login test to use
        self.open(base_url + '/register')
        self.type("#email", "test1@r21.com")
        self.type("#name", "u0")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test1@r21.com")
        self.type("#password", "@Password")
        # click enter button
        self.click('input[type="submit"]')

        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome u0!", "#welcome-header")
