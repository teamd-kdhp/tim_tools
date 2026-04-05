import json
from datetime import datetime
from pathlib import Path

from openai import OpenAI

from core.context_selector import select_context
from core.prompt_builder import build_prompt


MODEL_NAME = "gpt-4o-mini"
BASE = Path("/Users/agent-a/openclaw/tim_tools")
LOG_PATH = BASE / "logs" / "context_log.jsonl"

client = OpenAI()


def _read_start_prompt():
    return (BASE / "TIM_START_PROMPT.md").read_text(encoding="utf-8")


def _call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": _read_start_prompt(),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()


def run(user_input: str):
    selected = select_context(user_input)
    prompt = build_prompt(user_input, selected)

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "time": datetime.utcnow().isoformat(),
            "input": user_input,
            "prompt_length": len(prompt)
        }, ensure_ascii=False) + "\n")

    response_text = _call_llm(prompt)

    return {
        "response_text": response_text,
    }
