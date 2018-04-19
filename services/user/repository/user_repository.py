from flask_sqlalchemy import SQLAlchemy
from flask_security import RoleMixin, UserMixin
from services.user import app


db = SQLAlchemy(app)

roles_users = db.Table("roles_users",
                       db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
                       db.Column("role_id", db.Integer, db.ForeignKey("roles.id")))


class Roles(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(255))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    token = db.Column(db.String)
    roles = db.relationship("Roles", secondary=roles_users, backref=db.backref("users", lazy="dynamic"))

db.create_all()
db.session.commit()