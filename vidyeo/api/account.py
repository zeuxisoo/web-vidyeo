from flask import Blueprint
from flask import jsonify
from flask.ext.jwt import jwt_required

blueprint = Blueprint('api.account', __name__)

@blueprint.route('/me')
@jwt_required()
def me():
    return jsonify(message="/account/me")

