# TIM STATUS

## Current State
TIM currently supports:
- minimal end-to-end conversation
- OpenAI-based LLM gateway
- routing via tim_core.py
- action classification via tim_brain_llm.py
- explicit memory persistence
- memory context injection into chat prompt
- overwrite behavior for preference-type memory
- GitHub sync workflow between MacBook and Mac mini

## Current Working Flow
run_tim.py
→ tim_main.py
→ tim_core.py
→ tim_brain_llm.py
→ route by action
  - memory → append_memory(...) → "OK, 記憶しました"
  - search → "検索機能はまだ未実装です"
  - chat → tim_llm_gateway.py → OpenAI response

## Verified Behavior
- "覚えて ..." is saved to memory/conversation_memory.json
- normal conversation still works
- saved preference memory is reflected in later chat responses
- newer preference memory overwrites older preference memory of the same broad type

## Current Limitation
- tim_brain_llm.py is currently rule-based
- search route is placeholder only
- memory is simple file-based persistence
- overwrite is keyword-based (not structured)
- no State Layer yet
- no Data Layer yet
- no Context Builder yet

## Active Files
- core/tim_core.py
- core/tim_brain_llm.py
- core/tim_llm_gateway.py
- layers/tim_memory_layer.py
- memory/conversation_memory.json

## Git State
- tim_tools is the correct Git repository
- nested Git issue resolved
- latest memory changes pushed

