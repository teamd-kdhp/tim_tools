# TIM LLM GATEWAY DESIGN

## Purpose
Define the minimal design of tim_llm_gateway.py before implementation.

---

## Module
core/tim_llm_gateway.py

---

## Responsibility
tim_llm_gateway.py is the ONLY module allowed to communicate with the LLM provider.

It is responsible for:
- receiving structured prompt input
- sending request to LLM provider
- receiving raw response
- normalizing response structure
- returning normalized LLM output

---

## Non-Responsibility
tim_llm_gateway.py must NOT:
- manage memory
- manage state
- access connectors
- make business decisions outside LLM reasoning
- own orchestration flow
- perform prompt optimization at this stage

---

## Input Contract
tim_llm_gateway.py receives:

{
  "prompt": str,
  "context": dict,
  "mode": str
}

### Field Meaning
- prompt: final prompt text to send
- context: structured supporting context
- mode: gateway mode such as "conversation" or "command"

---

## Output Contract
tim_llm_gateway.py returns:

{
  "response": str,
  "reasoning_summary": str,
  "confidence": float,
  "actions": list
}

### Field Meaning
- response: user-facing main text
- reasoning_summary: short internal summary
- confidence: numeric confidence estimate
- actions: extracted next-action candidates if any

---

## Allowed Dependencies
- External LLM SDK / API client only

---

## Forbidden Dependencies
- tim_memory_layer.py
- tim_state_layer.py
- tim_data_layer.py
- any connector
- business-specific modules

---

## Error Policy
At the design stage, the module must be prepared to handle:
- provider connection failure
- invalid response shape
- timeout
- empty response

But implementation is NOT allowed yet.

---

## Design Principle
1. LLM access must be centralized
2. Final reasoning must pass through this module
3. The module must stay thin
4. The module must not become an orchestrator
5. The module must not absorb unrelated business logic

---

## Cursor Rule
When implementing this module later:
- modify core/tim_llm_gateway.py only
- do not touch any other module unless explicitly instructed
- implement minimal path first
- no optimization beyond current step

