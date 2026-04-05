def decide_action(user_input):
    if "覚えて" in user_input:
        return "memory"
    elif "調べて" in user_input:
        return "search"
    else:
        return "chat"
