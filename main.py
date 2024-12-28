from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def hook():
    print(request.data)
    return "Hello World!"

@app.route('/', methods=['GET'])
def index():
    return "App running..."


if __name__ == '__main__':
    app.run(debug=True)