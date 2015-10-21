from flask import Blueprint
from flask import request
from ..models import Streamer
from ..helpers import ResponseHelper, MessageHelper
from ..transformers import StreamerTransformer, MessageBagTransformer

blueprint = Blueprint('api.info', __name__)

@blueprint.route('/info')
def info():
    channel = request.args.get('channel')

    error    = True
    message  = ""

    streamer = Streamer.query.filter(Streamer.channel == channel).first()

    if not streamer:
        message = "Can not found related streamer"
    elif streamer.status != "open":
        message = "The stream was not started"
    else:
        return ResponseHelper.item(streamer, StreamerTransformer)

    return ResponseHelper.item(
        MessageHelper.create(error, message),
        MessageBagTransformer
    ), ResponseHelper.status_code(error)
