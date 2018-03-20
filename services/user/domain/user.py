from flask_login import LoginManager, UserMixin, login_required, AnonymousUserMixin


class User(UserMixin):
    def __init__(self, id, login, active):
        self.id = id
        self.login = login
        self.active = active

    def is_active(self):
        return self.active


class Anonymous(AnonymousUserMixin):
    login = "Anonymous"
