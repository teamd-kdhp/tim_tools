"""
tim_runtime.py

TIM Runtime V1
LLM-first minimum runtime orchestration layer.

Responsibilities:
- receive user input
- detect minimal mode
- retrieve relevant memory
- retrieve current state
- build context
- call LLM gateway
- format response
- update memory
- update state

Important:
- Runtime does NOT replace LLM thinking
- Runtime prepares context so LLM can think well
"""

from layers.tim_memory_layer import load_memory_context
from layers.tim_state_layer import load_state
from layers.tim_context_builder import build_context
from core.tim_llm_gateway import send_to_llm


def detect_mode(user_input: str) -> str:
    """
    Minimal mode detection.
    Returns:
        - "conversation"
        - "command"
    """
    return "conversation"


def run_tim(user_input: str) -> dict:
    """
    Main minimum runtime flow.
    """
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

    return {
        "response_text": llm_result,
        "memory_updates": [],
        "state_updates": {},
        "used_sources": [],
    }
