import json

def checkmsg(data):
    msg = data["message"]
    botReplay = "unknown"
    updatedIntent = ""
    updatedFallbackCount = 0
    words = msg.lower()
    words = words.split()
    
    with open("NM_keywords_dictionary.json", 'r') as f:
        data = json.load(f)

    for word in words:
        for key in data:
            for keyword in data[key]:
                if word == keyword:
                    botReplay = key


    return [botReplay, updatedIntent, updatedFallbackCount]
