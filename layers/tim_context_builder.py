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

    return {
        "user_input": user_input,
        "mode": mode,
        "memory": memory,
        "state": state,
    }
