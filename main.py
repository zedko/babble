from flask import Flask, request, make_response, json


app = Flask(__name__)


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


if __name__ == '__main__':
    app.debug = True
    app.run()
