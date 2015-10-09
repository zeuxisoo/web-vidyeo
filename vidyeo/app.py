import os
from flask import Flask
from flask import render_template, request, jsonify
from flask_wtf.csrf import CsrfProtect

def create_app():
    app = Flask(__name__, template_folder='views')
    app.static_folder = os.path.abspath('public')

    app.config.from_pyfile('../config/default.py')

    register_database(app)
    register_csrf(app)
    register_routes(app)
    register_api(app)
    register_view_filters(app)
    reigster_not_found(app)

    return app

def register_database(app):
    from .models import db

    db.init_app(app)
    db.app = app

def register_csrf(app):
    csrf = CsrfProtect()
    csrf.init_app(app)

def register_routes(app):
    from .routes import index

    app.register_blueprint(index.blueprint, url_prefix='')

def register_api(app):
    from .api import index

    app.register_blueprint(index.blueprint, url_prefix='/api')

def register_view_filters(app):
    from .helpers.view import assets_for

    @app.context_processor
    def utility_processor():
        return dict(
            assets_for=assets_for
        )

def reigster_not_found(app):
    @app.errorhandler(404)
    def page_not_found(e):
        if request.is_xhr:
            return jsonify(
                data=dict(
                    code=404,
                    message="404 Page not found"
                )
            ), 404
        else:
            return render_template('index.html'), 404
