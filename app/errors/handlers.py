#### Error Handlers
from flask import render_template
from app.errors import bp as error

@error.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@error.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@error.app_errorhandler(500)
def error_500(error):
    return render_template('errors/404.html'), 500