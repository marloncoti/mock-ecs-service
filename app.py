from flask import Flask
import os

app = Flask(__name__)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return {"status": "ok"}, 200

@app.route('/health', methods=['GET'])
def healthcheck():
    return {"status": "ok"}, 200

@app.route('/', methods=['GET'])
def hello():
    return {"foo": "bar"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("APP_PORT", 5000))
    app.run(host="0.0.0.0", port=port)
