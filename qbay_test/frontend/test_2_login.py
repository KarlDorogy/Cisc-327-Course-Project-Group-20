from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import *

"""
This file defines all integration tests for the frontend login page.
"""


class FrontEndLoginPageTest(BaseCase):

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

    def test_login__frontend_r2_2(self, *_):
        """
        This is BlackBox Input Test for R2-2:
        The login function should check if the supplied inputs
        meet the same email/password requirements for registration
        Checking: r1-1, r1-3, r1-4.
        """

        # R1-1 Testing:
        # P1: email empty
        self.open(base_url + '/login')
        self.type("#email", " ")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # P2 password empty
        self.open(base_url + '/login')
        self.type("#email", "partition2@r11.com")
        self.type("#password", " ")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # P3 both email & password empty
        self.open(base_url + '/login')
        self.type("#email", " ")
        self.type("#password", " ")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # P4 both email & password filled
        self.open(base_url + '/login')
        self.type("#email", "partition4@r11.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # If P4 registration was successful user is redirected to home page
        # with a messege of "Welcome "
        self.assert_element("#welcome-header")
        self.assert_text("Welcome u4!", "#welcome-header")

        # R1-3 Testing:
        # (GOES HERE)

        # R1-4 Testing:
        # P1: lowercase, less than 6 chars, no uppercase, no special char
        self.open(base_url + '/login')
        self.type("#email", "test1@14.com")
        self.type("#password", "five")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # P2: lowercase, greater than 6 chars, no uppercase, no special char
        self.open(base_url + '/login')
        self.type("#email", "test2@14.com")
        self.type("#password", "badpassword")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # P3: lowercase, greater than 6 chars, uppercase, no special char
        self.open(base_url + '/login')
        self.type("#email", "test3@14.com")
        self.type("#password", "Badpassword")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # P4: lowercase, greater than 6 chars, uppercase, special char
        self.open(base_url + '/login')
        self.type("#email", "test4@14.com")
        self.type("#password", "@Goodpassword")
        self.click('input[type="submit"]')
        # If P4 registration was successful user is redirected to home page
        # with a messege of "Welcome "
        self.assert_element("#welcome-header")
        self.assert_text("Welcome u0!", "#welcome-header")

        # P5: no lowercase, greater than 6 chars, uppercase, special char
        self.open(base_url + '/login')
        self.type("#email", "test5@14.com")
        self.type("#password", "@BADPASSWORD")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("login failed", "#message")