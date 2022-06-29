import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
#gives access to the project in any os we find ourselves in
#allows outside files/folders to be added to the project
#from the base dir

class Config():
    """
    Set config variable for the flask app
    Using the envirnment variables where avaible otherwise
    create the config variable if not done already
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or "SOMETHINGS WRONG"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turns off updates messages from sqlalchemy