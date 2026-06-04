from flask import Flask, request, jsonify, Response
import NM_keyword_searcher as searcher
from flask_cors import CORS
from datetime import datetime
import json

# Sorry by "intent" I meant state


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
        "timestamp" : datetime.now().strftime("%I:%M:%S %p")
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
        "timestamp" : datetime.now().strftime("%I:%M:%S %p")
    }

    for value in response.values():
        data["old_data"].append(value)
    new_history = data["old_data"]
    with open("NM_chat_history.json", 'w') as history:
        json.dump(new_history, history, indent=4)


    return jsonify(response)

@app.route("/export", methods=["GET"])
def export_history():
    
    try:
        with open("NM_chat_history.json", 'r') as history:
            history_obj = json.load(history)
    except:
        history_obj = []

        
    body = json.dumps(history_obj, indent=2)

    return Response(
        body,
        mimetype="application/json",
        headers={
            "Content-Disposition": "attachment; filename=history_of_chat.json"
        }
    )
@app.route("/reset", methods=["POST"])
def reset_history():
    initial_bot_text =  {}
    with open("NM_bot_questions.json", 'r') as f:
        q_data = json.load(f)
        initial_bot_text["bot"] = {
                "role" : "Bot",
                "message" : q_data["greet_and_ask_name"],
                "intent" : "greet_and_ask_name",
                "fallbackCount" : 0,
                "timestamp" : datetime.now().strftime("%I:%M:%S %p")
            }

    with open("NM_chat_history.json", 'w') as history:
        json.dump([initial_bot_text["bot"]], history, indent=4)
    return "history was also reseted"

if __name__ == "__main__":
    app.run(debug=True)