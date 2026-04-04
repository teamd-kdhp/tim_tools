# TIM LLM GATEWAY IMPLEMENTATION SPEC

## Current Step
Step 3.2: LLM Gateway Minimal Implementation

## Goal
Implement the thinnest possible working LLM gateway in core/tim_llm_gateway.py only.

## Scope
- One minimal callable function only
- One provider only for now
- Environment variable based API key loading
- Minimal request/response path only
- Normalize output to fixed structure

## Allowed File
- core/tim_llm_gateway.py only

## Forbidden
- Do NOT modify any other file
- Do NOT implement Memory integration
- Do NOT implement State integration
- Do NOT implement Context Builder integration
- Do NOT implement connector integration
- Do NOT implement retries, caching, logging, streaming, fallback, or optimization
- Do NOT change module contracts
- Do NOT redesign architecture

## Minimal Function
Function name:
send_to_llm

## Input
{
  "prompt": str,
  "context": dict,
  "mode": str
}

## Minimal Behavior
- Accept prompt/context/mode
- For initial implementation, context may be ignored except for safe placeholder handling
- Send prompt to LLM provider
- Receive text response
- Return normalized dict

## Output
{
  "response": str,
  "reasoning_summary": str,
  "confidence": float,
  "actions": list
}

## Output Rules
- response: actual returned text
- reasoning_summary: empty string allowed initially
- confidence: default 0.0 allowed initially
- actions: default empty list

## Provider Rule
- OpenAI only for initial implementation

## Configuration Rule
- API key must be loaded from environment variable only
- No hardcoded secrets
- No interactive input for secrets

## Failure Handling
- Raise clear exception on missing API key
- Raise clear exception on empty prompt
- Raise clear exception on provider failure
- Do NOT add custom recovery systems yet

## Success Definition
The module is complete for Step 3.2 only if:
1. core/tim_llm_gateway.py is the only modified file
2. a single function can be called with prompt/context/mode
3. the function returns the normalized output shape
4. no other module is touched

