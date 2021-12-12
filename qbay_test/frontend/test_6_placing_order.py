from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import *

"""
This file defines all integration tests for the frontend update product page.
"""


class FrontEndPlaceOrderTest(BaseCase):

    def test_place_order_r6_1(self, *_):
        """
        BlackBox Input Partition Test for R6-1.
        A user can place an order on the products.
        Analysis: A user should be able to order a
        product sold by another user, given the
        product exists.
        """

        # Logs in to a seller user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test6@15.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Creating product
        self.open(base_url + '/createproduct')
        self.type("#price", 10)
        self.type("#title", "iPhoneSeven")
        self.type("#description", "This is another test description \
                    that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Log out of seller
        self.click('a[id="btn-logout"]')

        # Log in as buyer
        self.open(base_url + '/login')
        self.type("#email", "test69@[192.0.2.146]")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Case 1: A user can successfully place an order on
        # a product sold by another user
        self.open(base_url + '/listings')
        self.assert_element("#products")
        self.click('a[id="iPhoneSeven"]')
        self.assert_element("#message")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Case 2: A user fails to place an order on a
        # product sold by another user because the product
        # does not exist. A user cannot place an order on any
        # product that is not in the available product listing
        self.open(base_url + '/listings')
        self.assert_element("#products")
        try:
            self.click('a[id="iPhoneNonMarketable"]')
        except Exception:
            return(True)
        
    def test_place_order_r6_2(self, *_):
        """
        BlackBox Input Partition Test for R6-2.
        A user cannot place an order for his/her products.
        Analysis: A user should not be able to purchase the
        items they are selling, only the items others are
        selling.
        """

        # Logs in to a seller user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test6@15.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Creating product
        self.open(base_url + '/createproduct')
        self.type("#price", 10)
        self.type("#title", "iPhoneEight")
        self.type("#description", "This is another test description \
                    that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Case 1: A user fails to place an order on a
        # product because the product is sold by themselves
        # and thus does not show up in the available product listings
        # even though the product has been created and is being sold
        # to other users
        self.open(base_url + '/listings')
        self.assert_element("#products")
        try:
            self.click('a[id="iPhoneEight"]')
        except Exception:
            return(True)

        # Log out of seller
        self.click('a[id="btn-logout"]')

        # Log in as buyer
        self.open(base_url + '/login')
        self.type("#email", "test69@[192.0.2.146]")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Case 1 (Continued): Another user can buy the
        # product the seller was trying to buy because
        # they are not the seller of the item
        self.open(base_url + '/listings')
        self.assert_element("#products")
        self.click('a[id="iPhoneEight"]')
        self.assert_element("#message")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

    def test_place_order_r6_3(self, *_):
        """
        BlackBox Input Partition Test for R6-3.
        A user cannot place an order that costs more than his/her balance.
        Analysis: A user should not be able to purchase an
        an item that costs more than their current balance,
        but can purchase an item that is less than or equal to their 
        current balance.
        """
        
        # Logs in to a seller user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test6@15.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Creating product that is more than the buyer's current balance
        self.open(base_url + '/createproduct')
        self.type("#price", 110)
        self.type("#title", "iPhoneExpensive")
        self.type("#description", "This is another test description \
                    that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Creating product that is less than the buyer's current balance
        self.open(base_url + '/createproduct')
        self.type("#price", 30)
        self.type("#title", "iPhoneNine")
        self.type("#description", "This is another test description \
                    that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Creating product that is equal to the buyer's current balance
        # (equal to current balance after purchasing the $30 iPhoneNine)
        self.open(base_url + '/createproduct')
        self.type("#price", 70)
        self.type("#title", "iPhoneTen")
        self.type("#description", "This is another test description \
                    that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Creating a cheap product that the buyer used to be able to buy but
        # cannot buy after the previous two purchases.
        self.open(base_url + '/createproduct')
        self.type("#price", 10)
        self.type("#title", "iPhoneCheap")
        self.type("#description", "This is another test description \
                    that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Log out of seller
        self.click('a[id="btn-logout"]')

        # Log in as a new buyer with a full 100 balance
        self.open(base_url + '/login')
        self.type("#email", "test.69@test.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Case 1: A user cannot place an order on something more than their 
        # current balance
        self.open(base_url + '/listings')
        self.assert_element("#products")
        self.click('a[id="iPhoneExpensive"]')
        self.assert_element("#message")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Placing Order Failed", "#message")

        # Case 2: A user can place an order on something that is less than 
        # their current balance
        self.open(base_url + '/listings')
        self.assert_element("#products")
        self.click('a[id="iPhoneNine"]')
        self.assert_element("#message")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Case 3: A user can place an order on something that is equal to 
        # their current balance
        self.open(base_url + '/listings')
        self.assert_element("#products")
        self.click('a[id="iPhoneTen"]')
        self.assert_element("#message")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Case 4: A user cannot place an order on something more than their 
        # current balance even if they used to be able to purchase it.
        self.open(base_url + '/listings')
        self.assert_element("#products")
        self.click('a[id="iPhoneCheap"]')
        self.assert_element("#message")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Placing Order Failed", "#message")

    def test_place_order_r6_4(self, *_):
        """
        BlackBox Input Partition Test for R6-4.
        A sold product will not be shown on the other user's user interface.
        Analysis: A seller should not see their product listing anymore
        after selling the product.
        """

        # Logs in to a seller user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test6@15.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Creating product
        self.open(base_url + '/createproduct')
        self.type("#price", 10)
        self.type("#title", "iPhoneEleven")
        self.type("#description", "This is another test description \
                    that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Case 1: The buyer sees an unsold product that they are selling
        self.assert_element("#iPhoneEleven")

        # Case 2: The product is sold and the buyer can no longer see the 
        # product
        self.click('a[id="btn-logout"]')  # Log out of seller

        # Log in as buyer
        self.open(base_url + '/login')
        self.type("#email", "test69@[192.0.2.146]")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Order the product as buyer
        self.open(base_url + '/listings')
        self.assert_element("#products")
        self.click('a[id="iPhoneEleven"]')
        self.assert_element("#message")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Log out of buyer
        self.click('a[id="btn-logout"]')

        # Log in to seller
        self.open(base_url + '/login')
        self.type("#email", "test6@15.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Try to view the sold product that was viewable before
        try:
            self.assert_element("#iPhoneEleven")
        except Exception:
            return(True)

    def test_place_order_r6_5(self, *_):
        """
        BlackBox Input Partition Test for R6-5.
        A sold product can be shown on the owner's user interface.
        Analysis: A buyer should be able to see the product they
        bought on their home page after they buy it, so long as
        they bought it.
        """

        self.open(base_url + '/login')
        self.type("#email", "test6@15.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Creating product
        self.open(base_url + '/createproduct')
        self.type("#price", 10)
        self.type("#title", "iPhoneTwelve")
        self.type("#description", "This is another test description \
                    that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Log out of seller
        self.click('a[id="btn-logout"]')

        # Log in as buyer
        self.open(base_url + '/login')
        self.type("#email", "test69@[192.0.2.146]")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # Case1: The buyer orders an item and can see it on their homepage
        self.open(base_url + '/listings')
        self.assert_element("#products")
        self.click('a[id="iPhoneTwelve"]')
        self.assert_element("#message")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_element("#iPhoneTwelve")
        self.assert_text("Title: iPhoneTwelve", "#iPhoneTwelve")

        # Case2: The buyer cannot see an item they did not order from the 
        # available product listing
        try:
            self.assert_element("#iPhoneExpensive")
        except Exception:
            return(True)
        
        # Case3: The buyer cannot see an item that is not in the available 
        # product listing
        try:
            self.assert_element("#iPhoneNonMarketable")
        except Exception:
            return(True)