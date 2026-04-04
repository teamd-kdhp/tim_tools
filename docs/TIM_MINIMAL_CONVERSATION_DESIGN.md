# TIM MINIMAL CONVERSATION DESIGN

## Purpose
Define the minimal working conversation path for TIM v2.

---

## Goal
Enable the smallest end-to-end path:

user_input
→ tim_main.py
→ tim_core.py
→ tim_llm_gateway.py
→ final_response

---

## Minimal Scope

### tim_main.py
Responsibility:
- accept raw user_input
- call tim_core.py
- return final response

### tim_core.py
Responsibility:
- accept raw user_input
- build the thinnest possible payload for tim_llm_gateway.py
- call send_to_llm(...)
- extract "response"
- return final text only

### tim_llm_gateway.py
Responsibility:
- already implemented
- send request to OpenAI
- return normalized dict

---

## Minimal Input Path

tim_main.py receives:
{
  "user_input": str
}

tim_core.py sends to gateway:
{
  "prompt": str,
  "context": {},
  "mode": "conversation"
}

---

## Minimal Output Path

tim_llm_gateway.py returns:
{
   "reasoning_summary": str,
  "confidence": float,
  "actions": list
}

tim_core.py returns:
- response only (str)

tim_main.py returns:
- final response only (str)

---

## Non-Goals
The minimal conversation path must NOT:
- use Memory
- use State
- use Context Builder
- use Data Layer
- use any connector
- implement business-specific logic
- implement multi-turn conversation state
- implement advanced formatting

---

## Design Principle
1. Keep the path as short as possible
2. Prove that TIM can talk end-to-end
3. Delay all enrichment until later steps
4. Do not expand scope

---

## Cursor Rule
When implementing later:
- modify only core/tim_main.py and core/tim_core.py
- do not touch gateway unless explicitly required
- no other modules may be edited
- no additional abstractions

