from flask import Flask, request, jsonify, session
import NM_keyword_searcher as searcher
from flask_cors import CORS



app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "This is just the home page"

@app.route("/chat", methods=["POST"])
def bot_response():
    data = request.get_json()
    user_msg = data["message"]
    print(data["old_data"])

    bot_response = searcher.checkmsg(user_msg)

    return jsonify({"reply" : f"The bot's answer is: {bot_response}"})

if __name__ == "__main__":
    app.run(debug=True)