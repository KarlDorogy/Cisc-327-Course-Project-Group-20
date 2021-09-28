from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

"""
Data base storing each succesful transaction that takes place on Qbay
"""


class Transaction(db.Model):
    # Sets up primary key id for each succesful transaction through Qbay
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    # Sets a seller id for the seller of a product with each transaction
    seller_id = db.Column(db.Integer, unique=False, nullable=True)
    # Sets a buyer id for the buyer of a product with each transaction
    buyer_id = db.Column(db.Integer, unique=False, nullable=True)
    # The amount or price of a the transaction between users
    amount = db.Column(db.Float, unique=False, nullable=False)
    # Sets a timestamp of a transaction
    timestamp = db.Column(db.String(100), unique=False, nullable=False)
    # The product id that was associated with the transaction
    product_id = db.Column(db.Integer, unique=False, nullable=False)
    # Represents if a transaction is between two users
    # Or if the transaction is a addition to a user's balance
    balance_transaction = db.Column(db.Boolean, unique=False, nullable=False)

    def __repr__(self):
        return '<Transaction ID: %r>' % self.id
        return '<Transaction Seller ID: %r>' % self.seller_id
        return '<Transaction Buyer ID: %r>' % self.buyer_id
        return '<Transaction Amount: %r>' % self.amount
        return '<Transaction Timestamp: %r>' % self.timestamp
        return '<Transaction Product ID: %r>' % self.product_id
        return '<Addition to a Balance?: %r>' % self.balance_transaction
