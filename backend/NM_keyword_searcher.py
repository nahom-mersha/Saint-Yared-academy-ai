import json
import NM_initial_chat_setup

def checkmsg(msg):
    currentState = msg["intent"] # Sorry my intent i meant state
    words = msg["message"]
    newState = msg["intent"]
    more_info = ["", ""] # Index 0 is for crafting the next message if neccessary
    words = words.lower()
    words = words.split()
    words.append('@') # This is just to prevent no checking if the user enters an empty string
    max_fallback_count = NM_initial_chat_setup.get_max_fallback_count()
    fb_count = msg["fallbackCount"]

    if fb_count >= max_fallback_count:
        return currentState, more_info
    
    with open("NM_keywords_dictionary.json", 'r') as f:
        data = json.load(f)

    def get_next_state(current):
        mark = 0
        for state in data:
            if mark == 1:
                return state
            if state == current:
                mark = 1
        return current # This is just incase there will be a bug that continues the convo after ending it
    
    for word in words:
        if currentState == "greet_and_ask_name":
            more_info[0] = msg["message"]
            newState = get_next_state(currentState)
        elif currentState == "list_options":
            decision = ""
            for keyword_pair in data["list_options"]:
                for key, keywords in keyword_pair.items():
                    if word in keywords:
                        decision = key
            if decision == "for_about_academy":
                more_info[0] = "for_about_academy"
                newState = get_next_state(currentState)
            elif decision == "for_link":
                more_info[0] = "for_link"
                newState = get_next_state(currentState)
            elif decision == "for_contact_list":
                more_info[0] = "for_contact_list"
                newState = get_next_state(currentState)
        elif currentState == "end" or currentState =="hard_fallback_end":
            newState = currentState
        else:    
            for keyword in data[currentState]:
                if word == keyword or keyword == "CONTINUE":
                    newState = get_next_state(currentState)   
    return [newState, more_info]

if __name__ == "__main__":
    data = {"message": "yes",
                    "intent": "ask_to_show_Founding_members",
                    "fallbackCount": 0
                    }
    print(checkmsg(data))
