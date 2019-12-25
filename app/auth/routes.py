from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app.auth import bp
from app.auth.forms import RegistrationForm, LoginForm
from app.models import User
from app import db


methods = ["GET", "POST"]

@bp.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
   
   
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        flash("Congratulations, you are now a registered user!", 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)
    
@bp.route('/login', methods=methods)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("You are now logged In", 'success')
            return redirect(url_for('main.index'))
        else:
            flash("Check username or password", 'danger')    
    return render_template('login.html', form=form)

@bp.route('/logout', methods=methods)
def logout():
    logout_user()
    flash("You are Now logged Out", 'info')
    return redirect(url_for('main.index'))