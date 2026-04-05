"""
tim_llm_gateway.py

Minimum LLM gateway for TIM Runtime V1.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request


_OPENAI_CHAT_URL = "https://api.openai.com/v1/chat/completions"
_DEFAULT_MODEL = "gpt-4o-mini"


def _post_chat(messages: list[dict]) -> str:
    api_key = (os.environ.get("OPENAI_API_KEY") or "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing")

    body = json.dumps(
        {
            "model": _DEFAULT_MODEL,
            "messages": messages,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        _OPENAI_CHAT_URL,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )

    with urllib.request.urlopen(req, timeout=120) as resp:
        raw = resp.read().decode("utf-8")

    data = json.loads(raw)
    content = data["choices"][0]["message"]["content"]

    if not isinstance(content, str) or not content.strip():
        raise RuntimeError("OpenAI API returned empty content")

    return content.strip()


def _build_prompt(context: dict) -> str:
    user_input = context.get("user_input", "")
    mode = context.get("mode", "conversation")
    memory = context.get("memory", [])
    state = context.get("state", {})
    instruction = context.get("llm_instruction", "")

    memory_text = json.dumps(memory, ensure_ascii=False, indent=2)
    state_text = json.dumps(state, ensure_ascii=False, indent=2)

    return f"""You are TIM, an LLM-first strategic partner.

Instruction:
{instruction}

Mode:
{mode}

Relevant memory:
{memory_text}

Current state:
{state_text}

User input:
{user_input}

Respond now.
"""


def send_to_llm(context: dict) -> str:
    prompt = _build_prompt(context)
    return _post_chat(
        [
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )


def should_store_memory(text: str) -> bool:
    if not isinstance(text, str):
        return False

    text = text.strip()
    if not text:
        return False

    prompt = f"""You are deciding whether a user message should be stored as long-term memory for TIM.

Store only if the message is likely to remain useful in future conversations.

Examples that SHOULD be stored:
- stable preferences
- work style
- personal policy
- recurring project background
- important long-term facts
- durable business context

Examples that should NOT be stored:
- greetings
- one-off casual chat
- temporary emotion
- trivial short response
- low-value filler

User message:
{text}

Answer ONLY with:
YES
or
NO
"""

    result = _post_chat(
        [
            {
                "role": "user",
                "content": prompt,
            }
        ]
    ).upper()

    return result.startswith("YES")
