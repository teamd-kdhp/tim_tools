You are working on TIM v2.

Read these files first and treat them as absolute constraints:
- docs/TIM_CURRENT_EXECUTION.md
- docs/TIM_STATUS.md
- docs/TIM_BRAIN_LLM_DESIGN.md
- docs/TIM_BRAIN_LLM_IMPLEMENTATION_SPEC.md
- docs/TIM_MODULE_CONTRACTS.md
- docs/TIM_HANDOFF_RULES.md

Current task:
Implement Step 5.1 Brain LLM only.

Absolute rules:
- Modify ONLY:
  - core/tim_brain_llm.py
- Do NOT touch:
  - core/tim_brain.py
  - core/tim_core.py
  - core/tim_main.py
  - core/tim_llm_gateway.py
  - layers/*
  - connectors/*
  - docs/*
- Do NOT change architecture
- Do NOT add memory/state/data integration
- Do NOT answer the user directly
- Do NOT add tool calling
- Do NOT add multi-step planning
- Keep implementation minimal

Implementation target:
- create one callable function
- classify action into exactly one of:
  - memory
  - search
  - chat
- return:
  {
    "action": "...",
    "confidence": float,
    "reason": str
  }
- if invalid output, fallback to:
  {
    "action": "chat",
    "confidence": 0.0,
    "reason": "fallback"
  }

Process rule:
1. First output ONLY:
   - files to modify
   - exact implementation summary
   - assumptions
2. Wait for approval
3. Do NOT write code until approval

Keep it minimal.
