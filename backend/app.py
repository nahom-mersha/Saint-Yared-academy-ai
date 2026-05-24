from flask import Flask, request, jsonify, session
import NM_keyword_searcher as searcher
from flask_cors import CORS
from datetime import datetime



app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "This is just the home page"

@app.route("/chat", methods=["POST"])
def bot_response():
    data = request.get_json()
    response = {}
    response["user"] = {
        "role" : "User",
        "message" : data["message"],
        "intent" : data["intent"],
        "fallbackCount" : data["fallbackCount"],
        "timestamp" : datetime.now().isoformat()
    }
     
    update = searcher.checkmsg(data)
    botResponse = update[0]
    newIntent = update[1]
    newFallbackCount = update[2]

    response["bot"] = {
        "role" : "Bot",
        "message" : botResponse,
        "intent" : newIntent,
        "fallbackCount" : newFallbackCount,
        "timestamp" : datetime.now().isoformat()
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)