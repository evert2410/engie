import sys
import json
from flask import Flask, Response, request

from ecarton_code_challenge.lib.convert import convert_chars

app = Flask('code_challenge')

@app.route('/convert', methods=['POST'])
def convert():

    request_data = json.loads(request.data)

    converted = convert_chars(request_data)
    print(converted)

    resp = Response(
        response=json.dumps(converted),
        mimetype='application/json',
        status=200)

    return resp


def create_app():
    return app
