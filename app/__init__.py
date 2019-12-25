from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

fl = '/home/imerla/Downloads/Login_v14/Login_v14'

app = Flask(__name__)

#config part 
db = SQLAlchemy(app)
migrate = Migrate(db=db, app=app)
login = LoginManager(app)

#####

app.config.from_object(Config)




# we import routes here
from app.auth import bp as auth_bp
app.register_blueprint(auth_bp)
from app.main import bp as main_bp
app.register_blueprint(main_bp)
from app import models