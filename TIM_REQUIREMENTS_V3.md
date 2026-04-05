# TIM REQUIREMENTS (v1 - Simplified)

## Purpose

- Maintain ChatGPT-level natural conversation
- Do NOT degrade LLM performance
- Add minimal context only when needed

---

## System Structure

User
 ↓
TIM (minimal)
 ├ context_selector
 ├ prompt_builder
 ├ data_fetcher (optional)
 ↓
LLM (100% thinking)
 ↓
Output

---

## TIM Responsibilities

- Receive input
- Select minimal context (if needed)
- Build prompt
- Call LLM
- Return response

---

## What TIM MUST NOT do

- Think
- Analyze deeply
- Interpret intent with complex logic
- Inject unnecessary data

---

## Context Types

- Thinking
- Topic
- Instruction

---

## Context Rules

- Default = none
- Topic > Thinking
- Avoid combining both unless necessary
- Keep each context under 5 lines

---

## Data Access (future)

- Web
- Drive
- API

Rule:
→ Fetch only when needed
→ LLM interprets, not TIM

---

## Memory / State

NOT USED in v1

---

## Success Condition

- Feels like ChatGPT
- No unnatural behavior
- No over-control
- Works naturally

---

## Definition

TIM = Minimal LLM Orchestrator
