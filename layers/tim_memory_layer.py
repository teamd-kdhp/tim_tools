import json
import os

_PACKAGE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY_PATH = os.path.join(_PACKAGE_ROOT, "memory", "conversation_memory.json")

def _load_all():
    parent = os.path.dirname(MEMORY_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)

    if not os.path.exists(MEMORY_PATH):
        return []

    with open(MEMORY_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

    return data if isinstance(data, list) else []

def _save_all(data):
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def _is_preference_memory(text: str) -> bool:
    if not isinstance(text, str):
        return False

    keywords = [
        "好き",
        "嫌い",
        "苦手",
        "得意",
        "推し",
        "趣味",
        "色",
        "食べ物",
    ]
    return any(k in text for k in keywords)

def append_memory(content: str) -> None:
    if not isinstance(content, str):
        return

    data = _load_all()

    # 好み・嗜好系の記憶は最新で上書きする
    if _is_preference_memory(content):
        filtered = []
        for item in data:
            if not isinstance(item, dict):
                continue
            old_content = item.get("content", "")
            if _is_preference_memory(old_content):
                continue
            filtered.append(item)
        data = filtered

    data.append({
        "role": "user",
        "content": content,
        "important": True
    })

    _save_all(data)

def load_memory_context(limit: int = 20):
    data = _load_all()
    cleaned = []

    for item in data:
        if not isinstance(item, dict):
            continue
        role = item.get("role")
        content = item.get("content")
        if role in ("user", "assistant") and isinstance(content, str) and content.strip():
            cleaned.append({
                "role": role,
                "content": content
            })

    return cleaned[-limit:]