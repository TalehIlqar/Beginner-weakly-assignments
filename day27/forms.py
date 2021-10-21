from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired
from models import Books
from extensions import db
class BooksForm(FlaskForm):
    ad = StringField(label = 'Tam adınız:', validators=[DataRequired()])
    sherh = TextAreaField(label = 'Şərhiniz:')
    saat = DateTimeField()