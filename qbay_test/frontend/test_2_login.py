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
        # P1: valid dot string email
        self.open(base_url + '/login')
        self.type("#email", "test.69@test.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Welcome GoofyGoober!", "#welcome-header")

        # P2: valid quote string email
        self.open(base_url + '/login')
        self.type("#email", '"test<>69"@test.com')
        self.type("#password", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Welcome GoofyGoober!", "#welcome-header")

        # P3: valid  domain email
        self.open(base_url + '/login')
        self.type("#email", "test6.9@test.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Welcome GoofyGoober!", "#welcome-header")

        # P4: valid IPv4 domain email
        self.open(base_url + '/login')
        self.type("#email", "test69@[192.0.2.146]")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Welcome GoofyGoober!", "#welcome-header")

        # P5: valid IPv6 domain email
        self.open(base_url + '/login')
        self.type("#email", "test69@[2001:db8:3333:4444:5555:6666:7777:8888]")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Welcome GoofyGoober!", "#welcome-header")

        # P6: invalid dot string email
        self.open(base_url + '/login')
        self.type("#email", "test..69@test.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # P7: invalid quote string email
        self.open(base_url + '/login')
        self.type("#email", '""@test.com')
        self.type("#password", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # P8: invalid domain email
        self.open(base_url + '/login')
        self.type("#email", "test69@te-st.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

        # P9: invalid IP domain email
        self.open(base_url + '/login')
        self.type("#email", "test69@[4.2.0:6.9]")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("login failed", "#message")

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