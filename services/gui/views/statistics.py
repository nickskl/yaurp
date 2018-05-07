from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort
from services.gui.utils import requires_admin


mod = Blueprint('statistics', __name__)


@mod.route('/')
def index():
    return render_template('statistics/index.html')
