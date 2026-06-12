import json
from datetime import datetime

def get_initial_state():
    INITIAL_STATE = "greet_user"
    return INITIAL_STATE

def get_initial_text():
    initial_bot_text =  {}
    initial_state = get_initial_state()
    with open("NM_bot_questions.json", 'r') as f:
        q_data = json.load(f)
        initial_bot_text = {
                "role" : "Bot",
                "message" : q_data[initial_state] + q_data["list_options"],
                "current_bot_state" : initial_state,
                "fallbackCount" : 0,
                "timestamp" : datetime.now().strftime("%I:%M:%S %p")
            }
    return initial_bot_text

def get_max_fallback_count():
    return 3