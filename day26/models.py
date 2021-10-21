from extensions import db
from datetime import datetime
from app import app

# a = Products(name="computer", description="some text", categories_id=2, amount=10, price=1000, production=2021)


class Book(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title =  db.Column(db.String(40), unique = True)
    author = db.Column(db.String(200), nullable = True)
    price = db.Column(db.Float(), nullable = True)
    description = db.Column(db.String(200), nullable = True)
    # image_url = url_for(images, filename='images/Inkognito.png')
    stock = db.Column(db.Float(), default = 0)
    genre = db.Column(db.String(200), nullable = True)
    language = db.Column(db.String(200), nullable = True)
    publisher = db.Column(db.String(200), nullable = True)

    # categories_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    

    def __repr__(self):
        return f'{self.id} | {self.title} | {self.author} | {self.price} | {self.description} | {self.stock} | {self.genre} | {self.language} | {self.publisher}'
    
    def __init__(self, title, author = None, price = None, description = None, stock = None, genre = None, language = None, publisher = None):
        self.title = title
        self.author = author
        self.price = price
        self.description = description
        # self.image_url = image_url
        self.stock = stock
        self.genre = genre
        self.language = language
        self.publisher = publisher

    def save(self):
        db.session.add(self)
        db.session.commit()

    