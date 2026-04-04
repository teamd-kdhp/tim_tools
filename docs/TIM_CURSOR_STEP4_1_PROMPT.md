You are working on TIM v2.

Read these files first and treat them as absolute constraints:
- docs/TIM_CURRENT_EXECUTION.md
- docs/TIM_MINIMAL_CONVERSATION_DESIGN.md
- docs/TIM_MINIMAL_CONVERSATION_IMPLEMENTATION_SPEC.md
- docs/TIM_MODULE_CONTRACTS.md
- docs/TIM_INTERFACES.md
- docs/TIM_HANDOFF_RULES.md

Current task:
Implement Step 4.1 minimal conversation only.

Absolute rules:
- Modify ONLY:
  - core/tim_main.py
  - core/tim_core.py
- Do NOT touch:
  - core/tim_llm_gateway.py
  - layers/*
  - connectors/*
  - any docs
- Do NOT change architecture
- Do NOT add Memory/State/Data integration
- Do NOT add prompt optimization
- Do NOT add business logic
- Do NOT add multi-turn behavior
- Do NOT refactor anything else
- Keep implementation minimal

Implementation target:

1) core/tim_core.py
- expose one callable function
- accept raw user_input: str
- build payload:
  {
    "prompt": user_i"context": {},
    "mode": "conversation"
  }
- call send_to_llm(...)
- extract payload["response"]
- return plain text only

2) core/tim_main.py
- expose one callable function
- accept raw user_input: str
- call tim_core.py
- return plain text only

Process rule:
1. First output ONLY:
   - files to modify
   - exact implementation summary
   - assumptions
2. Wait for approval
3. Do NOT write code until approval

Keep it minimal.
