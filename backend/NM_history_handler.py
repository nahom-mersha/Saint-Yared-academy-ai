import NM_initial_chat_setup
import json

def update_history(old_data, response):
    for value in response.values():
        old_data.append(value)
    new_history = old_data
    with open("NM_chat_history.json", 'w') as history:
        json.dump(new_history, history, indent=4)

def reset_history():
    initial_bot_text = NM_initial_chat_setup.get_initial_text()
    with open("NM_chat_history.json", 'w') as history:
        json.dump([initial_bot_text], history, indent=4)

def get_history():
    try:
        with open("NM_chat_history.json", 'r') as history_json:
            history = json.load(history_json)
    except:
        history = []
    return history
