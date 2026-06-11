import json

def extract_possible_intents(words):
    words = words.lower()
    words = words.split()
    with open("NM_intent_keyword_dictionary.json", 'r') as f:
        data = json.load(f)
    
    possible_intents = []
    for word in words:
        for intent, keywords in data.items():
            for keyword in keywords:
                if word == keyword:
                    possible_intents.append(intent)
    
    return possible_intents

if __name__ == "__main__":
    data = {"message": "",
                    "intent": "ask_to_show_Founding_members",
                    "fallbackCount": 0
                    }
    print(extract_possible_intents(data))
