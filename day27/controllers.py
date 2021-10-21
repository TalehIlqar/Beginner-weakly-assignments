from flask import render_template, request
from app import app
from forms import BooksForm
from models import Books
from models import Label
@app.route("/book/")
def index():
    results = Books.query.all()
    return render_template('index.html', results=results)
@app.route("/book/<int:book_ind>/", methods = ['GET', 'POST'])
def book(book_ind):
    a='True'
    results = Books.query.all()
    label = Label.query.filter_by(book_id = book_ind)
    post_data = request.form
    form = BooksForm()
    if request.method == 'POST':
            form = BooksForm(data=post_data)
            if form.validate_on_submit():
                contact = Label(ad = form.ad.data, sherh = form.sherh.data, saat = form.saat.data, book_id=book_ind)
                contact.save()
    return render_template('product.html', form=form, results=results, label=label, book_ind=book_ind-1, a=a)