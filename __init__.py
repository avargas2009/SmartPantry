import os

from flask import (Flask, render_template)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',

    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import contenedores
    app.register_blueprint(contenedores.bp)

    from . import productos
    app.register_blueprint(productos.bp)

    from . import mobil
    app.register_blueprint(mobil.bp)
    #app.add_url_rule('/contenedores', endpoint='index')

    @app.route('/')
    def maste_index():
        return render_template('dashboard.html')

    return app
