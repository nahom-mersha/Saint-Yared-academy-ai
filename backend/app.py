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

    print(data["old_data"])
     
    update = searcher.checkmsg(data)
    botResponse = update[0]
    newIntent = update[1]
    newFallbackCount = update[2]

    return jsonify({"reply" : f"The bot's answer is: {botResponse}",
                    "newIntent" : newIntent,
                    "newFallbackCount" : newFallbackCount
                    })

if __name__ == "__main__":
    app.run(debug=True)