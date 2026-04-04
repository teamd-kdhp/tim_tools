# TIM MINIMAL CONVERSATION IMPLEMENTATION SPEC

## Current Step
Step 4.1: Minimal Conversation Implementation Spec

## Goal
Define the thinnest implementation spec for tim_main.py and tim_core.py only.

## Allowed Files
- core/tim_main.py
- core/tim_core.py

## Forbidden
- Do NOT modify tim_llm_gateway.py
- Do NOT modify layers
- Do NOT modify connectors
- Do NOT add Memory/State/Data integration
- Do NOT add prompt optimization
- Do NOT add business logic
- Do NOT add multi-turn handling
- Do NOT touch any other file

## tim_main.py Minimal Role
- expose a single callable entry
- accept raw user_input string
- pass user_input to tim_core.py
- return final text only

## tim_core.py Minimal Role
- accept raw user_input string
- build payload:
  {
    "prompt": user_input,
    "context": {},
    "mode": "conversation"
  }
- call send_to_llm(...)
- extract response fieldresponse text only

## Success Definition
1. Only core/tim_main.py and core/tim_core.py are modified
2. A raw string can flow through main → core → gateway
3. Final returned value is plain text
4. No other system is touched

