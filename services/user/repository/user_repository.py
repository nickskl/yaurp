from flask_sqlalchemy import SQLAlchemy
from flask_security import RoleMixin, UserMixin
from services.user import app


db = SQLAlchemy(app)

roles_users = db.Table("roles_users",
                       db.Column("user_id", db.Integer, db.ForeignKey("userDB.id")),
                       db.Column("role_id"), db.Integer, db.ForeignKey("roleDB.id"))


class RoleDB(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(255))


class UserDB(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship("RoleDB", secondary=roles_users, backref=db.backref("usersDB", lazy="dynamic"))