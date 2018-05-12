from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort
from services.gui.utils import requires_admin
from services.gui.utils import do_get_statistics

mod = Blueprint('statistics', __name__)


@mod.route('/')
def index():
    result = do_get_statistics()
    return render_template('statistics/index.html')
