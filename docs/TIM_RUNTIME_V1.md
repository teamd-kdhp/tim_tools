# TIM RUNTIME V1

## 0. Purpose
TIM Runtime V1 defines the minimum runtime flow for an LLM-first TIM system.

Its purpose is:
- preserve ChatGPT-level conversation quality
- add memory and state continuity
- prepare for future Drive / Web / API / SaaS access
- avoid over-architecture in the initial implementation

TIM Runtime itself must not replace LLM thinking.
Its role is to prepare the right context so LLM can think well.

---

## 1. Core Principle

TIM Runtime does NOT think instead of the LLM.

TIM Runtime is responsible for:
- receiving user input
- detecting minimal mode/intent
- retrieving relevant memory
- retrieving current state
- building context
- sending context to LLM
- returning response
- updating memory and state

LLM remains responsible for:
- interpretation
- reasoning
- explanation
- judgment support
- natural conversation

---

## 2. Minimum Runtime Flow

User Input
  ↓
TIM Runtime
  ├ Intent / Mode Detection
  ├ Memory Retrieval
  ├ State Retrieval
  ├ Context Builder
  ├ LLM Gateway
  ├ Response Formatter
  ├ Memory Update
  └ State Update


---

## 3. Step-by-step Flow

### Step 1. User Input
Receive the latest user input.

### Step 2. Intent / Mode Detection
Detect minimal routing signals:
- Conversation Mode
- Command Mode

### Step 3. Memory Retrieval
Retrieve relevant memory only.

### Step 4. State Retrieval
Retrieve current working state.

### Step 5. Context Builder
Build minimal context:
- user_input
- memory
- state

### Step 6. LLM Gateway
Send context to LLM.

### Step 7. Response Formatter
Return natural response.

### Step 8. Memory Update
Store only important long-term info.

### Step 9. State Update
Update current working status.

---

## 4. Minimum Scope

Must:
- input
- memory
- state
- context
- llm

Not yet:
- Drive
- Web
- SaaS
- Execution

