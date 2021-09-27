from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


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
