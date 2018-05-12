from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort, Markup
from services.gui.utils import requires_login, do_login, do_logout, do_register
import requests.exceptions


mod = Blueprint('users', __name__)


@mod.route('/users/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        if 'provider' in request.args:
            #some magic here
            pass
        else:
            return render_template('users/register.html')
    else:
        failed = False
        if 'password' not in request.form:
            flash('Пароль не задан')
            failed = True

        if 'login' not in request.form:
            flash('Логин не задан')
            failed = True
        if failed:
            return redirect(url_for('users.register'))

        login = request.form['login']
        password = request.form['password']
        role = None
        if 'role' in request.form and len(request.form['role']) > 0:
            role = request.form['role']
        result = do_register(login, password, role)
        if result.success:
            if result.response.status_code == 200:
                flash(Markup('Регистрация произведёна успешно'))
                response = redirect(url_for(result.redirect))
                return response
            else:
                flash(result.response.content.decode('utf-8'))
                return redirect(url_for('users.register'))
        else:
            flash(result.error)
            return redirect(url_for('users.register'))


@mod.route('/users/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('users/login.html')
    elif request.method == 'POST':
        result = do_login(request.form['login'], request.form['password'])

        if result.success:
            if result.response.status_code == 200:
                response = redirect(url_for(result.redirect))
                response.headers["Set-Cookie"] = result.response.headers["Set-Cookie"]
                g.user = result.response.cookies
                return response
            else:
                flash(result.response.content.decode('utf-8'))
                return redirect(url_for('users.login'))
        else:
            flash(result.error)
            return redirect(url_for('users.login'))



@mod.route('/users/logout')
@requires_login
def logout():
    result = do_logout()
    response = redirect(url_for(result.redirect))
    response.delete_cookie('token')
    g.user = None
    return response