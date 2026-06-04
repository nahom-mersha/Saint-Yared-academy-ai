import json
def checkmsg(msg):
    bot_reply = "Default Message"
    newFallbackCount = 0
    currentState = msg["intent"] # Sorry my intent i meant state
    words = msg["message"]
    newState = "soft_fallback"
    more_info = ["", ""] # Index 0 is for crafting the next message if neccessary
    words = words.lower()
    words = words.split()
    words.append('@') # This is just to prevent no checking if the user enters an empty string
    

    with open("NM_keywords_dictionary.json", 'r') as f:
        data = json.load(f)

    def get_next_state(current):
        mark = 0
        for state in data:
            if mark == 1:
                return state
            if state == current:
                mark = 1
        return state # This is just incase there will be a bug that continues the convo after ending it

    def handle_fallback(msg):
        current_count = msg["fallbackCount"]
        if current_count == 2:
            return 3, "hard_fallback_end"
        else:
            current_count += 1
            return current_count, "soft_fallback"
    
    for word in words:
        if currentState == "greet_and_ask_name":
            more_info[0] = msg["message"]
            newState = "list_options"
        if currentState == "list_options":
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
        if currentState == "end" or currentState =="hard_fallback_end":
            newState = "end"
            more_info[0] = "chat_ended"
        if currentState == "soft_fallback": # his was newState IDK why
            newFallbackCount, newState = handle_fallback(msg)
        else:    
            for keyword in data[currentState]:
                if word == keyword or keyword == "CONTINUE":
                    newState = get_next_state(currentState) # You will need to implement a function to get the next state
            

    def get_bot_reply(current_state, more_info):
        with open("NM_bot_questions.json", 'r') as f:
            q_data = json.load(f)
        if current_state == "list_options":
            reply = f"Hi {more_info[0]}! {q_data['list_options']['question']}"
        elif current_state == "ask_to_show_Founding_members":
            reply = f"{q_data['list_options'][more_info[0]]} {q_data['ask_to_show_Founding_members']}"
        else:
            reply = q_data[current_state]

        return reply
        
    

    
    # bot_reply = [bot_reply, newState, newFallbackCount]
    bot_reply = get_bot_reply(newState, more_info)
    return [bot_reply, newState, newFallbackCount]

# Next round add the logic of the additional info to the caller. like the name of the user etc
#Try runs just for fun! Delete this afterwards!!
if __name__ == "__main__":
    # print(checkmsg({"message" : "a"}, "greet_and_ask_name"))
    # print(checkmsg({"message" : "b"}, "list_options"))
    # print(checkmsg({"message" : "information"}, "list_options"))
    # print(checkmsg({"message" : "website"}, "list_options"))
    # print(checkmsg({"message" : "email"}, "list_options"))
    # print(checkmsg({"message" : "ya"}, "ask_to_show_Founding_members"))
    # print(checkmsg({"message" : "blablabla"}, "ask_satisfaction"))
    # print(checkmsg({"message" : "qqqqq"}, "end"))
    print("--------------------------------------------------------")
    data = {"message": "yes",
                    "intent": "ask_to_show_Founding_members",
                    "fallbackCount": 0
                    }
    print(checkmsg(data))
    # print(checkmsg({"message" : "information"}, "list_options"))
    # print(checkmsg({"message" : "website"}, "list_options"))
    # print(checkmsg({"message" : "email"}, "list_options"))
    # print(checkmsg({"message" : "ya, show me"}, "ask_to_show_Founding_members"))
    # print(checkmsg({"message" : "It is good, Thank You"}, "ask_satisfaction"))
    # print(checkmsg({"message" : "Okay bye"}, "end"))

