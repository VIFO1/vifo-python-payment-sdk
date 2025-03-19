from flask import Flask, request, jsonify
import os
import json
import hmac
import hashlib
from datetime import datetime
from dotenv import load_dotenv
from modules.interfaces.body_webhook import WebhookBody, WebhookData, WebhookActionName
from modules.common_functions.generate_signature import generate_signature
load_dotenv()

app = Flask(__name__)

SECRET_KEY = os.getenv("SECRET_KEY")
@app.route("/")
def home():
    return "Flask server is running!", 200


@app.route('/api/v1/vifo/webhook', methods=['POST'])
def vifo_webhook():
    timestamp = request.headers.get("x-request-timestamp")
    request_signature = request.headers.get("x-request-signature")
    
    if not timestamp or not request_signature:
        return jsonify({"errors": ["Missing headers"]}), 400

    try:
        datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return jsonify({"errors": ["Invalid timestamp format"]}), 400

    body = request.get_json()
    if not body:
        return jsonify({"errors": ["Invalid body"]}), 400

    try:
        body["data"] = WebhookData(**body["data"])
        body_obj = WebhookBody(**body)
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

     # Kiểm tra action_name bằng Enum
    try:
        action = WebhookActionName(body_obj.action_name)
    except ValueError:
        return jsonify({"errors": ["Invalid action_name"]}), 400

    signature = generate_signature(SECRET_KEY, timestamp, body_obj.to_dict())

    if request_signature != signature:
        return jsonify({"errors": ["Invalid signature"]}), 401
    
    print(json.dumps(body_obj.to_dict(), indent=2))

    return jsonify({"status": "success"}), 201  

if __name__ == '__main__':
    app.run(debug=True, port=8000)
