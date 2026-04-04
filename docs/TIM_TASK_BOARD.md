# TIM TASK BOARD

## Step 2: File Structure Design

### Goal
Define stable file/module structure for TIM v2 before implementation.

### Scope
- Define top-level files
- Define module responsibilities
- Define dependency boundaries
- Avoid premature implementation

### Planned Core Files

1. tim_main.py
- Entry point
- Receives user input
- Calls TIM core

2. tim_core.py
- Central orchestrator
- Controls flow between layers
- Builds final response pipeline

3. tim_llm_gateway.py
- Wrapper for LLM communication
- Sends prompts
- Receives responses

4. tim_memory_layer.py
- Handles long-term memory
- Stores and retrieves persistent information

5. tim_state_layer.py
- Handles current task state
- Tracks active project / phase / progress

6. tim_context_builder.py
- Collects memory + state + external data
- Builds optimized context for LLM

7. tim_data_layer.py
- Central access layer for external data
- Connects Drive / Web / SaaS / DB

8. tim_drive_connector.py
- Retrieves documents from Drive

9. tim_web_connector.py
- Retrieves web information

10. tim_saas_connector.py
- Retrieves SaaS data (e.g. accounting, CRM)

11. tim_executor_connector.py
- Future execution layer
- Sends instructions to other systems

### Dependency Rule

tim_main.py
→ tim_core.py
→ tim_context_builder.py
→ tim_memory_layer.py
→ tim_state_layer.py
→ tim_data_layer.py
→ connectors
→ tim_llm_gateway.py

### Constraints

- Do NOT implement code yet
- Do NOT define detailed methods yet
- Do NOT add new agents yet
- Do NOT jump to Step 3

