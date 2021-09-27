from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    wallet = db.Column(db.Integer)
    
    

    def __repr__(self):
        return '<User %r>' % self.username


#class Search

#class Transaction(dbT.Model):
#   transaction_name = dbT.Column(db.String(100), unique=False, nullable=False)
#   transaction_amount = dbT.Column(db.Integer) 

#class Product(dbL.Model):
#   name = dbL.Column(db.String(100), unique=False, nullable=False)
#   price = dbL.Column(db.Integer)
#   brand = dbL.Column(db.String(100), unique=True, nullable = False)
#   review = dbL.Column(db.String(10000), unique=False, nullable=True) 
#   item_type = dbL.Column(db.String(100), unique=False, nullable=False)

