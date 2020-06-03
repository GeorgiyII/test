from flask import Blueprint, jsonify, request, Response
from werkzeug.exceptions import TooManyRequests


abuse_api = Blueprint('abuse', __name__)


@abuse_api.route('/check', methods=['GET'])
def abuse_data():
    if request.args['ipAddress'] == '1.1.1.1':
        data = {
            "data": {
                "ipAddress": "1.1.1.1",
                "isPublic": False,
                "ipVersion": 4,
                "isWhitelisted": False,
                "abuseConfidenceScore": 0,
                "countryCode": None,
                "usageType": None,
                "isp": None,
                "domain": None,
                "hostnames": [],
                "countryName": None,
                "totalReports": 13,
                "numDistinctUsers": 6,
                "lastReportedAt": "2020-06-01T23:34:12+00:00",
                "reports": [
                    {
                        "reportedAt": "2020-06-01T23:34:12+00:00",
                        "comment": "Tried to use the server as an open proxy",
                        "categories": [
                            9,
                            15,
                            21
                        ],
                        "reporterId": 39677,
                        "reporterCountryCode": "BY",
                        "reporterCountryName": "Belarus"
                    }
                ]
            }
        }
    else:
        return jsonify({'errors': [
            {'detail': 'test'}
        ]}), 429
    return jsonify(data)
