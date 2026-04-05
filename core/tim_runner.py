from pathlib import Path

from openai import OpenAI


MODEL_NAME = "gpt-4o-mini"
BASE = Path("/Users/agent-a/openclaw/tim_tools")

client = OpenAI()


def _read_start_prompt() -> str:
    return (BASE / "TIM_START_PROMPT.md").read_text(encoding="utf-8")


def run(user_input: str) -> dict:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": _read_start_prompt(),
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
        temperature=0.7,
    )

    return {
        "response_text": response.choices[0].message.content.strip(),
    }
