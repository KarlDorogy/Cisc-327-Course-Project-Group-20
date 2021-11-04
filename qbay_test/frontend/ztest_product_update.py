from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

class FrontEndCreateProductUpdateTest(BaseCase):

    def test_update_product_r5_2(self, *_):

        # Price can be increased but cannot be decreased (Success)
        # Input partitioning testing of increased price
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "iPhone Five")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 12)
        self.type("#title", "iPhone Five")
        self.type("#new_title", "iPhone Five")
        self.type("#new_description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Price can be increased but cannot be decreased (Failed)
        # Input partitioning testing of decreased price
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 10)
        self.type("#title", "iPhone Five")
        self.type("#new_title", "iPhone Five")
        self.type("#new_description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")


    def test_update_product_r5_1(self, *_):
        # One can update all attributes of the product, except owner_email and last_modified date (Success)
        # Input partitioning testing each accessable attribute
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "iPhone Five")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 11)
        self.type("#title", "iPhone Five")
        self.type("#new_title", "iPhone Five")
        self.type("#new_description", "This is a new description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # One can update all attributes of the product, except owner_email and last_modified date (Success)
        # Input partitioning testing each accessable attribute
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "iPhone Five")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 11)
        self.type("#title", "iPhone Five")
        self.type("#new_title", "New iPhone")
        self.type("#new_description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")


        # One can update all attributes of the product, except owner_email and last_modified date (Success)
        # Input partitioning testing each accessable attribute
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "iPhone Five")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 13)
        self.type("#title", "iPhone Five")
        self.type("#new_title", "iPhone Five")
        self.type("#new_description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")