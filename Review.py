from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


"""
Lays out the attributes for reviews that verified users can place on products
with a comment and a rating that can be liked or disliked
"""


class Review(db.Model):
    # The primary key id for each review on any product
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    # Integer rating from 1 to 5 stars that the user can rate
    rating = db.Column(db.Integer, unique=False, nullable=False)
    # String to contain the user's comment
    comment = db.Column(db.String(300), unique=False, nullable=False)
    # Integer id tied to the user making the review
    reviewer_id = db.Column(db.Integer, unique=False, nullable=False)
    # Boolean to check if user is verified
    verified_reviewer = db.Column(db.Boolean, unique=False, nullable=False)
    # Integer count of the number of users who pressed like on the review
    likes = db.Column(db.Integer, unique=False, nullable=False)
    # Integer count of the number of users who pressed dislike on the review
    dislikes = db.Column(db.Integer, unique=False, nullable=False)
    # Integer tying each review to a product id
    product_id = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Review ID: %r>' % self.id
        return '<Review Rating: %r>' % self.rating
        return '<Review Comment: %r>' % self.comment
        return '<Review Reviewer ID: %r>' % self.reviewer_id
        return '<Review Verified Reviwer: %r>' % self.verified_reviewer
        return '<Review Likes: %r>' % self.likes
        return '<Review Dislikes: %r' % self.dislikes
        return '<Review Product ID: %r>' % self.product_id
