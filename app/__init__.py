from flask import Flask
from config import Config

fl = '/home/imerla/Downloads/Login_v14/Login_v14'

app = Flask(__name__)

app.config.from_object(Config)




# we import routes here
from app.auth import bp as auth_bp
app.register_blueprint(auth_bp)
from app.main import bp as main_bp
app.register_blueprint(main_bp)