# TIM BRAIN LLM IMPLEMENTATION SPEC

## Current Step
Step 5.1: Brain LLM Implementation Spec

## Goal
Implement a new module that classifies user intent into one of:
- memory
- search
- chat

## Allowed File
- core/tim_brain_llm.py only

## Forbidden
- Do NOT modify tim_brain.py
- Do NOT modify tim_core.py
- Do NOT modify tim_main.py
- Do NOT modify tim_llm_gateway.py
- Do NOT modify layers
- Do NOT modify connectors
- Do NOT add Memory integration
- Do NOT add State integration
- Do NOT add Data Layer integration
- Do NOT add final response generation
- Do NOT expand scope beyond action classification

## Responsibility
tim_brain_llm.py must:
- accept raw user_input
- optionally accept lightweight conversation context
- call LLM for action classification
- return normalized action output only

## Input
{
  "user_input": str,
  "conversation_history": list,
  "memory_summary": str
}

For the minimal version:
- conversation_history may be ignored safely
- memory_summary may be ignored safely

## Output
{
  "action": "memory" | "search" | "chat",
  "confidence": float,
  "reason": str
}

## Output Rules
- If LLM returns invalid output, fallback to:
  {
    "action": "chat",
    "confidence": 0.0,
    "reason": "fallback"
  }

## Prompt Rule
The LLM must be instructed to classify into exactly one of:
- memory
- search
- chat

## Success Definition
1. Only core/tim_brain_llm.py is created/modified
2. The module returns normalized JSON-like dict output
3. Invalid LLM output falls back to chat
4. No other file is touched

