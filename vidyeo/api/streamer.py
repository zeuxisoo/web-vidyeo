from flask import Blueprint
from flask import jsonify, request
from flask.ext.jwt import jwt_required, current_identity
from ..models import Streamer
from ..helpers import SecureHelper, ResponseHelper, MessageHelper
from ..transformers import MessageBagTransformer

blueprint = Blueprint('api.streamer', __name__)

@blueprint.route('/create')
@jwt_required()
def create():
    error    = True
    message  = ""

    streamer = Streamer.query.filter(Streamer.user_id == current_identity.id).first()

    if streamer:
        message = "You already be a streamer"
    else:
        encode_channel = SecureHelper.encode_channel(current_identity.id)

        streamer = Streamer(user_id=current_identity.id, channel=encode_channel)
        streamer.save()

        error   = False
        message = "Your streamer role created"

    return ResponseHelper.item(
        MessageHelper.create(error, message),
        MessageBagTransformer
    ), ResponseHelper.status_code(error)

@blueprint.route('/start', methods=['POST'])
@jwt_required()
def start():
    error    = True
    message  = ""

    streamer = Streamer.query.filter(Streamer.user_id == current_identity.id).first()

    if not streamer:
        message = "Can not found related streamer account"
    else:
        streamer_json = request.get_json()

        streamer.cover  = streamer_json['cover']
        streamer.status = "open"
        streamer.save()

        error   = False
        message = "Your stream was started"

    return ResponseHelper.item(
        MessageHelper.create(error, message),
        MessageBagTransformer
    ), ResponseHelper.status_code(error)

@blueprint.route('/stop', methods=['POST'])
@jwt_required()
def stop():
    error    = True
    message  = ""

    streamer = Streamer.query.filter(Streamer.user_id == current_identity.id).first()

    if not streamer:
        message = "Can not found related streamer account"
    elif streamer.status != "open":
        message = "The stream was not started"
    else:
        streamer.status = "close"
        streamer.save()

        error   = False
        message = "Your stream was closed"

    return ResponseHelper.item(
        MessageHelper.create(error, message),
        MessageBagTransformer
    ), ResponseHelper.status_code(error)
