from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('productos', __name__, url_prefix='/productos')


@bp.route('/')
def index():
    return render_template('productos/index.html')
