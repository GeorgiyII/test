from flask import Blueprint, jsonify

spycloud_api = Blueprint('spycloud', __name__)


@spycloud_api.route('/spycloud/breach/data/emails/', methods=['GET'])
def data():
    return jsonify({'status': 'ok'})


@spycloud_api.route('/spycloud/breach/catalog/', methods=['GET'])
def catalog():
    return jsonify({'status': 'ok'})
