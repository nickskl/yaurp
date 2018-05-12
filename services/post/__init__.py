import flask
from services.post.config import current_config

app = flask.Flask(__name__)
app.config.from_object( current_config)
