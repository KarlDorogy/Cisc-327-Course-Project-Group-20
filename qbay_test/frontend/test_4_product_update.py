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
        Blackbox Input Partitioning for R5-1.
        One can update all attributes of the product, except owner_email
        and last_modified date. Testing each accessable attribute to 
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
        Blackbox Input Partitioning for R5-2.
        Price can be increased but cannot be decreased
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
        Whitebox testing for R5-3.
        Last_modified_date should be updated when the update operation 
        is successful.
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

        # Testing if modified_date is updated
        self.open(base_url + '/updateproduct')
        self.type("#new_price", 30)
        self.type("#title", "iPhone Seven")
        self.type("#new_title", "iPhone Seven")
        self.type("#new_description", "This is another test description \
                  that is at least 20 characters long")
        self.click('input[type="submit"]')

        # The last modified date of the product.
        last_modified_date = db.Column(db.String(10), unique=False, nullable=False)


        product_list = Product.query.filter_by(title="#title").all()

        # Updates every existing product object to new inputed values 
        for existed_product in product_list:

            existed_product.description = "#new_description"
            existed_product.title = "#new_title"
            # Checks if the new price is greater than the old price
            if(existed_product.price > "#new_price"):
                return False
            existed_product.price = "#new_price"
            
            # Gets the current last modified date
            last_date = existed_product.last_modified_date

            # Sets the last modified date to current date
            today = date.today()
            current_date = today.strftime("%d/%m/%Y")
            # existed_product.last_modified_date = current_date[6:10] + \
            #     "-" + current_date[3:5] + "-" + current_date[0:3]


            
            if(last_date == current_date):
                self.assert_element("#welcome-header")
            else:
                self.assert_element("#message")
                self.assert_text("Product Update Failed", "#message")

            db.session.add(existed_product)
            db.session.commit()




            #R5-4 check if attributes had the same properties as defined in R4, input partitioning testing failure for having description be too short, having two of same title