from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort, Markup
from services.gui.utils import requires_login, do_login, do_logout, do_register


mod = Blueprint('users', __name__)


@mod.route('/users/info')
@requires_login
def info():
    return render_template('users/index.html')


@mod.route('/users/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        if 'provider' in request.parameter_storage_class:
            #some magic here
            pass
        else:
            return render_template('users/register.html')
    else:
        result = do_register()
        if result.success:
            flash(Markup('Регистрация произведёна успешно'))
            return redirect('posts.index')
        else:
            flash(result.error)
            return redirect(result.redirect)


@mod.route('/users/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('users/login.html')
    elif request.method == 'POST':
        result = do_login(request.form.login, request.form.password)
        if result.success:
            return redirect('posts.index')
        else:
            flash(result.error)
            return redirect(result.redirect)


@mod.route('/users/logout')
@requires_login
def logout():
    do_logout()
    return redirect(url_for("posts.posts"))