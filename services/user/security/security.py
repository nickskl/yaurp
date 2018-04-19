from OpenSSL import SSL
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_login import LoginManager
from services.user.repository.user_repository import Users, Roles
from services.user.domain.user import User, Anonymous
from services.user import app
from services.user.security.token import Token

context = SSL.Context(SSL.TLSv1_2_METHOD)
#context.use_privatekey("./user.key")
#context.use_certificate("./user.crt")

db = SQLAlchemy(app)
# setting up flask_security
user_datastore = SQLAlchemyUserDatastore(db, Users, Roles)
security = Security(app, user_datastore)

# setting up flask_login
login_manager = LoginManager()
login_manager.anonymous_user = Anonymous
# TODO views and stuff
# login_manager.login_view = "login"
# login_manager.login_message = u"Please log in to access this page."
# login_manager.refresh_view = "reauth"

user = user_datastore.find_user(id=0)
role = user_datastore.find_role('tester')
user_datastore.add_role_to_user(user, role)
user_datastore.commit()

# ????!
@login_manager.user_loader
def load_user(identifier):
    user = user_datastore.get_user(identifier)
    if (user is not None and
        user.username is not "Guest"):
        return User(user.id, user.login, user.password, user.active, user.token)


def get_token(login, password):
    user = user_datastore.find_user(login=login)
    if (user is not None and
        user.login != "Guest"):
        if user.password == password:
            if user.token is None:
                user_datastore.get_user(user.id).token = Token.generate(user.id).serialize()
                user_datastore.commit()
            token = user_datastore.get_user(user.id).token
            return token
    return None


def get_user_by_token(token_string):
    user = user_datastore.get_user(identifier=0)
    user = user_datastore.find_user(token=token_string)
    return user


def check_role(user_id, role):
    user = user_datastore.get_user(user_id)
    if (user is not None and
            user.username is not "Guest"):
        return role in user.roles
    return False


def refresh_token(token_string):
    if token_string is not None:
        user = get_user_by_token(token_string)
        if user is not None:
            user.token = Token.refresh(token_string)
            user_datastore.commit()
            return user.token
    return None


login_manager.init_app(app)
