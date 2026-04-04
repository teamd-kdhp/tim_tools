"""
tim_llm_gateway.py
Single gateway to LLM provider.
"""

from __future__ import annotations
import json
import os
import urllib.error
import urllib.request

_OPENAI_CHAT_URL = "https://api.openai.com/v1/chat/completions"
_DEFAULT_MODEL = "gpt-4o-mini"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_PATH = os.path.join(BASE_DIR, "memory", "conversation_memory.json")

MAX_CONTEXT_MESSAGES = 20

IMPORTANT_KEYWORDS = [
    "覚えて",
    "重要",
    "忘れるな",
    "remember",
    "important",
]


def build_context(memory):
    return memory[-MAX_CONTEXT_MESSAGES:]


def is_important(text):
    return any(k in text for k in IMPORTANT_KEYWORDS)


def add_user_message(memory, prompt):
    memory.append({
        "role": "user",
        "content": prompt,
        "important": is_important(prompt),
    })


def add_assistant_message(memory, reply):
    memory.append({
        "role": "assistant",
        "content": reply,
        "important": False,
    })


def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return []
    with open(MEMORY_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data if isinstance(data, list) else []


def save_memory(memory):
    parent = os.path.dirname(MEMORY_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)


def send_to_llm(payload: dict) -> dict:
    if not isinstance(payload, dict):
        raise TypeError("payload must be a dict")

    prompt = payload.get("prompt")
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("prompt must be a non-empty string")

    api_key = (os.environ.get("OPENAI_API_KEY") or "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing or empty")

    memory = load_memory()
    add_user_message(memory, prompt)
    context = build_context(memory)

    api_messages = [{"role": m["role"], "content": m["content"]} for m in context]

    body = json.dumps({
        "model": _DEFAULT_MODEL,
        "messages": api_messages,
    }).encode("utf-8")

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
    except json.JSONDecodeError as e:
        raise RuntimeError("OpenAI API returned invalid JSON") from e

    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as e:
        raise RuntimeError("OpenAI API returned an unexpected response shape") from e

    text = "" if content is None else (content if isinstance(content, str) else str(content))

    if not text.strip():
        raise RuntimeError("OpenAI API returned empty assistant content")

    add_assistant_message(memory, text)
    save_memory(memory)

    return {
        "response": text,
        "reasoning_summary": "",
        "confidence": 0.0,
        "actions": [],
    }
