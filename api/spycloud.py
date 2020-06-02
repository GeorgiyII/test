from flask import Blueprint, jsonify
from werkzeug.exceptions import TooManyRequests

spycloud_api = Blueprint('spycloud', __name__)


@spycloud_api.route('/spycloud/breach/data/emails/admin@example.org', methods=['GET'])
def spy_data():
    data = {
        "cursor": "",
        "hits": 2,
        "results": [
            {
                "domain": "example.org",
                "target_url": "192.168.100.149",
                "infected_machine_id": "A8F01FCC8CA01546086603",
                "user_browser": "Google Chrome",
                "ip_addresses": [
                    "116.203.240.111"
                ],
                "email_username": "admin",
                "email": "admin@example.org",
                "spycloud_publish_date": "2020-05-28T00:00:00Z",
                "password": "admin",
                "email_domain": "example.org",
                "source_id": 17674,
                "password_plaintext": "admin",
                "password_type": "plaintext",
                "infected_time": "2020-05-10 00:04:25",
                "document_id": "2b1e43c7-798c-474b-906b-6b11ca6a8680",
                "severity": 25
            },
            {
                "city": "()",
                "domain": "example.org",
                "infected_path": "C:/Users/Usama/AppData/Local/Temp/6210230526.exe",
                "infected_time": "2020-03-26 16:56:49",
                "country": "()",
                "isp": "()",
                "email_username": "admin",
                "email": "admin@example.org",
                "spycloud_publish_date": "2020-04-16T00:00:00Z",
                "password": "test123",
                "target_url": "http://localhost:3000/en/session",
                "sighting": 1,
                "email_domain": "example.org",
                "source_id": 17551,
                "infected_machine_id": "0bb046a5-2ef2-4ec3-abbe-ba76f5b78e6c",
                "password_plaintext": "test123",
                "password_type": "plaintext",
                "document_id": "90f9c47d-c86d-400f-9a57-38fed22b5fad",
                "severity": 25
            }
        ]
    }
    return jsonify(data)


@spycloud_api.route('/spycloud/breach/catalog/17674', methods=['GET'])
def spy_catalog_17674():
    catalog = {
        "cursor": "",
        "hits": 1,
        "results": [
            {
                "confidence": 3,
                "description": "AzorUlt is a lesser known credential stealing botnet, also known as crimeware. This malware steals data from infected computers via web browsers and protected storage. Once infected, the computer sends the stolen data to a bot command and control (C&C) server, where the data is stored. Any credentials from this source can be assumed to already be in the hands of threat actors, and should be changed immediately.",
                "title": "Azorult Botnet",
                "type": "PRIVATE",
                "acquisition_date": "2020-05-27T00:00:00Z",
                "site": "n/a",
                "spycloud_publish_date": "2020-05-28T00:00:00Z",
                "site_description": "The AzorUlt Botnet is a lesser-known botnet that is mainly used for stealing credentials.",
                "uuid": "8f8a4738-7068-4666-882b-793d485fd9da",
                "num_records": 1530174,
                "id": 17674,
                "assets": {
                    "username": 644708,
                    "infected_path": 23558,
                    "infected_time": 1530174,
                    "user_browser": 1530174,
                    "ip_addresses": 1530174,
                    "target_url": 1530174,
                    "password": 1530174,
                    "email": 885466,
                    "infected_machine_id": 1530174
                }
            }
        ]
    }
    return jsonify(catalog)


@spycloud_api.route('/spycloud/breach/catalog/17551', methods=['GET'])
def spy_catalog_17551():
    catalog = {
        "cursor": "",
        "hits": 1,
        "results": [
            {
                "confidence": 3,
                "description": "AzorUlt is a lesser known credential stealing botnet, also known as crimeware. This malware steals data from infected computers via web browsers and protected storage. Once infected, the computer sends the stolen data to a bot command and control (C&C) server, where the data is stored. Any credentials from this source can be assumed to already be in the hands of threat actors, and should be changed immediately.",
                "title": "Azorult Botnet",
                "type": "PRIVATE",
                "acquisition_date": "2020-05-27T00:00:00Z",
                "site": "n/a",
                "spycloud_publish_date": "2020-05-28T00:00:00Z",
                "site_description": "The AzorUlt Botnet is a lesser-known botnet that is mainly used for stealing credentials.",
                "uuid": "8f8a4738-7068-4666-882b-793d485fd9da",
                "num_records": 1530174,
                "id": 17674,
                "assets": {
                    "username": 644708,
                    "infected_path": 23558,
                    "infected_time": 1530174,
                    "user_browser": 1530174,
                    "ip_addresses": 1530174,
                    "target_url": 1530174,
                    "password": 1530174,
                    "email": 885466,
                    "infected_machine_id": 1530174
                }
            }
        ]
    }
    return jsonify(catalog)


@spycloud_api.route('/spycloud/breach/data/emails/test@test.com ', methods=['GET'])
def spy_data():
    raise TooManyRequests
