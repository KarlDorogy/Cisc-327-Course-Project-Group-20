from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

class FrontEndCreateProductTest(BaseCase):


    def test_create_product_r4_1(self, *_):
        #Logs in to a user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test4@r16.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        #R4-1: The title of the product has to be alphanumeric-only, and space allowed only if it is not as prefix and suffix.

        #Input Partitioning

        #P1 The title of the product has to be alphanumeric-only (Success)
        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "ProductR11")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        #P1 The title of the product has to be alphanumeric-only (Fail)
        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "%Beans")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Creation Failed", "#message")

        #P2 space allowed only if it is not as prefix and suffix (Success)
        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "Product R12")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        #P2 space allowed only if it is not as prefix and suffix (Fail)
        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", " ProductR13")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Creation Failed", "#message")

        #P2 space allowed only if it is not as prefix and suffix (Fail)
        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "ProductR14 ")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Creation Failed", "#message")

    def test_create_product_r4_2(self, *_):
        #Logs in to a user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test4@r16.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        #R4-2: The title of the product is no longer than 80 characters.

        # Input Exhaustive

        # Case 1 The title is less than 80 characters (Success)

        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "ProductR2")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Case 2 The title is more than 80 characters (Fail)

        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "jkasdhakdhakldhasdhakljjdashjdajkdhkajsldhakljdhjsadnakjldhnwajkcjdgajsdkahjSSSSS")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Creation Failed", "#message")


    def test_create_product_r4_3(self, *_):
        #Logs in to a user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test4@r16.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        #R4-3 The description of the product can be arbitrary characters, with a minimum length of 20 characters and a maximum of 2000 characters.

        #Input Boundary Testing
        #Input Partitioning

        # P1 The description of the product has to have a minimum length of 20 characters (Success)

        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "ProductR31")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # P1 The description of the product has to have a minimum length of 20 characters (Failed)

        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "ProductR32")
        self.type("#description", "short desc")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Creation Failed", "#message")

        # P2 and a maximum of 2000 characters. (Success)

        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "ProductR33")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # P2 and a maximum of 2000 characters. (Failed)

        self.open(base_url + '/createproduct')
        self.type("#price", 1000)
        self.type("#title", "ProductR34")
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

    def test_create_product_r4_4(self, *_):
        #Logs in to a user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test4@r16.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        # R4-4: Description has to be longer than the product's title.

        # Input Exhaustive

        # Case 1 The description is longer than the title (Success)
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "ProductR4")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Case 2 The description is shorter than the title (Fail)
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "ProductR42andenoughcharacterstohavemorethantwentycharacters")
        self.type("#description", "This is a description that is long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        # Case 3 The description is the same length as the title (Fail)
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "ProductR43andenoughcharacterstohavemorethantwentycharacters")
        self.type("#description", "ProductR43andenoughcharacterstohavemorethantwentycharacters")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

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

    def date_compare(date):
        # Checks if year is within range
        if date[4] != "-" or date[7] != "-":
            return False
        last_modified_year = int(date[0:4])
        if last_modified_year < 2021 or last_modified_year > 2025:
            return False
        last_modified_month = int(date[5:7])
        if last_modified_month < 1 or last_modified_month > 12:
            return False
        last_modified_day = int(date[8:10])
        if last_modified_day < 1 or last_modified_day > 31:
            return False

        # Year range check but if year is 2021
        if last_modified_year == 2021:
            if last_modified_month == 1:
                if last_modified_day < 2:
                    return False

        # Year range check but if year is 2025
        if last_modified_year == 2025:
            if last_modified_month > 1:
                return False
            else:
                if last_modified_day >= 2:
                    return False

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
        pPrice = self.get_text("#price")
        self.type("#title", "ProductR61")
        pTitle = self.get_text("#title")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        product = self.get_text("#" + pTitle)
        date = product[(pTitle.len()+pPrice.len()+4):(pTitle.len()+pPrice.len()+4)+10]
        if(self.date_compare(date)):
            self.assert_text("#welcome-header")
        
        #P2 The date must be before 2025-01-02 (Success)
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        pPrice = self.get_text("#price")
        self.type("#title", "ProductR62")
        pTitle = self.get_text("#title")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        product = self.get_text("#" + pTitle)
        date = product[(pTitle.len()+pPrice.len()+4):(pTitle.len()+pPrice.len()+4)+10]
        if(self.date_compare(date)):
            self.assert_element("#welcome-header")
            

    def test_create_r4_7(self, *_):
        
        #R4-7: owner_email cannot be empty. The owner of the corresponding product must exist in the database.

        #Input Partitioning 

        #P1 The owner_email cannot be empty (Fail)
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "ProductR71")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Creation Failed", "#message")

        #P1 The owner_email cannot be empty (Success)
        #Logs in to a user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test4@r16.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "ProductR72")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        #P2 The owner of the corresponding product must exist in the database. (Success)
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "ProductR73")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

    def test_create_r4_8(self, *_):
        #Logs in to a user before creating products
        self.open(base_url + '/login')
        self.type("#email", "test4@r16.com")
        self.type("#password", "@Password")
        self.click('input[type="submit"]')

        #R4-8: A user cannot create products that have the same title.

        #Input Exhaustive

        #Case 1: No products have the same name (Success)
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "ProductR81")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "ProductR82")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

        #Case 2: Two products have the same name (Fail)
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "ProductSAME")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.open(base_url + '/createproduct')
        self.type("#price", 11)
        self.type("#title", "ProductSAME")
        self.type("#description", "This is a very long test description that is at least 20 characters long")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Product Creation Failed", "#message")
        

    