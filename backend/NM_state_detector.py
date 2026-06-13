import NM_initial_chat_setup
import json
import pprint
import NM_history_handler

def get_state(possible_intents, fall_back, current_state, past_data):    
    with open("NM_state_intent_dictionary.json", 'r') as f:
        data = json.load(f)
    pprint.pprint(past_data)
    max_fallback_count = NM_initial_chat_setup.get_max_fallback_count()
    if fall_back >= max_fallback_count:
        state = "hard_fallback_end"
        return state
    
    if current_state == "soft_fall_back":
        current_state = NM_history_handler.get_last_possible_state()

    
    if "ANY" in data[current_state]["possible_intents"]:
        return data[current_state]["next"]
    
    if len(possible_intents) == 0:
        state = "soft_fall_back"
        return state

    for intent in possible_intents:
        if intent in data[current_state]["possible_intents"]:
            return data[current_state]["next"]
        
    return "soft_fall_back"
        