"""
tim_main.py

Official entry point for TIM Runtime V1.

Responsibilities:
- receive user input
- call TIM runtime
- print user-facing response

Rules:
- no memory logic here
- no state logic here
- no context logic here
- no LLM logic here
"""

from core.tim_runtime import run_tim


def handle_user_input(user_input: str) -> dict:
    return run_tim(user_input)


if __name__ == "__main__":
    user_input = input("TIM > ")
    result = handle_user_input(user_input)
    print(result["response_text"])
