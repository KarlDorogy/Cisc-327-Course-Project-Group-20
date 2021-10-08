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

    validate_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    if re.fullmatch(validate_email, email):
        return True
    else:
        print(f"'{email}' is NOT a valid email")
        return False

    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False
    
    # check if email, password, or username are empty
    if (len(email.strip()) == 0 or len(password.strip()) == 0 or 
       len(name.strip()) == 0):
        return False
    
    # check if username between 2 and 20 characters
    if len(name) < 2 or len(name) > 20:
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

    # check if username contains space at begining or end
    if (name[0] == ' ' or name[-1] == ' '):
        return False
    
    # check if username contains only alphanumeric characters 
    if (name.replace(' ', '').isalnum() is False):
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


def update_user(name, shipping_address, postal_code):
    pass
