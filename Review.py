from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


"""
Lays out the attributes for reviews that users can place on products
with a comment and a rating
"""


class Review(db.Model):
    # User's id
    id = db.Column(db.Integer, primary_key=True)
    # Integer rating from 1 to 5 stars that user rates
    rating = db.Column(db.Integer, primary_key=True)
    # String to contain the user's comment
    comment = db.Column(db.String(120), unique=True, nullable=False)
    # Boolean to check if user is verified
    verified_comment = db.Column(db.Boolean, primary_key=True)
