from flask import Blueprint
from flask import jsonify
from flask.ext.jwt import jwt_required

blueprint = Blueprint('api.streamer', __name__)

@blueprint.route('/try-it')
@jwt_required()
def try_it():
    return jsonify(message="/streamer/try-it")

