from sqlalchemy.orm import backref
from extensions import db, login_manager
from app import app
from datetime import datetime
from controller import *
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
​
class User(UserMixin, db.Model):    
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean())
    is_superuser = db.Column(db.Boolean())
    password = db.Column(db.String(255), nullable=False)
​
​
    def __repr__(self):
        return f'{self.id}, {self.username}, {self.email}, {self.first_name}, {self.last_name}, {self.is_active}, {self.is_superuser}, {self.password}'
​
    def __init__(self, username, email, first_name, last_name, password, is_active=True, is_superuser=False):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active
        self.is_superuser = is_superuser
        self.password=generate_password_hash(password)
​
    def set_password(self, new_password):
        self.password=generate_password_hash(new_password)
​
    def check_password(self, password):
        return check_password_hash(self.password, password)
​
    def save(self):
        db.session.add(self)
        db.session.commit()
​
​
class Book_info(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(64,2), nullable=False)
    description = db.Column(db.Text())
    image_url = db.Column(db.String(255), nullable=False)
    stock = db.Column(db.Boolean(), default=True)
    genre = db.Column(db.String(255), nullable=False)
    language = db.Column(db.String(255), nullable=False)
    publisher = db.Column(db.String(255), nullable=False)
​
    def __repr__(self):
        return f'{self.id}, {self.title}, {self.author}, {self.price}, {self.description}, {self.image_url}, {self.stock}, {self.genre}, {self.language}, {self.publisher}'
​
    def __init__(self, title, author, price, description, image_url, stock, genre, language, publisher):
        self.title = title
        self.author = author
        self.price = price
        self.description = description
        self.image_url = image_url
        self.stock = stock
        self.genre = genre
        self.language = language
        self.publisher = publisher
​
​
    def save(self):
        db.session.add(self)
        db.session.commit()
​
​
class Books(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text())
    language = db.Column(db.String(255))
    date = db.Column(db.DateTime())
    book_id = db.Column(db.Integer(), db.ForeignKey('book_info.id'))
    book = db.relationship('Book_info', backref=db.backref('comments', lazy=True))
    
​
    def __repr__(self):
        return f'{self.id}, {self.name}, {self.message}, {self.language}, {self.date}, {self.book_id}'
​
    def __init__(self, name, message, language, date, book_id):
        self.name = name
        self.message = message
        self.language = language
        self.date = date
        self.book_id = book_id
        
​
​
    def save(self):
        db.session.add(self)
        db.session.commit()
​