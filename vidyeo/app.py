import os
from flask import Flask
from flask import render_template, request, jsonify
from flask_wtf.csrf import CsrfProtect
from flask.ext.jwt import JWT

def create_app():
    app = Flask(__name__, template_folder='views')
    app.static_folder = os.path.abspath('public')

    app.config.from_pyfile('../config/default.py')

    register_database(app)
    register_csrf(app)
    register_jwt(app)
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

def register_jwt(app):
    from .models import Account

    # curl -X POST -H "Content-Type: application/json" -d '{"username":"<USERNAME>","password":"<PASSWORD>"}' http://localhost:5000/api/auth
    def authenticate(username, password):
        if '@' in username:
            account = Account.query.filter_by(email=username).first()
        else:
            account = Account.query.filter_by(username=username).first()

        if account and account.password_verify(password):
            print account
            return account

    # curl -H "Authorization: Bearer <JWT_TOKEN>" http://localhost:5000/api/media/detail/protected?token=<TOKEN>
    def identity(payload):
        if 'identity' in payload:
            return Account.query.get(payload['identity'])
        else:
            return None

    jwt = JWT(app, authenticate, identity)

    @jwt.jwt_error_handler
    def error_handler(e):
        data = {
            'message'    : e.description,
            'status_code': e.status_code,
            'error'      : e.error
        }

        return jsonify(data=data), e.status_code, e.headers

def register_routes(app):
    from .routes import index

    app.register_blueprint(index.blueprint, url_prefix='')

def register_api(app):
    from .api import index, account, streamer

    app.register_blueprint(streamer.blueprint, url_prefix='/api/streamer')
    app.register_blueprint(account.blueprint, url_prefix='/api/account')
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
