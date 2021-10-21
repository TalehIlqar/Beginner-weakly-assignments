from extensions import db
from app import app
from datetime import datetime
class Books(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    price = db.Column(db.Numeric(4,2), default=0.00)
    description = db.Column(db.Text(), nullable=False)
    image_url = db.Column(db.String(100))
    stock = db.Column(db.Integer())
    genre = db.Column(db.String(100))
    language = db.Column(db.String(100))
    publisher = db.Column(db.String(100))
    def __repr__(self):
        return f'{self.title}, {self.author}, {self.price}, {self.description}, {self.image_url}, {self.stock}, {self.genre}, {self.language}, {self.publisher}'
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
    def save(self):
        db.session.add(self)
        db.session.commit()
class Label(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    ad = db.Column(db.String(100))
    sherh = db.Column(db.Text())
    saat = db.Column(db.DateTime(), default=datetime.now())
    book_id = db.Column(db.Integer(), db.ForeignKey('books.id'))
    def __repr__(self):
        return f'{self.ad}, {self.sherh}, {self.saat}, {self.book_id}'
    def __init__(self, ad, sherh, saat, book_id):
        self.ad = ad
        self.sherh = sherh
        self.saat = saat
        self.book_id = book_id
    def save(self):
        db.session.add(self)
        db.session.commit()