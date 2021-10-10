from operator import contains
from os import error
from qbay import app
from flask_sqlalchemy import SQLAlchemy
import re


'''
This file defines data models and related business logics
'''


db = SQLAlchemy(app)

"""
User will store personal information that is used on the qbay market
"""


class User(db.Model):
    username = db.Column(
        db.String(80), nullable=False)
    email = db.Column(
        db.String(120), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    shipping_address = db.Column(db.String(120), nullable=True)
    postal_code = db.Column(db.String(120), nullable=True)
    balance = db.Column(db.Float, unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Product(db.Model):
    # The id of the product. Used to identify the product in other entities.
    id = db.Column(db.Integer, primary_key=True)
    # The price of the product. The value must be an integer.
    price = db.Column(db.Integer)
    

"""
Lays out the attributes for reviews that verified users can place on products
with a comment and a rating that can be liked or disliked
"""


class Review(db.Model):
    # The primary key id for each review on any product
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(120), unique=False, nullable=False)
    # Integer rating from 1 to 5 stars that the user can rate
    score = db.Column(db.Integer, unique=False, nullable=False)
    # String to contain the user's comment
    review = db.Column(db.String(300), unique=False, nullable=False)


"""
Data base table storing each succesful transaction that takes place on Qbay
"""


class Transaction(db.Model):
    # Sets up primary key id for each succesful transaction through Qbay
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    # Sets a seller id for the seller of a product with each transaction
    email = db.Column(db.String(120), unique=False, nullable=False)
    # The product id that was associated with the transaction
    product_id = db.Column(db.Integer, nullable=False)
    # The amount or price of a the transaction between users
    price = db.Column(db.Float, unique=False, nullable=False)
    # Sets a timestamp of a transaction
    date = db.Column(db.Date, unique=False, nullable=False)


# create all tables
db.create_all()


def register(name, email, password):
    '''
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        True if registration succeeded otherwise False
    '''

    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False
    
    # check if email or password are empty
    if (len(email.strip()) == 0 or len(password.strip()) == 0):
        return False
    
    # check if username is not between 2 and 20 characters or is empty 
    if len(name.strip()) < 2 or len(name.strip()) > 20:
        return False
    
    # check if username contains space at begining or end
    if (name[0] == ' ' or name[-1] == ' '):
        return False
    
    # check if username contains only alphanumeric characters 
    if (name.replace(' ', '').isalnum() is False):
        return False
    
    # splits email address by @, left assigned to local, right assigned
    # to domain
    if '@' not in email:
        return False

    email_parts = email.split('@')
    local = email_parts[0]
    domain = email_parts[1]

    # checks there are no double quotes before running dot-string validation
    # regex
    if local.find('\"') == -1:

        # This regex checks 5 criteria: the expression is between 1-64
        # characters, does not start or end with a dot '.', there are no
        # consecutive dots and the name is made of alphanumeric and specific
        # special/printable characters
        validate_local = re.compile(
            r"^(?=.{1,64}$)(?![.])(?!.*[.]$)(?!.*?[.]{2})"
            r"[\w!#$%&*+-/=?^`{|}~]+$")
        
        # if local is not a perfect match against validate_local, it is an
        # invalid name
        if re.fullmatch(validate_local, local) is None:
            return False
    
    # checks local name against quoted-string regex if the first and last
    # characters are double quotes. The regex checks the quoted string is
    # between 1-62 characters because an empty string is not valid and the
    # first and last characters are double quotes ' " '
    elif local.find('\"') == 0 and local.find('\"', 1) == len(local) - 1:

        # This regex checks the quoted string is made of alphanumeric
        # characters, most printable characters and special characters.
        # There is no limitation on repetition
        validate_local = re.compile(r"^(?=.{1,62}$)"
                                    r"[\w\s!#$%&*+-/=?^\"`{|}~(),:;<>@[\]]+$"
                                    )

        # if local is not a perfect match against validate_local, it is an
        # invalid name
        if re.fullmatch(validate_local, local[1:-1]) is None:
            return False
    
    else:

        # informs user that local names cannot contain both quoted and
        # unquoted text
        print('''An email local name is either a Dot-string or a 
        Quoted-string; it cannot be a combination.''')
        return False

    # if domain starts with '[' and ends with ']' it gets checked against
    # IPv4 and IPv6 domain rules. Dual addresses fail check.
    if domain.find('[') == 0 and domain.find(']', -1) == len(domain) - 1:

        # validates normal IPv4 and IPv6 addresses
        validate_domain = re.compile("(?=.{1,39}$)(((25[0-5]|2[0-4][0-9]|[01]?"
                                     "[0-9][0-9]?)[.]){3}(25[0-5]|2[0-4][0-9]|"
                                     "[01]?[0-9][0-9]?))"

                                     # if the string doesn't match against IPv4 
                                     # rules, check against IPv6 rules
                                     "|"

                                     # validates normal IPv6 addresses
                                     "(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]"
                                     "{1,4}|"
                                     "([0-9a-fA-F]{1,4}:){1,7}:|"
                                     "([0-9a-fA-F]{1,4}:){1,6}:"
                                     "[0-9a-fA-F]{1,4}|"
                                     "([0-9a-fA-F]{1,4}:){1,5}"
                                     "(:[0-9a-fA-F]{1,4}){1,2}|"
                                     "([0-9a-fA-F]{1,4}:){1,4}"
                                     "(:[0-9a-fA-F]{1,4}){1,3}|"
                                     "([0-9a-fA-F]{1,4}:){1,3}"
                                     "(:[0-9a-fA-F]{1,4}){1,4}|"
                                     "([0-9a-fA-F]{1,4}:){1,2}"
                                     "(:[0-9a-fA-F]{1,4}){1,5}|"
                                     "[0-9a-fA-F]{1,4}:"
                                     "((:[0-9a-fA-F]{1,4}){1,6})|"
                                     ":((:[0-9a-fA-F]{1,4}){1,7}|:)|"
                                     "fe80:(:[0-9a-fA-F]{0,4}){0,4}%"
                                     "[0-9a-zA-Z]{1,}|"
                                     "::(ffff(:0{1,4}){0,1}:){0,1}"
                                     "((25[0-5]|(2[0-4]|1{0,1}[0-9])"
                                     "{0,1}[0-9])[.]{3,3}"
                                     "(25[0-5]|(2[0-4]|1{0,1}[0-9])"
                                     "{0,1}[0-9])|"
                                     "([0-9a-fA-F]{1,4}:){1,4}:"
                                     "((25[0-5]|(2[0-4]|1{0,1}[0-9])"
                                     "{0,1}[0-9])[.]){3,3}"
                                     "(25[0-5]|(2[0-4]|1{0,1}[0-9])"
                                     "{0,1}[0-9])))")

        # if domain is not a perfect match against validate_domain, it is an
        # invalid address
        if re.fullmatch(validate_domain, domain[1:-1]) is None:
            return False

    # checks the domain against LDH domain rules
    else:
        validate_domain = re.compile(
            # checks the domain for five criteria: it is between 1 and 63
            # characters long, it does not start or end with a hyphen '-',
            # there is one dot '.', and every other character is
            # a-z, A-Z, 0-9, -, or . for subdomains
            r"^(?=.{1,63}$)(?![-])(?!.*[-])[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

        # if domain is not a perfect match against validate_domain, it is an
        # invalid address
        if re.fullmatch(validate_domain, domain) is None:
            return False

    # check if password is at least 6 characters long
    if len(password) < 6:
        return False

    # counting upercase, lowercase, and special characters in supplied password
    uppercase_count = 0
    lowercase_count = 0
    special_count = 0
    for char in password:
        ascii_value = ord(char)
        if (ascii_value >= 65) and (ascii_value <= 90):  # char is uppercase
            uppercase_count += 1
        elif (ascii_value >= 97) and (ascii_value <= 122):  # char is lowercase
            lowercase_count += 1
        # char is special character except space char
        elif ((ascii_value >= 33 and ascii_value <= 47) or 
              (ascii_value >= 58 and ascii_value <= 64) or 
              (ascii_value >= 123 and ascii_value <= 126)):
            special_count += 1
        else:
            continue

    # check if password meets character requirments    
    if (uppercase_count == 0 or lowercase_count == 0 or 
       special_count == 0):
        return False

    # create a new user
    user = User(username=name, email=email, password=password,
                shipping_address=None, postal_code=None, balance=100)
    # add it to the current database session
    db.session.add(user)
    # actually save the user object
    db.session.commit()

    return True


def login(email, password):
    '''
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
 
    # check if email or password are empty
    if len(email.strip()) == 0 or len(password.strip()) == 0:
        return None
    
    # check if password is at least 6 characters long
    if len(password) < 6:
        return None

    # counting upercase, lowercase, and special characters in supplied password
    uppercase_count = 0
    lowercase_count = 0
    special_count = 0
    for char in password:
        ascii_value = ord(char)
        if (ascii_value >= 65) and (ascii_value <= 90):  # char is uppercase
            uppercase_count += 1
        elif (ascii_value >= 97) and (ascii_value <= 122):  # char is lowercase
            lowercase_count += 1
        # char is special character except space char
        elif ((ascii_value >= 33 and ascii_value <= 47) or 
              (ascii_value >= 58 and ascii_value <= 64) or 
              (ascii_value >= 123 and ascii_value <= 126)):
            special_count += 1
        else:
            continue

    # check if password meets character requirments    
    if (uppercase_count == 0 or lowercase_count == 0 or 
       special_count == 0):
        return None

    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    print(valids[0])
    return valids[0]


def update_user(find_email, new_name=None, 
                new_shipping_address=None, new_postal_code=None):

    modify_user = User.query.filter_by(email=find_email)

    if (new_name is not None):
        # check if username is not between 2 and 20 characters or is empty 
        if (len(new_name.strip()) < 2 or len(new_name.strip()) > 20):
            return False
        # check if username contains space at begining or end
        elif (new_name[0] == ' ' or new_name[-1] == ' '):
            return False
        # check if username contains only alphanumeric characters 
        elif (new_name.replace(' ', '').isalnum() is False):
            return False
        else:
            modify_user.update({User.username: new_name})

    if (new_shipping_address is not None):
        # check if new shipping address contains only alphanumeric characters 
        if (new_shipping_address.strip() == 0):
            return False
        # check if new shipping address is non-empty
        elif (new_shipping_address.isalnum() is False):
            return False
        else:
            modify_user.update({User.shipping_address: new_shipping_address}) 

    if (new_postal_code is not None):

        # validate_postal checks a string follows the format
        # x0x 0x0 where x is one of A,B,C,E,G,H,J,K,L,M,N,P,R,S,T,V,X,Y
        # and 0 is any digit from 0-9
        validate_postal = re.compile(r"[ABCEGHJKLMNPRSTVXY]\d"
                                     r"[ABCEGHJKLMNPRSTVXY][\s]?\d"
                                     r"[ABCEGHJKLMNPRSTVXY]\d")
            
        # if new_postal_code is not a perfect match against
        # validate_postal, it is not a valid Canadian postal code
        if re.fullmatch(validate_postal, new_postal_code) is None:
            return False

        modify_user.update({User.postal_code: new_postal_code})

    return True