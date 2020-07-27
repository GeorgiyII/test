from flask import Blueprint, jsonify, request, Response
from werkzeug.exceptions import InternalServerError


cybercrime_api = Blueprint('abuse', __name__)


@cybercrime_api.route('/query.php', methods=['GET'])
def cibercrime_data():
    if request.args['url'] == '1.1.1.1':
        data = {
            "success": True,
            "message": "Malicious: Keitaro"
        }
    else:
        raise InternalServerError
    return jsonify(data)
