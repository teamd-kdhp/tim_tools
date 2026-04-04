# TIM MODULE CONTRACTS

## Purpose
Define file-level responsibilities, inputs, outputs, and dependency boundaries for TIM v2.
This document is for Step 2 only.
No implementation is allowed here.

---

## 1. tim_main.py

### Responsibility
- Entry point of TIM v2
- Receive user input
- Call tim_core.py
- Return final output to user

### Input
- user_input
- runtime options (optional)

### Output
- final_response

### Allowed Dependencies
- tim_core.py

### Forbidden
- Direct connector access
- Direct memory/state access
- Direct LLM call

---

## 2. tim_core.py

### Responsibility
- Central orchestrator
- Interpret request flow
- Call context builder
- Call LLM gateway
- Build final response pipeline

### Input
- user_input
- session/project context (optional)

### Output
- final_response
- internal execution summary

### Allowed Dependencies
- tim_context_builder.py
- tim_llm_gateway.py

### Forbidden
- Direct file parsing
- Direct web scraping
- Direct SaaS logic
- Hardcoded decision logic

---

## 3. tim_llm_gateway.py

### Responsibility
- Single gateway to LLM provider
- Send structured prompt/context
- Receive and normalize LLM response

### Input
- prompt
- structured context
- mode/options

### Output
- llm_response

### Allowed Dependencies
- External LLM SDK / API client only

### Forbidden
- Memory logic
- State logic
- Connector logic
- Business decision ownership outside LLM reasoning

---

## 4. tim_memory_layer.py

### Responsibility
- Store and retrieve long-term memory
- Manage memory categories
- Provide relevant memory records

### Input
- memory query
- memory update payload

### Output
- memory records
- update result

### Allowed Dependencies
- Memory storage backend only

### Forbidden
- Direct LLM call
- Direct connector call
- Current session state ownership

---

## 5. tim_state_layer.py

### Responsibility
- Store and retrieve current working state
- Track active project / step / progress / pending items

### Input
- state query
- state update payload

### Output
- current state snapshot
- update result

### Allowed Dependencies
- State storage backend only

### Forbidden
- Long-term memory ownership
- Direct LLM call
- Direct connector call

---

## 6. tim_context_builder.py

### Responsibility
- Build optimized context for LLM
- Pull from memory, state, and data layer
- Filter noise
- Prepare structured context package

### Input
- user_input
- project/session hint (optional)

### Output
- structured_context

### Allowed Dependencies
- tim_memory_layer.py
- tim_state_layer.py
- tim_data_layer.py

### Forbidden
- Final response generation
- Direct user output
- Independent decision making

---

## 7. tim_data_layer.py

### Responsibility
- Unified access layer for external/internal data
- Route requests to proper connector
- Normalize retrieved data

### Input
- data request
- source type
- query constraints

### Output
- normalized data payload

### Allowed Dependencies
- tim_drive_connector.py
- tim_web_connector.py
- tim_saas_connector.py
- future db connector

### Forbidden
- Final reasoning
- Memory ownership
- State ownership
- Direct user-facing response generation

---

## 8. tim_drive_connector.py

### Responsibility
- Retrieve data from Drive
- Search files
- Read supported document content
- Return raw/normalized file content

### Input
- file query
- folder scope
- retrieval options

### Output
- drive results
- file content
- metadata

### Allowed Dependencies
- Drive SDK / API client only

### Forbidden
- Final reasoning
- LLM call
- Cross-layer orchestration

---

## 9. tim_web_connector.py

### Responsibility
- Retrieve web information
- Execute search
- Fetch content
- Return source-aware payload

### Input
- search query
- retrieval options

### Output
- web results
- content
- metadata / sources

### Allowed Dependencies
- Web search / fetch tools only

### Forbidden
- Final reasoning
- LLM call
- State updates

---

## 10. tim_saas_connector.py

### Responsibility
- Retrieve data from authenticated SaaS systems
- Normalize SaaS outputs

### Input
- SaaS query
- source/system identifier
- access options

### Output
- normalized SaaS data
- metadata

### Allowed Dependencies
- SaaS API / integration client only

### Forbidden
- Final reasoning
- LLM call
- Business logic ownership

---

## 11. tim_executor_connector.py

### Responsibility
- Future execution bridge
- Send approved actions to external execution systems

### Input
- approved action payload

### Output
- execution result
- execution log reference

### Allowed Dependencies
- External execution client only

### Forbidden
- Autonomous decision making
- Triggering execution without approval
- LLM reasoning ownership

---

## Global Dependency Direction

tim_main.py
→ tim_core.py
→ tim_context_builder.py
→ (tim_memory_layer.py + tim_state_layer.py + tim_data_layer.py)
→ connectors
→ tim_llm_gateway.py

---

## Global Rules

1. Final reasoning belongs to LLM via tim_llm_gateway.py
2. tim_core.py orchestrates but does not hardcode business logic
3. Connectors retrieve data only
4. Memory and State are separate
5. No module may silently expand scope
6. No implementation is allowed based on this document alone

