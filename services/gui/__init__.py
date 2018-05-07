import flask
from services.gui.config import DevelopmentConfig

app = flask.Flask(__name__)
app.config.from_object(DevelopmentConfig)
