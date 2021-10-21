from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateTimeField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from extensions import db
from models import User
from flask import request
​
class Books_info(FlaskForm):
    name = StringField('Tam adınız:', validators=[DataRequired(), Length(max=30)] )
    message = TextAreaField('Şərhiniz:', validators=[Length(max=50)])
    language = SelectField(u'Hansı dildə oxumusunuz?', choices=[('Azərbaycan', 'Azərbaycan'), ('İngilis', 'İngilis'), ('Rus', 'Rus'), ('İspan', 'İspan')])
    date = DateTimeField()
    book_id = IntegerField()
​
class RegisterForm(FlaskForm):
    first_name = StringField('Adınız:', validators=[DataRequired(), Length(min=3, max=30)] )
    last_name = StringField('Soyadınız:', validators=[DataRequired(), Length(min=3, max=30)] )
    email = StringField('Email:', validators=[DataRequired(), Email(), Length(min=3, max=30)] )
    username = StringField('İstifadəçi adı:', validators=[DataRequired(), Length(min=3, max=30)] )
    password = PasswordField('Password: ',validators=[DataRequired(), Length(min=6, max=25)] )
​
​
class LoginForm(FlaskForm):
    username = StringField('İstifadəçi adı:', validators=[DataRequired(), Length(min=3, max=30)] )
    email = StringField('Email address:', validators=[DataRequired(), Length(min=3, max=30)] )
    password = PasswordField('Password: ',validators=[DataRequired(), Length(min=6, max=25)] )
    
    
​