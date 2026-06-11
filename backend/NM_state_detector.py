import NM_initial_chat_setup
import json

def get_state(possible_intents, fall_back):    
    with open("NM_state_intent_dictionary.json", 'r') as f:
        data = json.load(f)
    
    max_fallback_count = NM_initial_chat_setup.get_max_fallback_count()
    if fall_back >= max_fallback_count:
        state = data["max_fall_back"]
        return state
    
    if len(possible_intents) == 0:
        state = data["no_keyword_match"]
        return state
    
    if len(possible_intents) == 1:
        state = data[possible_intents[0]]
        return state
    
    return data["multiple_intents"]
    