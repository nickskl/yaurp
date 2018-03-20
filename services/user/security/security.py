from OpenSSL import SSL
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_login import  LoginManager
from services.user.repository.user_repository import UserDB, RoleDB
from services.user import app


context = SSL.Context(SSL.TLSv1_2_METHOD)
#context.use_privatekey("./user.key")
#context.use_certificate("./user.crt")

db = SQLAlchemy(app)
# setting up flask_security
user_datastore = SQLAlchemyUserDatastore(db, UserDB, RoleDB)
security = Security(app, user_datastore)
# setting up flask_login
login_manager = LoginManager()