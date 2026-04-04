# TIM CURRENT EXECUTION

## Objective
Replace the current rule-based brain with an LLM-based action selection brain.

## Current Development Phase
BRAIN LLM DESIGN PHASE

## Current Step
Step 5: Brain LLM Design

## Task
Define how tim_brain_llm.py will classify user intent into one of:
- memory
- search
- chat

## Scope
- Design brain LLM behavior only
- Define input/output shape
- Define fallback behavior
- Keep routing responsibility separate from response generation

## In Scope Now
- tim_brain_llm.py design
- action classification design
- fallback-to-chat rule
- Brain-only responsibility

## Out of Scope Now
- No Memory redesign
- No State Layer work
- No Data Layer work
- No connector work
- No prompt optimization beyond action classification
- No final response generation inside brain

## Constraints
- Do NOT implement code yet
- Do NOT modify other modules yet
- Do NOT expand scope beyond Brain LLM design

## Single Source of Truth
CURRENT_EXECUTION is absolute.
