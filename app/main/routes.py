from app.main import bp
from flask import render_template
from flask_login import login_required

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('base.html', title="Lashas ")

@bp.route('/profile/<username>')
@login_required
def profile(username):
    return render_template("profile.html")