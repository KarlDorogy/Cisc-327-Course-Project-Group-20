from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import *

"""
This file defines all integration tests for the frontend registerpage.
"""


class FrontEndRegisterPageTest(BaseCase):

    def test_register_frontend_r1_1(self, *_):
        """
        BlackBox Input Partition Test for R1-1.
        Both the email and password cannot be empty
        Analysis: So if either email or password are empty 
        then user registration should fail.
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
        This is BlackBox Functionality Test for R1-2.
        Users are uniquely identified by his/her email address
        """

        # T1: valid email (not already in database)
        self.open(base_url + '/register')
        self.type("#email", "test69@test.com")
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # T2: invalid email (already in database)
        self.open(base_url + '/register')
        self.type("#email", "test69@test.com")
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

    def test_register_frontend_r1_3(self, *_):
        """
        This is BlackBox Input Partition Testing for R1-3.
        Emails used to create accounts must follow RFC 5322
        guidelines.
        """

        # P1: valid dot string email
        self.open(base_url + '/register')
        self.type("#email", "test.69@test.com")
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # P2: valid quote string email
        self.open(base_url + '/register')
        self.type("#email", '"test<>69"@test.com')
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # P3: valid  domain email
        self.open(base_url + '/register')
        self.type("#email", "test6.9@test.com")
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # P4: valid IPv4 domain email
        self.open(base_url + '/register')
        self.type("#email", "test69@[192.0.2.146]")
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # P5: valid IPv6 domain email
        self.open(base_url + '/register')
        self.type("#email", "test69@[2001:db8:3333:4444:5555:6666:7777:8888]")
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # P6: invalid dot string email
        self.open(base_url + '/register')
        self.type("#email", "test..69@test.com")
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P7: invalid quote string email
        self.open(base_url + '/register')
        self.type("#email", '""@test.com')
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P8: invalid domain email
        self.open(base_url + '/register')
        self.type("#email", "test69@te-st.com")
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P9: invalid IP domain email
        self.open(base_url + '/register')
        self.type("#email", "test69@[4.2.0:6.9]")
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")
    
    def test_register_frontend_r1_4(self, *_):
        """
        BlackBox Input Parition Test for R1-4. 
        Password has to meet the required complexity: 
        minimum length 6, at least one upper case, at least one 
        lower case, and at least one special character.
        """

        # P1: lowercase, less than 6 chars, no uppercase, no special char
        self.open(base_url + '/register')
        self.type("#email", "test1@14.com")
        self.type("#name", "u0")
        self.type("#password", "five")
        self.type("#password2", "five")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P2: lowercase, greater than 6 chars, no uppercase, no special char
        self.open(base_url + '/register')
        self.type("#email", "test2@14.com")
        self.type("#name", "u0")
        self.type("#password", "badpassword")
        self.type("#password2", "badpassword")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P3: lowercase, greater than 6 chars, uppercase, no special char
        self.open(base_url + '/register')
        self.type("#email", "test3@14.com")
        self.type("#name", "u0")
        self.type("#password", "Badpassword")
        self.type("#password2", "Badpassword")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P4: lowercase, greater than 6 chars, uppercase, special char
        self.open(base_url + '/register')
        self.type("#email", "test4@14.com")
        self.type("#name", "u0")
        self.type("#password", "@Goodpassword")
        self.type("#password2", "@Goodpassword")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # P5: no lowercase, greater than 6 chars, uppercase, special char
        self.open(base_url + '/register')
        self.type("#email", "test5@14.com")
        self.type("#name", "u0")
        self.type("#password", "@BADPASSWORD")
        self.type("#password2", "@BADPASSWORD")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

    def test_register_frontend_r1_5(self, *_):
        """
        BlackBox Input Parition Test for R1-5. 
        User name has to be non-empty, alphanumeric-only, 
        and space allowed only if it is not as the prefix or suffix.
        """
        # P1: empty
        self.open(base_url + '/register')
        self.type("#email", "test1@15.com")
        self.type("#name", " ")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P2: not alphanumeric-only, no space
        self.open(base_url + '/register')
        self.type("#email", "test2@15.com")
        self.type("#name", "@#!]")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P3: alphanumeric-only, no space
        self.open(base_url + '/register')
        self.type("#email", "test3@15.com")
        self.type("#name", "alphanumeric")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        # redirected to login page if registration is successful 
        self.assert_element("#message")
        self.assert_text('Please login', "#message")

        # P4: alphanumeric-only, prefix space
        self.open(base_url + '/register')
        self.type("#email", "test4@15.com")
        self.type("#name", " alphanumeric")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P5: alphanumeric-only, suffix space
        self.open(base_url + '/register')
        self.type("#email", "test5@15.com")
        self.type("#name", "alphanumeric ")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P6: alphanumeric-only, middle space
        self.open(base_url + '/register')
        self.type("#email", "test6@15.com")
        self.type("#name", "alpha numeric")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text('Please login', "#message")
        
    def test_register_frontend_r1_6(self, *_):
        """
        BlackBox Input Boundary/Paritioning Test for R1-6. 
        User name has to be longer than 2 characters 
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
        # If T2 registration was successful user is redirected to login page
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

    def test_register_frontend_r1_7(self, *_):
        """
        BlackBox Ouput Partition Test for R1-7.
        Users are uniquely identified by his/her email address
        Output that the operation failed if the email has 
        already been used/registered. 
        """

        # P1: output registration failed using already in database email
        self.open(base_url + '/register')
        self.type("#email", "test69@test.com")
        self.type("#name", "GoofyGoober")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Registration Failed.", "#message")

        # P2: output registration successful using new email
        self.open(base_url + '/register')
        self.type("#email", "test2@r17.com")
        self.type("#name", "GoofyGoober2")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')
        # redirected to login page if registration is successful 
        self.assert_element("#message")
        self.assert_text('Please login', "#message")

    def test_register_frontend_r1_8(self, *_):
        """
        This is BlackBox Functionality Testing for R1-8.
        Shipping addrss must be empty (only) in the case 
        when a user just registered a new account.
        """

        # T1: register new user and check shipping address is empty
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

        # T1: register new user and check postal code is empty
        self.open(base_url + '/register')
        self.type("#email", "test1@r19.com")
        self.type("#name", "userpostal")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')

        self.open(base_url + '/login')
        self.type("#email", "test1@r19.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        self.open(base_url)
        self.assert_element("#postal-header")
        self.assert_text("None", "#postal-header")

    def test_register_frontend_r1_10(self, *_):
        """
        This is BlackBox Functionality Test for R1-10.
        Checks Balance should be initialized as 100 at 
        the time of registration.
        """
        # P1: register new user and check balance is initialized to 100
        self.open(base_url + '/register')
        self.type("#email", "test1@r110.com")
        self.type("#name", "userbalance")
        self.type("#password", "@Password")
        self.type("#password2", "@Password")
        self.click('input[type="submit"]')

        self.open(base_url + '/login')
        self.type("#email", "test1@r110.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        self.open(base_url)
        self.assert_element("#balance-header")
        self.assert_text("User Balance: 100.0", "#balance-header")