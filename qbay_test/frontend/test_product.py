from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

class FrontEndCreateProductTest(BaseCase):

    def test_create_product_r4_3(self, *_):
        #R4-3 The description of the product can be arbitrary characters, with a minimum length of 20 characters and a maximum of 2000 characters.

        #Input Boundary Testing
        #Input Partitioning

        # P1 The description of the product has to have a minimum length of 20 characters (Success)
        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "Partition Test One")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # P1 The description of the product has to have a minimum length of 20 characters (Failed)
        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "Partition Test One")
        self.type("#description", "short desc")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Creation Failed", "#message")

        # P2 and a maximum of 2000 characters. (Success)
        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "Partition Test One")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        
        # P2 and a maximum of 2000 characters. (Failed)
        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "Partition Test One")
        self.type("#description", """dkjalhdkljahdkljashdkahdjsha
                         daljhdklsahdashdkahdahdalhkdajkndkjasldhaiyuodgwhadha
                         iodnbkadwkjlsandklanxcjkahsdkahdwiuahdksdladjkadhaakd
                         dkjalhdkljahdkljashdkahdjshadaljhdklsahdashdkahdahdal
                         hkdajkndkjasldhaiyuodgwhadhaiodnbkadwkjlsandklanxcjka
                         hsdkahdwiuahdksdladjkadhaakddkjalhdkljahdkljashdkahdj
                         shadaljhdklsahdashdkahdahdalhkdajkndkjasldhaiyuodgwha
                         dhaiodnbkadwkjlsandklanxcjkahsdkahdwiuahdksdladjkadha
                         akddkjalhdkljahdkljashdkahdjshadaljhdklsahdashdkahdah
                         dalhkdajkndkjasldhaiyuodgwhadhaiodnbkadwkjlsandklanxc
                         jkahsdkahdwiuahdksdladjkadhaakddkjalhdkljahdkljashdka
                         hdjshadaljhdklsahdashdkahdahdalhkdajkndkjasldhaiyuodg
                         whadhaiodnbkadwkjlsandklanxcjkahsdkahdwiuahdksdladjka
                         dhaakddkjalhdkljahdkljashdkahdjshadaljhdklsahdashdkah
                         dahdalhkdajkndkjasldhaiyuodgwhadhaiodnbkadwkjlsandkla
                         nxcjkahsdkahdwiuahdksdladjkadhaakddkjalhdkljahdkljash
                         dkahdjshadaljhdklsahdashdkahdahdalhkdajkndkjasldhaiyu
                         odgwhadhaiodnbkadwkjlsandklanxcjkahsdkahdwiuahdksdlad
                         jkadhaakddkjalhdkljahdkljashdkahdjshadaljhdklsahdashd
                         kahdahdalhkdajkndkjasldhaiyuodgwhadhaiodnbkadwkjlsand
                         klanxcjkahsdkahdwiuahdksdladjkadhaakddkjalhdkljahdklj
                         ashdkahdjshadaljhdklsahdashdkahdahdalhkdajkndkjasldha
                         iyuodgwhadhaiodnbkadwkjlsandklanxcjkahsdkahdwiuahdksd
                         ladjkadhaakddkjalhdkljahdkljashdkahdjshadaljhdklsahda
                         shdkahdahdalhkdajkndkjasldhaiyuodgwhadhaiodnbkadwkjls
                         andklanxcjkahsdkahdwiuahdksdladjkadhaakddkjalhdkljahd
                         kljashdkahdjshadaljhdklsahdashdkahdahdalhkdajkndkjasl
                         dhaiyuodgwhadhaiodnbkadwkjlsandklanxcjkahsdkahdwiuahd
                         ksdladjkadhaakddkjalhdkljahdkljashdkahdjshadaljhdklsa
                         hdashdkahdahdalhkdajkndkjasldhaiyuodgwhadhaiodnbkadwk
                         jlsandklanxcjkahsdkahdwiuahdksdladjkadhaakddkjalhdklj
                         ahdkljashdkahdjshadaljhdklsahdashdkahdahdalhkdajkndkj
                         asldhaiyuodgwhadhaiodnbkadwkjlsandklanxcjkahsdkahdwiu
                         ahdksdladjkadhaakddkjalhdkljahdkljashdkahdjshadaljhdk
                         lsahdashdkahdahdalhkdajkndkjasldhaiyuodgwhadhaiodnbka
                         dwkjlsandklanxcjkahsdkahdwiuahdksdladjkadhaakddkjalhd
                         kljahdkljashdkahdjshadaljhdklsahdashdkahdahdalhkdajkn
                         dkjasldhaiyuodgwhadhaiodnbkadwkjlsandklanxcjkahsdkahd
                         wiuahdksdladjkadhaakddkjalhdkljahdkljashdkahdjshadalj
                         hdklsahdashdkahdahdalhkdajkndkjasldhaiyuodgwhadhaiodn
                         bkadwkjlsandklanxcjkahsdkahdwiuahdksdladjkadhaakddkja
                         lhdkljahdkljashdkahdjshadaljhdklsahdashdkahdahdalhkda
                         jkndkjasldhaiyuodgwhadhaiodnbkadwkjlsandklanxcjkahsdk
                         ahdwiuahdksdladjkadhaakddkjalhdkljahdkljashdkahdjshad
                         aljhdklsahdashdkahdahdalhkdajkndkjasldhaiyuodgwhadhai
                         odnbkadwkjlsandklanxcjkahsdkahdwiuahdksdladjkadhaakdd
                         kjalhdkljahdkljashdkahdjshadaljhdklsahdashdkahdahdalh
                         kdajkndkjasldhaiyuodgwhadhaiodnbkadwkjlsandklanxcjkah
                         sdkahdwiuahdksdladjkadhaakddkjalhdkljahdkljashdkahdjs
                         hadaljhdklsahdashdkahdahdalhkdajkndkjasldhaiyuodgwhad
                         haiodnbkadwkjlsandklanxcjkahsdkahdwiuahdksdladjkadhaa
                         kddkjalhdkljahdkljashdkahdjshadaljhdklsahdashdkahdahd
                         alhkdajkndkjasldhaiyuodgwhadhaiodnbkadwkjlsandklanxcj
                         kahsdkahdwiuahdksdladjkadhaakddkjalhdkljahdkljashdkah
                         djshadaljhdklsahdashdkahdahdalhkdajkndkjasldhaiyuodgw
                         hadhaiodnbkadwkjlsandklanxcjkahsdkahdwiuahdksdladjkad
                         haakddkjalhdkljahdkljashdkahdjshadaljhdklsahdashdkahd
                         ahdalhkdajkndkjasldhaiyuodgwhadhaiodnbkadwkjlsandklan
                         xcjkahsdkahdwiuahdksdladjkadhaakddkjalhdkljahdkljashd
                         kahdjshadaljhdklsahdashdkahdahdalhkdajkndkjasldhaiyuo
                         dgwhadhaiodnbkadwkjlsandklanxcjkahsdkahdwiuahdksdladj
                         kadhaakd""")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Creation Failed", "#message")

    def test_create_product_r4_5(self, *_):
        #R4-5 Price has to be of range [10, 10000].

        #Input Boundary Testing
        #Input Partitioning

        #P1 Price has to be at least 10 (Success)
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "Partition Test Two")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        #P1 Price has to be at least 10 (Failed)
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "Partition Test Two")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Creation Failed", "#message")

        #P2 Price has to be below 10000 (Success)
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "Partition Test Two")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        #P2 Price has to be below 10000 (Failed)
        self.open(base_url + '/createproduct')
        self.type("#price", 10001)
        self.type("#title", "Partition Test Two")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Creation Failed", "#message")
    