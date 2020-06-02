from flask import Blueprint, jsonify
from werkzeug.exceptions import TooManyRequests


cyberprotect_api = Blueprint('cyberprotect', __name__)


@cyberprotect_api.route('/cyberprotect/1.1.1.1', methods=['GET'])
def cyber_data():
    data = {
        "geo": {
            "country": {
                "code": "AU",
                "name": "Australia"
            }
        },
        "signature": "f9e779c8cefd81cbc3824564e7e0aec121547eeaaf210d5b7a3442f02761b940",
        "data": "1.1.1.1",
        "types": [
            "ip"
        ],
        "version": 17594054,
        "firstSeen": "2018-10-01",
        "lastSeen": "2020-06-02T13:00:10.738Z",
        "sources": 1,
        "scores": [
            {
                "date": "2020-06-02T13:00:10.738Z",
                "score": 0.3680555555555556,
                "confidence": None,
                "level": "suspicious",
                "details": [
                    {
                        "date": "2020-06-02T13:00:10.738Z",
                        "engineId": "4528c02832675d34898b0511e24c0607",
                        "engineConfidence": None,
                        "level": "safe",
                        "score": 0
                    },
                    {
                        "date": "2020-06-02T13:00:10.738Z",
                        "engineId": "4f0cf6da88d2d2867549648af09c6072",
                        "engineConfidence": None,
                        "level": "safe",
                        "score": 0
                    }
                ]
            }
        ]
    }
    return jsonify(data)


@cyberprotect_api.route('/cyberprotect/2.2.2.2', methods=['GET'])
def cyber_data_2():
    raise TooManyRequests
