from flask import Blueprint
from flask import jsonify
from flask.ext.jwt import jwt_required, current_user
from ..models import Streamer
from ..helpers import SecureHelper, ResponseHelper, MessageHelper
from ..transformers import MessageBagTransformer

blueprint = Blueprint('api.streamer', __name__)

@blueprint.route('/create')
@jwt_required()
def create():
    error    = True
    message  = ""

    streamer = Streamer.query.filter(Streamer.user_id == current_user.id).first()

    if streamer:
        message = "You already be a streamer"
    else:
        raw_channel    = "{0}-{1}".format(current_user.id, current_user.email)
        encode_channel = SecureHelper.encode_channel(raw_channel)

        streamer = Streamer(user_id=current_user.id, channel=encode_channel)
        streamer.save()

        error   = False
        message = "Your streamer role created"

    return ResponseHelper.item(
        MessageHelper.create(error, message),
        MessageBagTransformer
    ), ResponseHelper.status_code(error)
