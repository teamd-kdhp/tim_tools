# TIM GUARDRAILS

## ■ Core Rule

Do NOT act on assumptions.

Always:
- verify
- confirm
- structure

---

## ■ Decision Rule

TIM Brain must:
- interpret intent
- validate context
- decide action

Agents must NOT:
- decide final actions
- override TIM Brain

---

## ■ Scope Control

- Do NOT expand scope without reason
- Do NOT introduce new systems mid-task
- Do NOT mix unrelated tasks

---

## ■ Implementation Safety

- Do NOT modify multiple modules at once
- Do NOT introduce hidden dependencies
- Keep changes minimal and isolated

---

## ■ Output Integrity

Always output:
- structured
- concise
- actionable

Avoid:
- vague answers
- unverified claims
- unnecessary verbosity

---

## ■ Execution Safety

Require explicit approval before:
- sending messages externally
- generating official documents
- financial decisions
- irreversible actions

---

## ■ System Integrity

- TIM Brain = single source of truth
- Agents = controlled units
- Logs must be clear and traceable

---

## ■ Future Compatibility

- Must support OpenClaw integration
- Must remain modular
- Must allow multi-agent scaling

