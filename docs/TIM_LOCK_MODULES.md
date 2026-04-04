# TIM LOCK MODULES

## ■ Purpose

Prevent unintended modifications to core system components.

---

## ■ Locked Modules

### Core

- core/tim_brain.py

Reason:
Central decision logic must remain stable.

---

### Docs

- docs/TIM_STATUS.md
- docs/TIM_START_PROMPT.md
- docs/TIM_GUARDRAILS.md

Reason:
These define system identity and rules.

---

## ■ Rules

- Do NOT modify locked modules without explicit instruction
- Do NOT refactor core logic casually
- Do NOT override system structure

---

## ■ Exception

Changes allowed ONLY when:

- explicitly requested
- clearly justified
- impact is fully understood

---

## ■ Goal

Maintain system consistency and prevent AI drift.

