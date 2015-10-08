from flask import Blueprint
from flask import render_template, jsonify
from ..forms import SignupForm
from ..transformers import FormErrorTransformer, FormSuccessTransformer
from ..helpers import ResponseHelper

blueprint = Blueprint('api.index', __name__)

@blueprint.route('/signup', methods=['POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        message = "Your account was created"

        return ResponseHelper.item(message, FormSuccessTransformer)
    else:
        return ResponseHelper.item(form.errors, FormErrorTransformer), 500

@blueprint.route('/login', methods=['POST'])
def login():
    return jsonify(message="login")
