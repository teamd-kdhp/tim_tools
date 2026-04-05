"""
tim_runtime.py

TIM Runtime V1
LLM-first minimum runtime orchestration layer.
"""

from layers.tim_memory_layer import load_memory_context, append_memory_entry
from layers.tim_state_layer import load_state
from layers.tim_context_builder import build_context
from core.tim_llm_gateway import send_to_llm, should_store_memory


def detect_mode(user_input: str) -> str:
    return "conversation"


def run_tim(user_input: str) -> dict:
    mode = detect_mode(user_input)
    memory = load_memory_context()
    state = load_state()

    context = build_context(
        user_input=user_input,
        mode=mode,
        memory=memory,
        state=state,
    )

    llm_result = send_to_llm(context)

    stored_entries = []

    if should_store_memory(user_input):
        append_memory_entry("user", user_input)
        stored_entries.append({"role": "user", "content": user_input})

    return {
        "response_text": llm_result,
        "memory_updates": stored_entries,
        "state_updates": {},
        "used_sources": [],
    }
