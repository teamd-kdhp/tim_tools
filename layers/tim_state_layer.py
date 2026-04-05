"""
tim_state_layer.py

Minimum state layer for TIM Runtime V1.

Responsibilities:
- load current working state
- save updated state
- return compact dict state

Rules:
- no LLM call here
- no memory logic here
- no decision logic here
"""

from __future__ import annotations

import json
from pathlib import Path


_STATE_PATH = Path("state/tim_state.json")


def load_state() -> dict:
    if not _STATE_PATH.exists():
        return {}

    try:
        with _STATE_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}

    return data if isinstance(data, dict) else {}


def save_state(state: dict) -> None:
    if not isinstance(state, dict):
        raise TypeError("state must be a dict")

    _STATE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with _STATE_PATH.open("w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
