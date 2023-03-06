from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('mobil', __name__, url_prefix='/mobil')


@bp.route('/')
def index():
    return render_template('mobil/index.html')


@bp.route('/homemobil')
def homemobil():
    return render_template('mobil/dashboard.html')
