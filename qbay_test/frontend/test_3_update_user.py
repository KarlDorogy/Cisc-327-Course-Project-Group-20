from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import *

"""
This file defines all integration tests for the frontend update user page.
"""


class FrontEndUpdateUserPageTest(BaseCase):

    def test_update_user_frontend_r3_1(self, *_):
        """
        This is BlackBox Functionality Testing for R3-1:
        Using the updateuser function, a user should only be
        able to update/change their username, shipping address
        and postal code.
        """
        # open login page
        self.open(base_url + '/login')
        # login to a user already in database
        self.type("#email", "test1@r21.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # T1: successfully updates user
        self.open(base_url + '/updateuser')
        self.type("#name", "Sherlock Holmes")
        self.type("#shippingaddress", "221B Baker Street")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        # redirected to home page with updated info but old email
        self.assert_element("#welcome-header")
        self.assert_text("Welcome Sherlock Holmes!", "#welcome-header")
        self.assert_element("#shipping-header")
        self.assert_text("Current Shipping Address: 221B Baker Street", "#shipping-header")
        self.assert_element("#postal-header")
        self.assert_text("Current Postal Code: M1C 8X3", "#postal-header")
        
        # open login page
        self.open(base_url + '/login')
        # login to same account using original email
        self.type("#email", "test1@r21.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

    def test_update_user_frontend_r3_2(self, *_):
        """
        This is BlackBox Input Partition Testing for R3-2:
        The user Shipping address should be non-empty, alphanumeric-only,
        and have no special characters.
        """
        # open login page
        self.open(base_url + '/login')
        # login to a user already in database
        self.type("#email", "test1@r21.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # P1: empty
        self.open(base_url + '/updateuser')
        self.type("#name", "Sherlock Holmes")
        self.type("#shippingaddress", " ")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Updating of User Profile Failed.", "#message")

        # P2: alphanumeric only
        self.open(base_url + '/updateuser')
        self.type("#name", "Sherlock Holmes")
        self.type("#shippingaddress", "best address")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        # redirected to home page with address if update was successful
        self.assert_element("#shipping-header")
        self.assert_text("Current Shipping Address: best address", "#shipping-header")

        # P3: special character
        self.open(base_url + '/updateuser')
        self.type("#name", "Sherlock Holmes")
        self.type("#shippingaddress", "The #1! address")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Updating of User Profile Failed.", "#message")

    def test_update_user_frontend_r3_3(self, *_):
        """
        This is BlackBox Output Testing for R3-3:
        The user postal code must be a valid Canadian postal code.
        """
        # open login page
        self.open(base_url + '/login')
        # login to a user already in database
        self.type("#email", "test1@r21.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Out1: Valid Canadian postal code
        self.open(base_url + '/updateuser')
        self.type("#name", "Sherlock Holmes")
        self.type("#shippingaddress", "The best address")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        # redirected to home page with new postal code on successful update
        self.assert_element("#postal-header")
        self.assert_text("Current Postal Code: M1C 8X3", "#postal-header")

        # Out2: Invalid Canadian postal code
        self.open(base_url + '/updateuser')
        self.type("#name", "Sherlock Holmes")
        self.type("#shippingaddress", "420 The best address")
        self.type("#postalcode", "F1C 8X3")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Updating of User Profile Failed.", "#message")

        # Out3: Valid non-Canadian postal code
        self.open(base_url + '/updateuser')
        self.type("#name", "Sherlock Holmes")
        self.type("#shippingaddress", "420 The best address")
        self.type("#postalcode", "85001")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Updating of User Profile Failed.", "#message")

    def test_update_user_frontend_r3_4(self, *_):
        """
        This is BlackBox Input Test for R3-4:
        The updateuser function/web page should check if 
        the supplied Username meets the same requirements 
        for registration checking: r1-5, r1-6.
        """
        # open login page
        self.open(base_url + '/login')
        # login to a user already in database
        self.type("#email", "test1@r21.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # R1-5 Testing:
        # P1: empty
        self.open(base_url + '/updateuser')
        self.type("#name", " ")
        self.type("#shippingaddress", "Default")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Updating of User Profile Failed.", "#message")

        # P2: not alphanumeric-only, no space
        self.open(base_url + '/updateuser')
        self.type("#name", "@#!]")
        self.type("#shippingaddress", "Default")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Updating of User Profile Failed.", "#message")

        # P3: alphanumeric-only, no space
        self.open(base_url + '/updateuser')
        self.type("#name", "alphanumeric")
        self.type("#shippingaddress", "Default")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        # redirected to home page with new username if update was successful 
        self.assert_element("#welcome-header")
        self.assert_text("Welcome alphanumeric!", "#welcome-header")

        # P4: alphanumeric-only, prefix space
        self.open(base_url + '/updateuser')
        self.type("#name", " alphanumeric")
        self.type("#shippingaddress", "Default")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Updating of User Profile Failed.", "#message")

        # P5: alphanumeric-only, suffix space
        self.open(base_url + '/updateuser')
        self.type("#name", "alphanumeric ")
        self.type("#shippingaddress", "Default")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Updating of User Profile Failed.", "#message")

        # P6: alphanumeric-only, middle space
        self.open(base_url + '/updateuser')
        self.type("#name", "alpha numeric")
        self.type("#shippingaddress", "Default")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Welcome alpha numeric!", "#welcome-header")

        # R1-6 Testing:
        # # T1: less than 2 characters
        self.open(base_url + '/updateuser')
        self.type("#name", "u")
        self.type("#shippingaddress", "Default")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Updating of User Profile Failed.", "#message")

        # # T2: more than 2 characters less than 20 characters
        self.open(base_url + '/updateuser')
        self.type("#name", "user1")
        self.type("#shippingaddress", "Default")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Welcome user1!", "#welcome-header")

        # # T3: more than 20 characters
        self.open(base_url + '/updateuser')
        self.type("#name", "thisusernameismorethan")
        self.type("#shippingaddress", "Default")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Updating of User Profile Failed.", "#message")

        # # T4: 20 characters
        self.open(base_url + '/updateuser')
        self.type("#name", "thisusernamesisexact")
        self.type("#shippingaddress", "Default")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Welcome thisusernamesisexact!", "#welcome-header")

        # # T5: 2 characters
        self.open(base_url + '/updateuser')
        self.type("#name", "u2")
        self.type("#shippingaddress", "Default")
        self.type("#postalcode", "M1C 8X3")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Welcome u2!", "#welcome-header")