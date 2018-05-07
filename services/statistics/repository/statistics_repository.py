from flask_sqlalchemy import SQLAlchemy
from services.post.domain.post import Post
from services.post import app
import datetime
import jsonpickle
import dateutil.parser

db = SQLAlchemy(app)


class Statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64))
    data = db.Column(db.JSON)


db.create_all()
db.session.commit()


class StatisticsRepository:
    def create(self, type, data):
        stat_event = Statistics(type=type, data=data)
        db.session.add(stat_event)
        db.session.commit()
        return stat_event.id

    def get_by_type(self, type):
        return Statistics.query.filter_by(type=type).all()

    def get(self, id):
        return Statistics.query.filter_by(id=id).first()