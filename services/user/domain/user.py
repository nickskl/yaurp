from flask_login import LoginManager, UserMixin, login_required, AnonymousUserMixin


class User(UserMixin):
    def __init__(self, identifier, username, password, active, token):
        self.id = identifier
        self.username = username
        self.password = password
        self.active = active
        self.token = token

    def is_active(self):
        return self.active


class Anonymous(AnonymousUserMixin):
    username = "Guest"
