import os

from flask import Flask, jsonify

from api.spycloud import spycloud_api
from api.cyberprotect import cyberprotect_api

app = Flask(__name__)

app.url_map.strict_slashes = False
app.config.from_object('config.Config')

app.register_blueprint(spycloud_api)
app.register_blueprint(cyberprotect_api)


@app.errorhandler(Exception)
def handle_error(exception):
    code = getattr(exception, 'code', 500)
    message = getattr(exception, 'description', 'Something went wrong.')
    reason = '.'.join([
        exception.__class__.__module__,
        exception.__class__.__name__,
    ])

    response = jsonify(code=code, message=message, reason=reason)
    return response, code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
