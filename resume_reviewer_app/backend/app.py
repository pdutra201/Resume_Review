from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
