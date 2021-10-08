from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Product(db.Model):
    # The name of the product. Can not be null
    name = db.Column(db.String(100), unique=False, nullable=False)
    # The price of the product. The value must be an integer.
    price = db.Column(db.Integer)
    # The brand name of the product. Must be unique and can not be null
    brand = db.Column(db.String(100), unique=True, nullable=False)
    # The item type of the product. Can not be null
    item_type = db.Column(db.String(100), unique=False, nullable=False)
    # The id of the product. Used to identify the product in other entities.
    id = db.Column(db.Integer, primary_key=True)
    # The amount of the product that exists. The value must be an integer.
    quantity = db.Column(db.Integer)
    # Special attributes of the given product (i.e phones have storage).
    attributes = db.Column(db.String(1000), unique=False, nullable=True)
    #The email of the user
    user_email = db.Column(db.String(1000), unique=False, nullable=False)
    #The email of the owner
    owner_email = db.Column(db.String(1000), unique=False, nullable=False)
    #The last modified date
    last_modified_date = db.Column(db.String(1000), unique=False, nullable=True)
    #The description of the product
    description = db.Column(db.String(1000), unique=False, nullable=True)

def create_product():
    product = Product

def update_product():


def __repr__(self):
        return '<Product %r>' % self.name
