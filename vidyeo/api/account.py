from flask import Blueprint
from flask import jsonify
from flask.ext.jwt import jwt_required, current_identity
from ..helpers import ResponseHelper
from ..transformers import AccountTransformer

blueprint = Blueprint('api.account', __name__)

@blueprint.route('/me')
@jwt_required()
def me():
    return ResponseHelper.item(current_identity, AccountTransformer)

