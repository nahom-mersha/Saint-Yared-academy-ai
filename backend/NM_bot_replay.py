import json
import NM_multiple_intents_handler

def get_bot_reply(state, possible_intents, fb_count):
    with open("NM_bot_questions.json", 'r') as f:
        q_data = json.load(f)

    if state == "list_and_clarify_intent":
        reply = NM_multiple_intents_handler.handle_multiple_intents(possible_intents)
    else:
        reply = q_data[state] + q_data["list_options"]

    return reply