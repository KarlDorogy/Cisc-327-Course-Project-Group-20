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
        self.type("#email", "test2@email.com")
        self.type("#name", "u0")
        self.type("#password", " ")
        self.type("#password2", " ")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P3 both email & password empty
        self.open(base_url + '/register')
        self.type("#email", " ")
        self.type("#name", "u0")
        self.type("#password", " ")
        self.type("#password2", " ")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P4 both email & password filled
        self.open(base_url + '/register')
        self.type("#email", "test0@test.com")
        self.type("#name", "u0")
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

    def test_register_frontend_r1_9(self, *_):
        """
        This is BlackBox Functionality Test for R1-9.
        Users postal code is empty upon registration
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

        self.type("#email", "test3@test.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        self.assert_element("#message")



        
    
    def test_login_success(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # register new user for frontend login test to use
        register("u1", "test1@test.com", "@Password")

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
        self.assert_text("Welcome u1!", "#welcome-header")
        # other available APIs