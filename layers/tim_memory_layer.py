"""
tim_memory_layer.py

Minimum memory layer for TIM Runtime V1.

Responsibilities:
- load memory context
- save memory context
- append conversation entries

Rules:
- no LLM call here
- no state logic here
- no decision logic here
"""

from __future__ import annotations

import json
from pathlib import Path


_MEMORY_PATH = Path("memory/conversation_memory.json")


def load_memory_context() -> list:
    if not _MEMORY_PATH.exists():
        return []

    try:
        with _MEMORY_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

    return data if isinstance(data, list) else []


def save_memory_context(memory: list) -> None:
    if not isinstance(memory, list):
        raise TypeError("memory must be a list")

    _MEMORY_PATH.parent.mkdir(parents=True, exist_ok=True)

    with _MEMORY_PATH.open("w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)


def append_memory_entry(role: str, content: str) -> None:
    if role not in ("user", "assistant"):
        raise ValueError("role must be 'user' or 'assistant'")

    if not isinstance(content, str):
        raise TypeError("content must be a str")

    text = content.strip()
    if not text:
        return

    memory = load_memory_context()
    memory.append(
        {
            "role": role,
            "content": text,
        }
    )
    save_memory_context(memory)
