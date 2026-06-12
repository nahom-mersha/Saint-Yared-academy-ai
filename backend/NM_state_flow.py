import json
def handle_acceptance(past_state):

    with open("NM_state_flow_dictionary.json", "r") as f:
        data = json.load(f)
    if past_state in data:
        new_state = data[past_state]
        return new_state
    
    return "no_next_state"
