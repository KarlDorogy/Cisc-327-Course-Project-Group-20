from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import *

"""
This file defines all integration tests for the frontend update product page.
"""


class FrontEndCreateProductUpdateTest(BaseCase):

    def test_update_product_r5_1(self, *_):
        """
        Blackbox functionality testing for R5-1.
        One can update all attributes of the product, except owner_email
        and last_modified date.
        Testing each accessable attribute to 
        showcase owner_email and last_modified date are not accessable to
        be updated.
        """

        # Logs in to a user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test4@r16.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')
        
        # Creates product
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "iPhone Five")
        self.type("#description", "This is a very long test description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        
        # Testing if updating the description attribute succeeds
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 11)
        self.type("#title", "iPhone Five")
        self.type("#new_title", "iPhone Five")
        self.type("#new_description", "This is a new description that is \
                  at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # testing if updating the title attribute succeeds
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 11)
        self.type("#title", "iPhone Five")
        self.type("#new_title", "New iPhone")
        self.type("#new_description", "This is a new description that is \
                  at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        
        # testing if updating the price attribute succeeds
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 13)
        self.type("#title", "New iPhone")
        self.type("#new_title", "New iPhone")
        self.type("#new_description", "This is a new description that is \
                  at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

    def test_update_product_r5_2(self, *_):
        """
        Blackbox input partitioning for R5-2.
        Price can be increased but cannot be decreased.
        Testing increasing and testing decreasing price.
        """

        # Logs in to a user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test4@r16.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Creating product
        self.open(base_url + '/createproduct')
        self.type("#price", 20)
        self.type("#title", "iPhone Six")
        self.type("#description", "This is a different test description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        
        # Testing if increasing price succeeds
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 22)
        self.type("#title", "iPhone Six")
        self.type("#new_title", "iPhone Six")
        self.type("#new_description", "This is a different test description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Testing if decreasing price fails
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 18)
        self.type("#title", "iPhone Six")
        self.type("#new_title", "iPhone Six")
        self.type("#new_description", "This is a different test description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Update Failed", "#message")

    def test_update_product_r5_3(self, *_):
        """
        Blackbox exhaustive output testing for R5-3.
        Last_modified_date should be updated when the update operation 
        is successful.
        Exhaustive testing every case for last_modified_date's updatation
        when the update operation is successful.
        Last_modified_date will always update when the product updates,
        unless the python code itself breaks, changing any attribute
        will not break the function that updates the date.
        """

        # Logs in to a user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test4@r16.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Creating product
        self.open(base_url + '/createproduct')
        self.type("#price", 30)
        self.type("#title", "iPhone Seven")
        self.type("#description", "This is another test description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Case 1: last_modified_date is updated after successful update
        # operation
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 32)
        self.type("#title", "iPhone Seven")
        self.type("#new_title", "iPhone Seven")
        self.type("#new_description", "This is another test description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Case 2: last_modified_date is not updated due to unsuccessful update
        # operation
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 28)
        self.type("#title", "iPhone Seven")
        self.type("#new_title", "iPhone Seven")
        self.type("#new_description", "This is another test description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Update Failed", "#message")

    def test_update_product_r5_4(self, *_):
        """
        Blackbox functionality testing for R5-4.
        When updating an attribute, one has to make sure that it follows
        the same requirements as R4.
        Testing each attribute for a success and fail case due to R4.
        """

        # Logs in to a user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test4@r16.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Creating product
        self.open(base_url + '/createproduct')
        self.type("#price", 40)
        self.type("#title", "iPhone Eight")
        self.type("#description", "This is a final test description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        
        # Testing if the requirements from R4 apply when 
        # updating the description requirement.
        # From R4 the description must be a minimum length of 20
        # characters and a maximum of 2000 and longer than the product's
        # title. 
        # Case 1: description successfully meets the requirements
        # from R4 and is updated.
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 40)
        self.type("#title", "iPhone Eight")
        self.type("#new_title", "iPhone Eight")
        self.type("#new_description", "This is a new final description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Case 2: description fails to meets the requirements
        # from R4 and is not updated.
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 40)
        self.type("#title", "iPhone Eight")
        self.type("#new_title", "iPhone Eight")
        self.type("#new_description", "New under 20")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Update Failed", "#message")

        # Testing if the requirements from R4 apply when
        # updating the title requirement.
        # From R4 the title of the product has to be alphanumeric-only,
        # and space allowed if it is not as prefix and suffix, the
        # title is no longer than 80 characters, and cannot share
        # titles with any other product.
        # Case 1: title successfully meets the requirements
        # from both R4 and is updated.
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 40)
        self.type("#title", "iPhone Eight")
        self.type("#new_title", "New iPhone Eight")
        self.type("#new_description", "This is a new final description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # # Case 2: title fails to meets the requirements
        # # from R4 and is not updated.
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 40)
        self.type("#title", "New iPhone Eight")
        self.type("#new_title", "New iPhone @")
        self.type("#new_description", "This is a new final description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Update Failed", "#message")

        # Testing if the requirements from R4 apply when
        # updating the price requirement.
        # From R4 the price has to be greater than 10 and
        # less than 10000
        # Case 1: price successfully meets the requirements
        # from R4 and is updated.
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 42)
        self.type("#title", "New iPhone Eight")
        self.type("#new_title", "New iPhone Eight")
        self.type("#new_description", "This is a new final description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Case 2: price fails to meet the requirements
        # from R4 and is not updated.
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 10002)
        self.type("#title", "New iPhone Eight")
        self.type("#new_title", "New iPhone Eight")
        self.type("#new_description", "This is a new final description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Update Failed", "#message")
        