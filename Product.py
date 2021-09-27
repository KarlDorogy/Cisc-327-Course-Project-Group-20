from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Product(dbL.Model):
   name = db.Column(db.String(100), unique=False, nullable=False)
   price = db.Column(db.Integer)
   brand = db.Column(db.String(100), unique=True, nullable = False) 
   item_type = db.Column(db.String(100), unique=False, nullable=False)
   id = db.Column(db.Integer)
   quantity = db.Column(db.Integer)
   attributes = db.Column(db.String(1000), unique=False, nullable=True)

   def __repr__(self):
        return '<Product %r>' % self.name