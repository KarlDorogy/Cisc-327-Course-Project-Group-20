from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    seller_id = db.Column(db.Integer, unique=False, nullable=False)
    buyer_id = db.Column(db.Integer, unique=False, nullable=False)
    amount = db.Column(db.Float, unique=False, nullable=False)
    timestamp = db.Column(db.String(100), unique=False, nullable=False)
    product_id = db.Column(db.Float, unique=False, nullable=False)
    
    def __repr__(self):
        return '<Transaction ID: %r>' % self.id
        return '<Transaction Seller ID: %r>' % self.seller_id
        return '<Transaction Buyer ID: %r>' % self.buyer_id
        return '<Transaction Amount: %r>' % self.amount
        return '<Transaction Timestamp: %r>' % self.timestamp
        return '<Transaction Product ID: %r>' % self.product_id