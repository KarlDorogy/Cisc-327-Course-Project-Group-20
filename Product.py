from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Product(db.Model):
   name = db.Column(db.String(100), unique=False, nullable=False) # The name of the product. Can not be null
   price = db.Column(db.Integer) # The price of the product. The value must be an integer.
   brand = db.Column(db.String(100), unique=True, nullable = False) # The brand name of the product. Must be unique and can not be null
   item_type = db.Column(db.String(100), unique=False, nullable=False) # The item type of the product. Can not be null
   id = db.Column(db.Integer, primary_key=True) # The id of the product. Used to identify the product in other entities.
   quantity = db.Column(db.Integer) # The amount of the product that exists. The value must be an integer.
   attributes = db.Column(db.String(1000), unique=False, nullable=True) # Special attributes of the given product (i.e phones have storage).

   def __repr__(self):
        return '<Product %r>' % self.name