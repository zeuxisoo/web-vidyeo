from flask import Blueprint
from flask import render_template, jsonify
from ..forms import SignupForm
from ..transformers import StreamerTransformer, FormErrorTransformer, FormSuccessTransformer
from ..helpers import ResponseHelper
from ..models import Streamer

blueprint = Blueprint('api.index', __name__)

@blueprint.route('/streaming')
def streaming():
    streamers = Streamer.query.filter(Streamer.status == 'open').order_by(Streamer.update_at.desc()).all()

    return ResponseHelper.collection(streamers, StreamerTransformer)

@blueprint.route('/signup', methods=['POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        form.save()

        data = dict(
            message="Your account was created"
        )

        return ResponseHelper.item(data, FormSuccessTransformer)
    else:
        return ResponseHelper.item(form.errors, FormErrorTransformer), 400
