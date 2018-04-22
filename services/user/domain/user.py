from flask_login import LoginManager, UserMixin, login_required, AnonymousUserMixin


class User(UserMixin):
    def __init__(self, identifier, username, active):
        self.id = identifier
        self.username = username
        self.active = active

    def is_active(self):
        return self.active


class Anonymous(AnonymousUserMixin):
    username = "Guest"
