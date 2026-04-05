"""
tim_context_builder.py

Minimum context builder for TIM Runtime V1.

Responsibilities:
- receive runtime inputs
- assemble minimum context payload for LLM
- keep context compact and structured

Rules:
- no LLM call here
- no memory retrieval here
- no state retrieval here
- no decision logic here
"""


def _trim_memory(memory: list, limit: int = 5) -> list:
    if not isinstance(memory, list):
        return []
    return memory[-limit:]


def _trim_state(state: dict) -> dict:
    if not isinstance(state, dict):
        return {}

    allowed_keys = [
        "current_project",
        "phase",
        "next_action",
        "pending",
        "blocked",
        "unresolved_items",
    ]

    trimmed = {}
    for key in allowed_keys:
        if key in state:
            trimmed[key] = state[key]

    return trimmed


def _build_llm_instruction(mode: str) -> str:
    if mode == "command":
        return (
            "Respond in Japanese. Be practical and structured. "
            "If useful, provide next actions clearly."
        )

    return (
        "Respond in Japanese. Be natural, helpful, and clear. "
        "Keep the tone conversational but practical."
    )


def build_context(
    *,
    user_input: str,
    mode: str,
    memory: list,
    state: dict,
) -> dict:
    if not isinstance(user_input, str):
        raise TypeError("user_input must be a str")

    if not isinstance(mode, str):
        raise TypeError("mode must be a str")

    if not isinstance(memory, list):
        raise TypeError("memory must be a list")

    if not isinstance(state, dict):
        raise TypeError("state must be a dict")

    trimmed_memory = _trim_memory(memory)
    trimmed_state = _trim_state(state)
    llm_instruction = _build_llm_instruction(mode)

    return {
        "user_input": user_input,
        "mode": mode,
        "memory": trimmed_memory,
        "state": trimmed_state,
        "llm_instruction": llm_instruction,
    }
