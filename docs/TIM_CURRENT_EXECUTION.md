# TIM CURRENT EXECUTION

## Objective
Define the minimal conversation flow of TIM before wider integration.

## Current Development Phase
MINIMAL CONVERSATION DESIGN PHASE

## Current Step
Step 4: Minimal Conversation

## Task
Define the minimal end-to-end conversation path using tim_main.py, tim_core.py, and tim_llm_gateway.py only.

## Scope
- Define minimal request flow
- Define minimal responsibility split between main/core/gateway
- Define the exact input/output path
- Keep implementation scope as small as possible

## In Scope Now
- tim_main.py design
- tim_core.py design
- minimal conversation flow design
- response path definition only

## Out of Scope Now
- No Memory integration
- No State integration
- No Context Builder integration
- No Data Layer integration
- No connectors
- No prompt optimization
- No advanced orchestration
- No multi-turn memory behavior

## Constraints
- Do ent code yet
- Do NOT modify other modules yet
- Do NOT jump to Step 5+
- Do NOT expand scope beyond minimal conversation flow

## Required Development Order
Step 1: Architecture Fix
Step 2: File Structure
Step 3.1: LLM Gateway Design
Step 3.2: LLM Gateway Minimal Implementation
Step 4: Minimal Conversation
Step 5: Memory Layer
Step 6: State Layer
Step 7: Data Layer
Step 8: Context Builder
Step 9: Thinking Template Optimization

## Single Source of Truth
CURRENT_EXECUTION is absolute.
