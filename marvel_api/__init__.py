from flask import Flask
from config import Config

from .authentication.routes import auth
from .site.routes import site


# define/instantiate our Flask object...aka tell the computer that this is a flask app
app = Flask(__name__)

# tell this app how it should be configured. Does it have a database, is it a development or production flask app, does it have passwords or secret keys???- over to the config.py file to set up for this

# aka configure our flask app from the Config object we just wrote
app.config.from_object(Config)

app.register_blueprint(site)
app.register_blueprint(auth)