from qbay import app
from flask_sqlalchemy import SQLAlchemy


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
    shipping_adress = db.Column(db.String(120), nullable=True)
    postal_code = db.Column(db.String(120), nullable=True)
    balance = db.Column(db.Float, unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Product(db.Model):
    # The id of the product. Used to identify the product in other entities.
    id = db.Column(db.Integer, primary_key=True)
    # The price of the product. The value must be an integer.
    price = db.Column(db.Integer)

    # # Remaining Tom Code from Assignment/Sprint 1 for Products Below

    # # The name of the product. Can not be null
    # name = db.Column(db.String(100), unique=False, nullable=False)
    # # The brand name of the product. Must be unique and can not be null
    # brand = db.Column(db.String(100), unique=True, nullable=False)
    # # The item type of the product. Can not be null
    # item_type = db.Column(db.String(100), unique=False, nullable=False)
    # # The amount of the product that exists. The value must be an integer.
    # quantity = db.Column(db.Integer)
    # # Special attributes of the given product (i.e phones have storage).
    # attributes = db.Column(db.String(1000), unique=False, nullable=True)


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

    # create a new user
    user = User(username=name, email=email, password=password)
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
    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]
