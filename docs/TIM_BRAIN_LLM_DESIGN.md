# TIM BRAIN LLM DESIGN

## Purpose
Define how TIM Brain will use LLM for action selection before implementation.

---

## Current State
- tim_brain.py uses fixed if/elif logic
- action choices:
  - memory
  - search
  - chat

---

## Goal
Replace fixed rule-based action selection with LLM-based action selection.

---

## New Module
- core/tim_brain_llm.py

---

## Responsibility
tim_brain_llm.py will:
- receive raw user_input
- ask LLM to classify intended action
- return one action string only

---

## Allowed Output Values
- "memory"
- "search"
- "chat"

No other values are allowed.

---

## Input
{
  "user_input": str
}

---

## Output
{
  "action": "memory" | "search" | "chat"
}

---

## Design Principle
1. Brain decides action only
2. Brain does not answer the user directly
3. Brain does not manage memory/state/data
4. Brain only classifies intent
5. If LLM output is invalid, fallback t---

## Minimal Prompt Requirement
LLM should be instructed to:
- classify the user intent
- return only one of:
  - memory
  - search
  - chat

---

## Non-Goals
- No Memory integration
- No State integration
- No Data Layer integration
- No tool calling
- No multi-step planning yet
- No final response generation

---

## Future Flow
user_input
→ tim_brain_llm.py
→ action
→ tim_core.py routes by action
→ downstream handler

