from flask import Blueprint

bp = Blueprint('auth', __name__)

import app.auth.routes