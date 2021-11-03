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