from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort
from services.gui.utils import requires_login, requires_admin, requires_publisher

mod = Blueprint('posts', __name__)


@mod.route('/')
def index():
    return redirect(url_for("posts.posts"))


@mod.route('/posts')
def posts():
    return render_template('posts/index.html')


@mod.route('/posts/create')
@requires_publisher
def create():
    return render_template('posts/create.html')


@mod.route('/posts/search')
def search():
    return render_template('posts/search.html')


@mod.route('/posts/search/results')
def search_results():
    return render_template('posts/search_results.html')


@mod.route('/post/delete')
@requires_publisher
def delete():
    return render_template('posts/delete.html')

@mod.route('/post/edit')
@requires_publisher
def edit():
    return render_template('posts/edit.html')
