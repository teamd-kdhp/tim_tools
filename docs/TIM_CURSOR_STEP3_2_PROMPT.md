You are working on TIM v2.

Read these files first and treat them as absolute constraints:
- docs/TIM_CURRENT_EXECUTION.md
- docs/TIM_LLM_GATEWAY_DESIGN.md
- docs/TIM_LLM_GATEWAY_IMPLEMENTATION_SPEC.md
- docs/TIM_MODULE_CONTRACTS.md
- docs/TIM_INTERFACES.md
- docs/TIM_HANDOFF_RULES.md

Current task:
Implement Step 3.2 minimal LLM gateway only.

Absolute rules:
- Modify ONLY: core/tim_llm_gateway.py
- Do NOT touch any other file
- Do NOT change architecture
- Do NOT add integrations beyond the minimal gateway
- Do NOT add Memory/State/Data/Connector usage
- Do NOT optimize
- Do NOT refactor
- Do NOT add retries, caching, logging, streaming, fallback, or extra abstractions
- Keep the module thin
- Final reasoning belongs to LLM, but this module is only the gateway

Process rule:
1. First output ONLY:
   - files to modify
   - exact implementation summary
   - any assumptions
2. Wait for approval
3. Do NOT write code until approval

Implementation target:
- one minimal function: send_to_llm
- input shape:
  {
    "prompt": str,
    "context": dict,
    "mode": str
  }
- output shape:
  {
    "response": str,
    "reasoning_summary": str,
    "confidence": float,
    "actions": list
  }

Keep it minimal.
