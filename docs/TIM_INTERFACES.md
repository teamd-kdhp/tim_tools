# TIM INTERFACES

## Purpose
Define strict input/output formats between modules.
This prevents structure drift and Cursor misalignment.

---

## 1. Core Request

{
  "user_input": str,
  "timestamp": str,
  "session_id": str,
  "project_id": str | null
}

---

## 2. Context Builder Output

{
  "user_intent": str,
  "memory_context": list,
  "state_context": dict,
  "data_context": dict,
  "constraints": dict
}

---

## 3. LLM Gateway Input

{
  "prompt": str,
  "context": {
    "user_intent": str,
    "memory_context": list,
    "state_context": dict,
    "data_context": dict,
    "constraints": dict
  },
  "mode": str
}

---

## 4. LLM Gateway Output

{
  "response": str,
  "reasoning_summary": str,
  "confidence": float,
  "actions": list
}

---

## 5. Memory Layer

### Query Input
{
  "query": str,
  "limit": int
}

### Output
{
  "results": list
}

---

## 6. State Layer

### Query Input
{
  "session_id": str
}

### Output
{
  "current_step": str,
  "active_task": str,
  "progress": dict
}

---

## 7. Data Layer

### Input
{
  "source": str,
  "query": str,
  "options": dict
}

### Output
{
  "data": list,
  "metadata": dict
}

---

## Rules

1. All modules must follow these formats exactly
2. No module may redefine structure
3. No implicit fields allowed
4. All keys must be explicit
5. Cursor must NOT modify these formats

