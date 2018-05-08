import flask
from services.user.config import current_config


app = flask.Flask(__name__)
app.config.from_object(current_config)
