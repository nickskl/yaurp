from flask import Flask
from services.gateway.config import current_config


app = Flask(__name__)
app.config.from_object(current_config)
