from flask import Blueprint

spycloud_api = Blueprint('spycloud', __name__)


@spycloud_api.route('/spycloud/breach/data/emails/', methods=['GET'])
def data():
    return jsonify_data({'status': 'ok'})


@spycloud_api.route('/spycloud/breach/catalog/', methods=['GET'])
def catalog():
    return jsonify_data({'status': 'ok'})
