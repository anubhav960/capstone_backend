from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "Hello, World"

@app.route("/incomingData", methods=['POST'])
@cross_origin()
def data():
    import spellcheck
    request_data=request.get_json()
    data=request_data['data']
    return correct_text(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)