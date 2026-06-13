import json

def get_bot_reply(state):
    with open("NM_bot_questions.json", 'r') as f:
        q_data = json.load(f)

    replay = q_data[state]

    return replay