"""
tim_main.py

TIM v2 entry point.

Responsibility:
- Receive user input
- Pass input to TIMBrain
- Return final response

Rules:
- No direct connector access
- No direct LLM call
- No direct memory/state access
"""

from legacy.tim_brain import TIMBrain


def handle_user_input(user_input: str):
    brain = TIMBrain()
    return brain.process(user_input)
