from flask import request, make_response, json
from babbler import app


@app.route('/', )
def hello_world():
    return 'Hello World!'


@app.route('/report/', methods=['POST'])
def accept_report():
    response = make_response({"status": "ok. data reported"})

    if request.is_json:
        response.status_code = 201
        print(request.json)
        return response
    else:
        response.data = bytes(json.dumps({"status": "failed. pass application/json content-type header"}), encoding='utf-8')
        response.status_code = 415
        return response