You are continuing development of the TIM system.

You MUST strictly follow ALL rules below.

--------------------------------------------------
## 🔴 FIRST RESPONSE FORMAT (MANDATORY)
--------------------------------------------------

You MUST output ONLY:

1. Current state
2. Current development phase
3. Current step
4. Active task
5. Current structure (TIM / Layers)
6. ONE relevant file and WHY

DO NOT:
- Start implementation
- Expand scope
- Add new agents
- Jump ahead of CURRENT_EXECUTION

--------------------------------------------------
## 🔴 CORE DESIGN
--------------------------------------------------

TIM is NOT a simple chatbot.
TIM is an LLM-centered strategic commander system.

Structure:

User
  ↓
TIM (only dialogue interface)
  ├ Conversation Core (LLM)
  ├ Memory Layer
  ├ State Layer
  ├ Data Layer
  │   ├ Web Connector
  │   ├ Drive Connector
  │   ├ Internal DB Connector
  │   └ SaaS Connector
  └ Executor Connector (future)

--------------------------------------------------
## 🔴 CORE PRINCIPLE
--------------------------------------------------

TIM intelligence MUST come from LLM reasoning.

TIM itself must NOT become a rule-based decision engine.

TIM must:
- gather context
- organize context
- let LLM reason
- return practical answers

--------------------------------------------------
## 🔴 DEVELOPMENT ORDER (MANDATORY)
--------------------------------------------------

Step 1: Architecture Fix
Step 2: File Structure
Step 3: LLM Gateway
Step 4: Minimal Conversation
Step 5: Memory Layer
Step 6: State Layer
Step 7: Data Layer
Step 8: Context Builder
Step 9: Thinking Template Optimization

You MUST NOT:
- skip steps
- reorder steps
- optimize prompts before LLM integration
- implement advanced design before the current step is complete

--------------------------------------------------
## 🔴 CURRENT_EXECUTION RULE
--------------------------------------------------

CURRENT_EXECUTION is the single source of truth.

You MUST:
- follow CURRENT_EXECUTION strictly
- work on ONLY the current step
- refuse scope expansion implicitly by staying inside scope

If CURRENT_EXECUTION conflicts with anything else:
→ CURRENT_EXECUTION wins

--------------------------------------------------
## 🔴 IMPLEMENTATION STYLE
--------------------------------------------------

User is NOT an engineer.

Therefore:
- Give copy-paste commands only
- One step at a time
- No manual editing assumptions
- No skipped steps

--------------------------------------------------
## 🔴 FINAL RULE
--------------------------------------------------

At every new thread start:
- First confirm current development phase
- Then confirm current step
- Then confirm active task
- Then identify one relevant file
- Then stop
