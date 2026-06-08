import json
import NM_initial_chat_setup


def get_bot_reply(newIntent, fb_count, more_info):
    with open("NM_bot_questions.json", 'r') as f:
        q_data = json.load(f)
    terminate = False
    current_state = newIntent
    max_fallback_count = NM_initial_chat_setup.get_max_fallback_count()
    
    if fb_count >= max_fallback_count:
        terminate = True
    
    if fb_count > 0 and current_state != "end":
        if 0 < fb_count <= 2 and terminate == False:
            reply = q_data["soft_fallback"]
        else:
            reply = q_data["hard_fallback_end"]
    
    else:
        if current_state == "list_options":
            reply = f"Hi {more_info[0]}! {q_data['list_options']['question']}"
        elif current_state == "ask_to_show_Founding_members":
            reply = f"{q_data['list_options'][more_info[0]]} {q_data['ask_to_show_Founding_members']}"
        else:
            reply = q_data[current_state]

    return reply