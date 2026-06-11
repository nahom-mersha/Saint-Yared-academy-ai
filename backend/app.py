from flask import Flask, Response
import NM_intents_searcher as searcher
from flask_cors import CORS
import NM_bot_replay as NM_bot_replay
import NM_fall_back as NM_fall_back
import NM_history_handler as NM_history_handler
from datetime import datetime
import json
from flask_socketio import SocketIO, emit
import NM_initial_chat_setup
import NM_state_detector

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return "This is just the home page"

@socketio.on("start_chat")
def send_history():
    history = NM_history_handler.get_history()
    if len(history) > 0:
        state = history[-1]["current_bot_state"]
        fall_back = history[-1]["fallbackCount"]
    else:
        state = NM_initial_chat_setup.get_initial_state()
        fall_back = 0
    socketio.emit("get_history", {
                "state" : state,
                "history" : history,
                "fall_back" : fall_back
            })

@socketio.on("user_text")
def bot_response(data):
    response = {}
    response["user"] = {
        "role" : "User",
        "message" : data["message"],
        "current_bot_state" : data["current_bot_state"],
        "fallbackCount" : data["fallbackCount"],
        "timestamp" : datetime.now().strftime("%I:%M:%S %p")
    }
    possible_intents = searcher.extract_possible_intents(data["message"])
    state = NM_state_detector.get_state(possible_intents, data["fallbackCount"])
    newFallbackCount = NM_fall_back.update_fb_count(state, data["fallbackCount"])
    botResponse = NM_bot_replay.get_bot_reply(state, possible_intents, newFallbackCount)
    response["bot"] = {
        "role" : "Bot",
        "message" : botResponse,
        "current_bot_state" : state,
        "fallbackCount" : newFallbackCount,
        "timestamp" : datetime.now().strftime("%I:%M:%S %p")
    }
    NM_history_handler.update_history(data["old_data"], response)
    emit("bot_reply", response)

@socketio.on("reset")
def reset_history():
    NM_history_handler.reset_history()
    initial_bot_text = NM_initial_chat_setup.get_initial_text()

    socketio.emit("reset_success", initial_bot_text)

@app.route("/export", methods=["GET"])
def export_history():
    history = NM_history_handler.get_history()
    body = json.dumps(history, indent=2)
    return Response(
        body,
        mimetype="application/json",
        headers={
            "Content-Disposition": "attachment; filename=history_of_chat.json"
        }
    )

if __name__ == "__main__":
    socketio.run(app, debug=True)