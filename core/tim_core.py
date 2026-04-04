"""
tim_core.py

TIM v2 central orchestrator.

Responsibility:
- Control overall request flow
- Call context builder
- Call LLM gateway
- Build final response pipeline

Rules:
- No hardcoded business decision logic
- No direct connector logic
- No direct web/file/SaaS implementation
"""
