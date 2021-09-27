from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

"""
User will store personal information that is used on the qbay market
"""


class User(db.Model):
    # Sets primary key so we can map things to table
    id = db.Column(db.Integer, primary_key=True)
    # The alias displayed on transactions
    username = db.Column(db.String(80), unique=True, nullable=False)
    # Used to verify user
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Only verified users can make reviews
    verified = db.Column(db.Bool, unique=False, nullable=False)
    # Shows user balance, will be used for transactions
    wallet = db.Column(db.Float, unique=True, nullable=False)
    # Tracks all prodocts the user is buying
    shopping_cart = db.Column(db.List, unique=True, nullable=True)
    # Tracks all products the user wants to buy
    wish_list = db.Column(db.Integer, unique=True, nullable=True)
    # User address that products are shipped to
    shipping_address = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
