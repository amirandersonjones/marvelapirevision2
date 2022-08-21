#imports @ top
import os

# set up the base directory of the entire application - aka help our computer figure out our file system and where to find the different pieces of this project.
basedir = os.path.abspath(os.path.dirname(__name__))

# config variables setup the names are mandatory: FLASK_APP, FLASK_ENV, FLASK_KEY
class Config:
    """
    set configuration variables for our entire flask app
    """
    FLASK_APP = os.environ.get('FLASK_APP')  # go get the FLASK_APP value from .env
    FLASK_DEBUG = os.environ.get('FLASK.ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')