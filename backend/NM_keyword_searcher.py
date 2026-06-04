import json
def checkmsg(msg, currentState):
    words = msg["message"]
    newState = "unknown"
    more_info = ["", ""] # Index 0 is for crafting the next message if neccessary
    words = words.lower()
    words = words.split()
    

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
            if decision == "for_about_website":
                more_info[0] = "for_about_website"
                newState = "ask_to_show_Founding_members"
            elif decision == "for_link":
                more_info[0] = "for_link"
                newState = "ask_to_show_Founding_members"
            elif decision == "for_contact_list":
                more_info[0] = "for_contact_list"
                newState = "ask_to_show_Founding_members"
        if currentState == "end":
            newState = "end"
            more_info[0] = "chat_ended"
        else:    
            for keyword in data[currentState]:
                if word == keyword or keyword == "CONTINUE":
                    newState = get_next_state(currentState) # You will need to implement a function to get the next state

    return [newState, more_info]

# Next round add the logic of the additional info to the caller. like the name of the user etc
#Try runs just for fun! Delete this afterwards!!
if __name__ == "__main__":
    print(checkmsg({"message" : "a"}, "greet_and_ask_name"))
    print(checkmsg({"message" : "b"}, "list_options"))
    print(checkmsg({"message" : "information"}, "list_options"))
    print(checkmsg({"message" : "website"}, "list_options"))
    print(checkmsg({"message" : "email"}, "list_options"))
    print(checkmsg({"message" : "ya"}, "ask_to_show_Founding_members"))
    print(checkmsg({"message" : "blablabla"}, "ask_satisfaction"))
    print(checkmsg({"message" : "qqqqq"}, "end"))
    print("--------------------------------------------------------")
    print(checkmsg({"message" : "Nahom"}, "greet_and_ask_name"))
    print(checkmsg({"message" : "information"}, "list_options"))
    print(checkmsg({"message" : "website"}, "list_options"))
    print(checkmsg({"message" : "email"}, "list_options"))
    print(checkmsg({"message" : "ya, show me"}, "ask_to_show_Founding_members"))
    print(checkmsg({"message" : "It is good, Thank You"}, "ask_satisfaction"))
    print(checkmsg({"message" : "Okay bye"}, "end"))

