import os
from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='views')
    app.static_folder = os.path.abspath('public')

    app.config.from_pyfile('../config/default.py')

    register_routes(app)

    return app

def register_routes(app):
    from .routes import index

    app.register_blueprint(index.blueprint, url_prefix='')
