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
    shipping_address = db.Column(db.String(120), nullable=True)
    postal_code = db.Column(db.String(120), nullable=True)
    balance = db.Column(db.Float, unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

    # # Remaining Douglas Code from Assignment/Sprint 1 for Users Below

    # # Sets primary key so we can map things to table
    # id = db.Column(db.Integer, primary_key=True)
    # # Only verified users can make reviews
    # verified = db.Column(db.Boolean, unique=False, nullable=False)
    # # Tracks all prodocts the user is buying
    # shopping_cart = db.Column(db.List, unique=True, nullable=True)
    # # Tracks all products the user wants to buy
    # wish_list = db.Column(db.Integer, unique=True, nullable=True)
    # # User address that products are shipped to
    # shipping_address = db.Column(db.String(200), unique=True, nullable=False)


class Product(db.Model):
    # The id of the product. Used to identify the product in other entities.
    id = db.Column(db.Integer, primary_key=True)
    # The price of the product. The value must be an integer.
    price = db.Column(db.Integer)
    # The title of the product.
    title = db.Column(db.String(1000), unique=False, nullable=False)
    # The description of the product.
    description = db.Column(db.String(1000), unique=False, nullable=True)
    # The last modified date of the product.
    last_modified_date = db.Column(db.String(1000), unique=False, nullable=True)
    # The owner's email
    owner_email = db.Column(db.String(1000), unique=False, nullable=False)

def create_product(price, title, description, last_modified_date, owner_email):

def update_product():


   

"""
Lays out the attributes for reviews that verified users can place on products
with a comment and a rating that can be liked or disliked
"""


class Review(db.Model):
    # The primary key id for each review on any product
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    # Integer rating from 1 to 5 stars that the user can rate
    score = db.Column(db.Integer, unique=False, nullable=False)
    # String to contain the user's comment
    comment = db.Column(db.String(300), unique=False, nullable=False)

    # # Remaining Tom Code from Assignment/Sprint 1 for Products Below

    # # Integer id tied to the user making the review
    # reviewer_id = db.Column(db.Integer, unique=False, nullable=False)
    # # Boolean to check if user is verified
    # verified_reviewer = db.Column(db.Boolean, unique=False, nullable=False)
    # # Integer count of the number of users who pressed like on the review
    likes = db.Column(db.Integer, unique=False, nullable=False)
    # # Integer count of the number of users who pressed dislike on the review
    # dislikes = db.Column(db.Integer, unique=False, nullable=False)
    # # Integer tying each review to a product id
    # product_id = db.Column(db.Integer, unique=False, nullable=False)


"""
Data base table storing each succesful transaction that takes place on Qbay
"""


class Transaction(db.Model):
    # Sets up primary key id for each succesful transaction through Qbay
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    # The product id that was associated with the transaction
    product_id = db.Column(db.Integer, unique=False, nullable=False)
    # Sets a seller id for the seller of a product with each transaction
    user_email = db.Column(db.Integer, unique=False, nullable=True)
    # The amount or price of a the transaction between users
    price = db.Column(db.Float, unique=False, nullable=False)
    # Sets a timestamp of a transaction
    date = db.Column(db.String(100), unique=False, nullable=False)

    # # Remaining Karl Code from Assignment/Sprint 1 for Transaction Below

    # # Sets a buyer id for the buyer of a product with each transaction
    # buyer_id = db.Column(db.Integer, unique=False, nullable=True)
    # # Represents if a transaction is between two users
    # # Or if the transaction is a addition to a user's balance
    # balance_transaction = db.Column(db.Boolean, unique=False, nullable=False)


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
