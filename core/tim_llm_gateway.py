"""
tim_llm_gateway.py

Single gateway to LLM provider.

Responsibility:
- Send prompt and structured context to LLM
- Receive and normalize LLM response

Rules:
- Final reasoning belongs to LLM through this module
- No memory ownership
- No state ownership
- No connector logic
"""
