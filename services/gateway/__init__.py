from flask import Flask
from services.gateway.config import *

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
