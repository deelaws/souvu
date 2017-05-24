from flask import Blueprint, request, render_template, jsonify

mod_app = Blueprint('app',__name__, url_prefix='/app')

@mod_app.route('/home', methods=['GET'])
def home():
    return "Hello World home"


@mod_app.route('/data', methods=['POST'])
def sample_post_handler():
    request.json
    return jsonify(memories=[1,2,3,4,5], yourname="waleed shahid")