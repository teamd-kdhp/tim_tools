from tim_tools.core.tim_llm_gateway import send_to_llm
from tim_tools.core.tim_brain_llm import classify_intent
from tim_tools.layers.tim_memory_layer import append_memory, load_memory_context

def handle_user_input(user_input):
    result = classify_intent({
        "user_input": user_input,
        "conversation_history": [],
        "memory_summary": "",
    })

    action = result["action"]

    if action == "memory":
        append_memory(user_input)
        return "OK, 記憶しました"

    elif action == "search":
        return "検索機能はまだ未実装です"

    else:
        memory = load_memory_context()
        memory_text = "\n".join(
            [f"{m['role']}: {m['content']}" for m in memory]
        )

        prompt = f"""Past memory:
{memory_text}

Current user input:
{user_input}

Answer the current user naturally, while using the past memory if relevant.
"""

        return send_to_llm({
            "prompt": prompt,
            "context": {},
            "mode": "conversation",
        })["response"]