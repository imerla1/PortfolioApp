from flask import Blueprint

bp = Blueprint('error', __name__)

import app.errors.handlers