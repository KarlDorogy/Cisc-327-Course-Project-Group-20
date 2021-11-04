from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

class FrontEndCreateProductTest(BaseCase):

    def listing_creation_success(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "Test Product")
        self.type("#description", "This is a test description made to be at least twenty characters long")
        self.click('input[type="submit"]')