"""
tim_main.py

TIM v2 entry point.

Responsibility:
- Receive user input
- Pass input to tim_core.py
- Return final response

Rules:
- No direct connector access
- No direct LLM call
- No direct memory/state access
"""

from . import tim_core


def handle_user_input(user_input: str) -> str:
    return tim_core.handle_user_input(user_input)
