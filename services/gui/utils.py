from functools import wraps
from flask import g, url_for, flash, abort, request, redirect


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash(u'You need to be signed in for this page.')
            return redirect(url_for('user.login', next=request.path))
        return f(*args, **kwargs)
    return decorated_function


def requires_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.user.is_admin:
            abort(401)
        return f(*args, **kwargs)
    return requires_login(decorated_function)


def requires_publisher(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.user.is_publisher and not g.user.is_admin:
            abort(401)
        return f(*args, **kwargs)
    return requires_login(decorated_function)


def do_login(login, password):
    pass


def do_logout():
    pass


def do_register():
    pass