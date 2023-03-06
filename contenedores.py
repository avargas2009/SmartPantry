from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('contenedores', __name__, url_prefix='/contenedores')


@bp.route('/')
def index():
    return render_template('contenedores/index.html')


@bp.route('/vistaContenedor')
def vistaContenedor():
    return render_template('contenedores/view.html')
