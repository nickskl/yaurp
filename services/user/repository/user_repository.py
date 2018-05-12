from flask_sqlalchemy import SQLAlchemy
from services.user.security.token import Token
from services.user import app


db = SQLAlchemy(app)

roles_users = db.Table("roles_users",
                       db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
                       db.Column("role_id", db.Integer, db.ForeignKey("roles.id")))


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    user_token = db.Column(db.String)
    roles = db.relationship("Roles", secondary=roles_users, backref=db.backref("users", lazy="dynamic"))


class UserRepository:
    def create_user(self, login, password):
        t = Token.generate(login).serialize()
        user = Users(login=login, password=password, active=True, user_token=t)
        db.session.add(user)
        db.session.commit()
        return user.id

    def create_role(self, name):
        role = Roles(name=name)
        db.session.add(role)
        db.session.commit()
        return role.id

    def role_exists(self, name):
        return db.session.query(Roles.query.filter(Roles.name == name).exists()).scalar()

    def get_user(self, login):
        if self.user_exists(login):
            user = Users.query.filter_by(login=login).first()
            return user
        else:
            return None

    def get_role(self, name):
        if self.role_exists(name):
            role = Roles.query.filter_by(name=name).first()
            return role
        else:
            return None

    def add_role_to_user(self, rolename, username):
        user = self.get_user(username)
        role = self.get_role(rolename)
        user.roles.append(role)
        db.session.commit()

    def get_by_token(self, token):
        if not Token.is_expired(token):
            login = Token.get_value(token)
            user = self.get_user(login)
            return user
        return None

    def get_token(self,login, password):
        if self.user_exists(login):
            user = self.get_user(login=login)
            if user.password == password:
                t = Token.generate(login).serialize()
                user.user_token = t
                db.session.commit()
                return t
        return None

    def check_password(self, login, password):
        if self.user_exists(login):
            user = Users.query.filter_by(login=login).first()
            return password == user.password
        return False

    def update(self, login, password):
        if self.user_exists(login):
            user_to_update = Users.query.filter_by(login=login).first()
            if password is not None:
                user_to_update.password = password
            db.session.commit()

    def refresh_token(self, token):
        login = Token.get_value(token)
        if self.user_exists(login):
            t = Token.refresh(token)
            user = self.get_user(login)
            user.user_token = t
            db.session.commit()
            return t
        return None

    def delete(self, login):
        if self.user_exists(login):
            user_to_delete = Users.query.filter_by(login=login).first()
            db.session.delete(user_to_delete)
            db.session.commit()

    def user_exists(self, login):
        return db.session.query(Users.query.filter(Users.login == login).exists()).scalar()

