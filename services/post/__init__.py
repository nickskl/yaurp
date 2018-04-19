import flask
from services.post.config import DevelopmentConfig

app = flask.Flask(__name__)
app.config.from_object(DevelopmentConfig)
