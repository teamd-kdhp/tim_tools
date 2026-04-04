from tim_tools.core.tim_llm_gateway import send_to_llm
from tim_tools.core.tim_brain import decide_action


def handle_user_input(user_input):
    action = decide_action(user_input)

    if action == "memory":
        return "OK, 記憶しました"

    elif action == "search":
        return "検索機能はまだ未実装です"

    else:
        return send_to_llm({
            "prompt": user_input,
            "context": {},
            "mode": "conversation",
        })["response"]
