"""
tim_llm_gateway.py

Minimum LLM gateway for TIM Runtime V1.

Responsibilities:
- receive runtime context
- build a prompt for the LLM
- call OpenAI API
- return plain response text

Rules:
- no memory logic here
- no state logic here
- no decision logic here
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request


_OPENAI_CHAT_URL = "https://api.openai.com/v1/chat/completions"
_DEFAULT_MODEL = "gpt-4o-mini"


def _build_prompt(context: dict) -> str:
    user_input = context.get("user_input", "")
    mode = context.get("mode", "conversation")
    memory = context.get("memory", [])
    state = context.get("state", {})

    memory_text = json.dumps(memory, ensure_ascii=False, indent=2)
    state_text = json.dumps(state, ensure_ascii=False, indent=2)

    return f"""You are TIM, an LLM-first strategic partner.

Mode:
{mode}

Relevant memory:
{memory_text}

Current state:
{state_text}

Current user input:
{user_input}

Respond naturally in Japanese.
Be helpful, clear, and practical.
"""


def send_to_llm(context: dict) -> str:
    if not isinstance(context, dict):
        raise TypeError("context must be a dict")

    api_key = (os.environ.get("OPENAI_API_KEY") or "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing or empty")

    prompt = _build_prompt(context)

    body = json.dumps(
        {
            "model": _DEFAULT_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
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

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI API request failed: {e.code} {err_body}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"OpenAI API connection failed: {e.reason}") from e

    try:
        data = json.loads(raw)
        content = data["choices"][0]["message"]["content"]
    except (json.JSONDecodeError, KeyError, IndexError, TypeError) as e:
        raise RuntimeError("OpenAI API returned unexpected response") from e

    text = content if isinstance(content, str) else str(content)

    if not text.strip():
        raise RuntimeError("OpenAI API returned empty content")

    return text
