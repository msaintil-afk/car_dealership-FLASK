from flask import Flask
from .site.routes import site
# from .api.routes import api
# todo api
from .authentication.routes import auth
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import db as root_db


app = Flask(__name__)

app.register_blueprint(site)
# app.register_blueprint(api)
# todo register api
app.register_blueprint(auth)



app.config.from_object(Config)

root_db.init_app(app)
#order matters
migrate = Migrate(app, root_db)