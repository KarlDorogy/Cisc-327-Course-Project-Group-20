from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User



class FrontEndCreateProductTest(BaseCase):


    def test_create_product_r4_5(self, *_):
        #Logs in to a user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test4@r16.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        #R4-5 Price has to be of range [10, 10000].

        #Input Boundary Testing
        #P1 Price has to be at least 10 (Success)
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "ProductR51")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        #P1 Price has to be at least 10 (Failed)
        self.open(base_url + '/createproduct')
        self.type("#price", 9)
        self.type("#title", "ProductR52")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Creation Failed", "#message")

        #P2 Price has to be below 10000 (Success)

        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "ProductR53")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        #P2 Price has to be below 10000 (Failed)

        self.open(base_url + '/createproduct')
        self.type("#price", 10001)
        self.type("#title", "ProductR54")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Creation Failed", "#message")

    def test_create_product_r4_6(self,*_):
        #Logs in to a user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test4@r16.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        #R4-6: last_modified_date must be after 2021-01-02 and before 2025-01-02.

        #Input Partitioning

        #P1 The date must be after 2021-01-02 (Success)
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "ProductR61")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        product = self.get_text("#product")


if __name__ == "__main__":
    print("stuff worked")