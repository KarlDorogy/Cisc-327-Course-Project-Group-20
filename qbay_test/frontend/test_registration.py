from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import *

"""
This file defines all integration tests for the frontend homepage.
"""


class FrontEndHomePageTest(BaseCase):

    def test_register_frontend_r1_1(self, *_):
        """
        This is BlackBox Input Partition Test for R1-1.
        Both the email and password cannot be empty
        """

        # P1: email empty
        self.open(base_url + '/register')
        self.type("#email", " ")
        self.type("#name", "u0")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P2 password empty
        self.open(base_url + '/register')
        self.type("#email", "partition2@r11.com")
        self.type("#name", "u2")
        self.type("#password", " ")
        self.type("#password2", " ")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P3 both email & password empty
        self.open(base_url + '/register')
        self.type("#email", " ")
        self.type("#name", "u3")
        self.type("#password", " ")
        self.type("#password2", " ")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P4 both email & password filled
        self.open(base_url + '/register')
        self.type("#email", "partition4@r11.com")
        self.type("#name", "u4")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')

        # If P4 registration was successful user is redirected to login page
        # with a messege of "Please login"
        self.assert_element("#message")
        self.assert_text('Please login', "#message")

    def test_register_frontend_r1_2(self, *_):
        """
        This is BlackBox Input Partition Test for R1-2.
        Users are uniquely identified by his/her email address
        """

        # P1: valid email (not already in database)
        self.open(base_url + '/register')
        self.type("#email", "test69@test.com")
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Please login.", "#message")

        # P2: invalid email (already in database)
        self.open(base_url + '/register')
        self.type("#email", "test69@test.com")
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")
     
    
    def test_register_frontend_r1_6(self, *_):
        """
        This is BlackBox Input Boundary/Paritioning Testing 
        for R1-6. User name has to be longer than 2 characters 
        and less than 20 characters.
        """

        # # T1: less than 2 characters
        self.open(base_url + '/register')
        self.type("#email", "test1@r16.com")
        self.type("#name", "u")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # # T2: more than 2 characters less than 20 characters
        self.open(base_url + '/register')
        self.type("#email", "test2@r16.com")
        self.type("#name", "user1")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        # If P4 registration was successful user is redirected to login page
        # with a messege of "Please login"
        self.assert_element("#message")
        self.assert_text('Please login', "#message")

        # # T3: more than 20 characters
        self.open(base_url + '/register')
        self.type("#email", "test3@r16.com")
        self.type("#name", "thisusernameismorethan")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # # T4: 20 characters
        self.open(base_url + '/register')
        self.type("#email", "test4@r16.com")
        self.type("#name", "thisusernamesisexact")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text('Please login', "#message")

        # # T5: 2 characters
        self.open(base_url + '/register')
        self.type("#email", "test5@r16.com")
        self.type("#name", "u2")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text('Please login', "#message")

    def test_register_frontend_r1_8(self, *_):
        """
        This is BlackBox Functionality Testing for R1-8.
        Shipping addrss must be empty (only) in the case when a
        user just registered a new account.
        """

        # T1: new user account registration
        self.open(base_url + '/register')
        self.type("#email", "test1@r18.com")
        self.type("#name", "u0")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')

        self.open(base_url + '/login')
        self.type("#email", "test1@r18.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        self.open(base_url)
        self.assert_element("#shipping-header")
        self.assert_text("None", "#shipping-header")

    def test_register_frontend_r1_9(self, *_):
        """
        This is BlackBox Functionality Test for R1-9.
        Checks users postal code is empty upon registration.
        """

        # P1: register new user and check postal code is empty
        self.open(base_url + '/register')
        self.type("#email", "test3@test.com")
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Please login.", "#message")

        self.open(base_url + '/login')
        self.type("#email", "test3@test.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        self.open(base_url)
        self.assert_element("#postal-header")
        self.assert_text("None", "#postal-header")