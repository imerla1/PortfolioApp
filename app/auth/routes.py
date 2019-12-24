from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app.auth import bp
from app.auth.forms import RegistrationForm


methods = ["GET", "POST"]

@bp.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    err = form.password2.errors
    print(err)
   
    if form.validate_on_submit():
        flash("Register Finished Succesfully")
        return "HELLO WORLD"
    return render_template('register.html', form=form)
    
