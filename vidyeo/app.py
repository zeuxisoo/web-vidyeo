import os
from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='views')
    app.static_folder = os.path.abspath('public')

    app.config.from_pyfile('../config/default.py')

    register_routes(app)
    register_view_filters(app)

    return app

def register_routes(app):
    from .routes import index

    app.register_blueprint(index.blueprint, url_prefix='')

def register_view_filters(app):
    from .helpers.view import assets_for

    @app.context_processor
    def utility_processor():
        return dict(
            assets_for=assets_for
        )
