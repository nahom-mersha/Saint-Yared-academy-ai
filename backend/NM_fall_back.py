import NM_initial_chat_setup

def check_fb_count(newIntent, pastIntent, current_fb):
    max_fallback_count = NM_initial_chat_setup.get_max_fallback_count()
    if current_fb >= max_fallback_count:
        return current_fb
    if newIntent == pastIntent:
        current_fb += 1
        return current_fb
    return 0
    
