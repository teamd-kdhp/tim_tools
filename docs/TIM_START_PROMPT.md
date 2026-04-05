You are continuing development of the TIM system.

Before doing anything, you MUST read:
- docs/TIM_CONSTITUTION.md
- docs/TIM_REQUIREMENTS_V3.md
- docs/TIM_STATUS.md
- docs/TIM_CURRENT_EXECUTION.md

CRITICAL PRINCIPLES

- TIM is LLM-first
- TIM is the only dialogue interface
- TIM must not become a rule-based decision engine
- TIM must not become a degraded wrapper around ChatGPT
- Brain architecture is optional
- The real goal is to extend LLM with memory, state, and data access

If any old implementation conflicts:
- Constitution wins

If any implementation weakens LLM-centered usefulness:
- Reject that direction

IMPLEMENTATION PHILOSOPHY

TIM should be:
- LLM-centered conversation core
- memory extension
- current-state awareness
- internal/external information access
- future execution layer

TIM's value:
- remembering
- tracking current work
- fetching needed information
- helping the user think and act better

DO NOT

- do not assume old architecture is correct
- do not force Brain/Agent design
- do not add rigid rule-based logic
- do not expand scope without confirmation
- do not degrade conversation quality

FIRST RESPONSE FORMAT (MANDATORY)

You MUST output ONLY:
1. Current state
2. Current development phase
3. Current step
4. Active task
5. Current valid architecture
6. ONE relevant file and WHY

Do NOT:
- start implementation immediately
- expand scope
- redesign casually

FINAL RULE

TIM is not a workflow bot.
TIM is the user's strategic partner.
Always preserve that direction.

