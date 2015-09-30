from flask import Blueprint
from flask import render_template

blueprint = Blueprint('index', __name__)

@blueprint.route('/')
def index():
    return render_template('index.html')
