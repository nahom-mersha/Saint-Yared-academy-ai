import json

def checkmsg(msg):
    words = msg.lower()
    words = words.split()
    
    with open("NM_keywords_dictionary.json", 'r') as f:
        data = json.load(f)

    for word in words:
        for key in data:
            for keyword in data[key]:
                if word == keyword:
                    return key
    return "unknown"