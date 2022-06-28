import os

basedir = os.path.abspath(os.path.dirname(__file__))
#gives access to the project in any os we find ourselves in
#allows outside files/folders to be added to the project
#from the base dir

class Config():
    """
    Set config variable for the flask app
    Using the envirnment variables where avaible otherwise
    create the config variable if not done already
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or "SOMETHINGS WRONG"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db') 
    SQLALCHEMY_TRACK_MODIFICATION = False #turns off updates messages from sqlalchemy