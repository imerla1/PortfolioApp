from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app.auth import bp
from app.auth.forms import RegistrationForm, LoginForm


methods = ["GET", "POST"]

@bp.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
   
   
    if form.validate_on_submit():
        flash("Registration finished succesfully", 'success')
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form)
    
@bp.route('/login', methods=methods)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username == "giorgi" and password == "1":
            flash("You are Now logged in", 'success')
            return redirect(url_for('main.index'))
        else:
            flash("Check username or password", 'danger')    
    return render_template('login.html', form=form)