import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# دریافت کلید API از متغیر محیطی
HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")
if not HELIUS_API_KEY:
    raise ValueError("HELIUS_API_KEY environment variable is not set.")

@app.route("/")
def home():
    return "✅ Helius Proxy is running."

@app.route("/rpc", methods=["POST"])
def proxy_rpc():
    helius_url = f"https://mainnet.helius.xyz/v1/{HELIUS_API_KEY}/rpc"
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(helius_url, json=request.get_json(), headers=headers)
        return response.content, response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
