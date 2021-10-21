from flask import render_template, request, redirect
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash 
from app import app
from forms import contact_form, registrFrom, loginForm
from model import User
from extensions import login_manager




@app.route('/registr', methods = ["GET", "POST"])
def registr():
    form = registrFrom()
    if request.method == 'POST':
        post_data = request.form   
        form = registrFrom(data = post_data)
        if form.validate_on_submit:
            user = User(first_name = form.first_name.data,last_name = form.last_name.data, email = form.email.data, username = form.username.data, password = form.password.data )
            user.save()
            return redirect("/login")
    return render_template("sign_up.html", form = form )



@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = loginForm()
    if request.method == 'POST':
        post_data = request.data
        form1 = loginForm(data=post_data)
        if form.validate_on_submit():
            user = User.query.filter_by(user_name=form.user_name.data).first() 
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                print("login oldu")
            else:
                print("login olmadi")
    return render_template('sing_in.html', form2 = form1)



@app.route('/user-profile')
def user_profile():
    return render_template('user_profile.html')
