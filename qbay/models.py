from qbay import app
from flask_sqlalchemy import SQLAlchemy
from datetime import date
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
    # The title of the product.
    title = db.Column(db.String(80), unique=True, nullable=False)
    # The description of the product.
    description = db.Column(db.String(2000), unique=False, nullable=True)
    # The last modified date of the product.
    last_modified_date = db.Column(db.String(10), unique=False, nullable=False)
    # The owner's email
    owner_email = db.Column(db.String(1000), unique=False, nullable=False)
   

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

def update_product(new_price, new_title, new_description, title):

    existed_product = Product.query.filter_by(title=title)
    existed_product.price = new_price
    existed_product.description = new_description
    existed_product.title = new_title

    if(existed_product.price > new_price):
        return False

    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    existed_product.last_modified_date = current_date[7:10] + "-" + current_date[4:6] + "-" + current_date[0:3]

    return True

def create_product(price, title, description, last_modified_date, owner_email):
    
    # checks

    for character in title:
        if character.isdigit():
            return False
        if title.index(character) == 0:
            if character == " ":
                return False
        if title.index(character) == title.len():
            if character == " ":
                return False
        ascii_val = ord(character)
        if ((ascii_val >= 33 and ascii_val <= 47) or (ascii_val >= 58 and ascii_val <= 64) or (ascii_val >= 123 and ascii_val <= 126)):
            return False


    if title.len() > 80:
        return False
    
    if description.len() < 20 or description.len() > 2000 or description.len() <= title.len():
        return False

    if price < 10 or price > 10000:
        return False
    
    if last_modified_date.index(4) or last_modified_date.index(7) != "-":
        return False
    
    last_modified_year = int(last_modified_date[0:4])
    if last_modified_year < 2021 or last_modified_year > 2025:
        return False
    last_modified_month = int(last_modified_date[5:7])
    if last_modified_month < 1 or last_modified_month > 12:
        return False
    last_modified_day = int(last_modified_date[8:10])
    if last_modified_day < 1 or last_modified_day > 31:
        return False

    if last_modified_year == 2021:
        if last_modified_month == 1:
            if last_modified_day < 2:
                return False

    if last_modified_year == 2025:
        if last_modified_month > 1:
            return False
        else:
            if last_modified_day >= 2:
                return False
    
    if owner_email is None:
        return False
    
    existed_emails = User.query.filter_by(email=owner_email).all()
    if len(existed_emails) < 1:
        return False
    
    existed_titles = Product.query.filter_by(title=title).all()
    if len(existed_titles) > 1:
        return False
    print(existed_titles)
    
    new_product = Product(price, title, description, last_modified_date, owner_email)
    db.session.add(new_product)
    db.session.commit()

    return True 

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
    
    if '@' not in email:
        return False

    email_parts = email.split('@')
    local = email_parts[0]
    domain = email_parts[1]
    
    validate_local = re.compile(
        r"^(?=.{1,64}$)(?![.])(?!.*?[.]{2})(?!.*[.]$)[a-zA-Z0-9_.+-]+$")

    validate_domain = re.compile(
        r"^(?=.{1,63}$)(?![-])(?!.*[-])[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    if re.fullmatch(validate_local, local) is None:
        return False

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

    # check if password has at least one upercase, lowercase, and 
    # special characters in supplied password 
    if (uppercase_count == 0 or lowercase_count == 0 or 
       special_count == 0):
        return False

    # creates a new user
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

    # check if password has at least one upercase, lowercase, and 
    # special characters in supplied password    
    if (uppercase_count == 0 or lowercase_count == 0 or 
       special_count == 0):
        return None

    # Finds and returns user in database
    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    print(valids[0])
    return valids[0]


def update_user(find_email, new_name=None, 
                new_shipping_address=None, new_postal_code=None):
    '''
    updates a existing user
      Parameters:
        find_email (string):    user email
        new_name (string):    modified username
        new_shipping_address (string): modified shipping address
        new_postal_code (string): modified postal code
      Returns:
        True if updating user info succeeded otherwise False
    '''

    modify_user = User.query.filter_by(email=find_email)

    # Updating Username 
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

    # Updating Shipping address 
    if (new_shipping_address is not None):
        # check if new shipping address contains only alphanumeric characters 
        if (new_shipping_address.strip() == 0):
            return False
        # check if new shipping address is non-empty
        elif (new_shipping_address.isalnum() is False):
            return False
        else:
            modify_user.update({User.shipping_address: new_shipping_address}) 

    # Updating Postal Code
    if (new_postal_code is not None):
        modify_user.update({User.postal_code: new_postal_code})

    return True