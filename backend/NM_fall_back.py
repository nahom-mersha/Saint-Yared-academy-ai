def update_fb_count(newState, fall_back):
    if newState == "soft_fall_back" or newState == "hard_fallback_end":
        new_fall_back = fall_back + 1
        return new_fall_back
    else:
        return 0
    
