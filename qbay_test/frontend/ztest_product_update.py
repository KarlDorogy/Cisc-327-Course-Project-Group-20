from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

class FrontEndCreateProductUpdateTest(BaseCase):

    def test_update_product_r5_1(self, *_):
        """
        Blackbox Input Partitioning for R5-1.
        One can update all attributes of the product, except owner_email and last_modified date.
        Testing each accessable attribute to showcase owner_email and last_modified date
        are not accessable to be updated.
        """

        # testing if updating the description attribute succeeds
        #Logs in to a user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test4@r16.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')
        
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
        self.type("#new_description", "This is a new description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

    #     # testing if updating the title attribute succeeds


    #     # #Logs in to a user before creating products
    #     # self.open(base_url + '/login')
    #     # self.type("#email", "test4@r16.com")
    #     # self.type("#password", "@Password")
    #     # self.click('input[type="submit"]')

    #     # self.open(base_url + '/createproduct')
    #     # self.type("#price", 11)
    #     # self.type("#title", "iPhone Five")
    #     # self.type("#description", "This is a very long test description that is at least 20 characters long")
    #     # self.click('input[type="submit"]')
    #     # self.assert_element("#welcome-header")
        
    #     self.open(base_url + '/updateproduct')
    #     self.type("#new_price", 11)
    #     self.type("#title", "iPhone Five")
    #     self.type("#new_title", "New iPhone")
    #     self.type("#new_description", "This is a very long test description that is at least 20 characters long")
    #     self.click('input[type="submit"]')
    #     self.assert_element("#welcome-header")

    #     # # testing if updating the price attribute succeeds


    #     # #Logs in to a user before creating products
    #     # self.open(base_url + '/login')
    #     # self.type("#email", "test4@r16.com")
    #     # self.type("#password", "@Password")
    #     # self.click('input[type="submit"]')

    #     # self.open(base_url + '/createproduct')
    #     # self.type("#price", 11)
    #     # self.type("#title", "iPhone Five")
    #     # self.type("#description", "This is a very long test description that is at least 20 characters long")
    #     # self.click('input[type="submit"]')
    #     # self.assert_element("#welcome-header")
        
    #     self.open(base_url + '/updateproduct')
    #     self.type("#new_price", 13)
    #     self.type("#title", "iPhone Five")
    #     self.type("#new_title", "iPhone Five")
    #     self.type("#new_description", "This is a very long test description that is at least 20 characters long")
    #     self.click('input[type="submit"]')
    #     self.assert_element("#welcome-header")


    # def test_update_product_r5_2(self, *_):
    #     """
    #     Blackbox Input Partitioning for R5-2.
    #     Price can be increased but cannot be decreased
    #     """

    #     #Logs in to a user before creating products
    #     self.open(base_url + '/login')
    #     self.type("#email", "test4@r16.com")
    #     self.type("#password", "@Password")
    #     self.click('input[type="submit"]')

    #     # testing if increasing price succeeds
    #     self.open(base_url + '/createproduct')
    #     self.type("#price", 11)
    #     self.type("#title", "iPhone Five")
    #     self.type("#description", "This is a very long test description that is at least 20 characters long")
    #     self.click('input[type="submit"]')
    #     self.assert_element("#welcome-header")
        
    #     self.open(base_url + '/updateproduct')
    #     self.type("#new_price", 12)
    #     self.type("#title", "iPhone Five")
    #     self.type("#new_title", "iPhone Five")
    #     self.type("#new_description", "This is a very long test description that is at least 20 characters long")
    #     self.click('input[type="submit"]')
    #     self.assert_element("#welcome-header")

    #     # testing if decreasing price fails
    #     self.open(base_url + '/updateproduct')
    #     self.type("#new_price", 10)
    #     self.type("#title", "iPhone Five")
    #     self.type("#new_title", "iPhone Five")
    #     self.type("#new_description", "This is a very long test description that is at least 20 characters long")
    #     self.click('input[type="submit"]')
    #     self.assert_element("#welcome-header")