# TIM Handoff Rules

## 🔴 Core Principles

- NEVER assume context
- ALWAYS rely on provided documents
- DO NOT expand scope without instruction
- ONLY focus on CURRENT_EXECUTION
- TIM is LLM-centered
- TIM is the only dialogue interface

---

## 🔴 Architecture Lock

TIM structure is fixed as:

User
  ↓
TIM
  ├ Conversation Core (LLM)
  ├ Memory Layer
  ├ State Layer
  ├ Data Layer
  │   ├ Web Connector
  │   ├ Drive Connector
  │   ├ Internal DB Connector
  │   └ SaaS Connector
  └ Executor Connector (future)

Do NOT redesign this casually.

---

## 🔴 Brain / LLM Rule

- Final reasoning must come from LLM
- TIM must NOT become a fixed logic engine
- TIM must focus on context building and orchestration
- Do NOT weaken LLM’s role

---

## 🔴 Execution Rule

At any time:
- You MUST ONLY work on ONE current step
- You MUST follow development order
- You MUST NOT jump ahead

---

## 🔴 Development Order

Step 1: Architecture Fix
Step 2: File Structure
Step 3: LLM Gateway
Step 4: Minimal Conversation
Step 5: Memory Layer
Step 6: State Layer
Step 7: Data Layer
Step 8: Context Builder
Step 9: Thinking Template Optimization

---

## 🔴 Current Execution Rule

CURRENT_EXECUTION is the single source of truth.

If there is any ambiguity:
- CURRENT_EXECUTION wins
- Current step wins
- Scope must remain narrow

---

## 🔴 Forbidden

- Refactoring without instruction
- Adding features not requested
- Modifying architecture without confirmation
- Designing prompt optimization before LLM integration
- Implementing rule-based final decision logic
- Skipping phases

---

## 🔴 STEP 1 COMPLETION CRITERIA (Architecture Fix)

Step 1 is considered COMPLETE only if ALL conditions below are met:

1. TIM is clearly defined as LLM-centered in all files
2. TIM is the ONLY dialogue interface
3. Memory / State / Data Layer structure is fixed
4. Development order is defined and consistent everywhere
5. CURRENT_EXECUTION is the single source of truth
6. All files strictly follow CURRENT_EXECUTION
7. "No implementation" is clearly enforced
8. LLM is NOT yet connected
9. Prompt optimization has NOT started
10. No connectors or agents are implemented

--------------------------------------------------

Completion Definition:

"Any new thread will ONLY discuss Step 1 topics."

If ANY implementation discussion appears:
→ Step 1 is NOT complete

--------------------------------------------------

Do NOT move to Step 2 unless ALL conditions are satisfied.


---

## 🔴 STEP 1 COMPLETION CRITERIA (Architecture Fix)

Step 1 is considered COMPLETE only if ALL conditions below are met:

1. TIM is clearly defined as LLM-centered in all files
2. TIM is the ONLY dialogue interface
3. Memory / State / Data Layer structure is fixed
4. Development order is defined and consistent everywhere
5. CURRENT_EXECUTION is the single source of truth
6. All files strictly follow CURRENT_EXECUTION
7. "No implementation" is clearly enforced
8. LLM is NOT yet connected
9. Prompt optimization has NOT started
10. No connectors or agents are implemented

--------------------------------------------------

Completion Definition:

"Any new thread will ONLY discuss Step 1 topics."

If ANY implementation discussion appears:
→ Step 1 is NOT complete

--------------------------------------------------

Do NOT move to Step 2 unless ALL conditions are satisfied.


## 🔴 Cursor運用ルール（重要）

本プロジェクトでは、Cursorによる自動実装を使用するが、以下を厳守すること。

### ① 先に実装しない
・いきなりコードを書かない
・必ず「変更予定ファイル一覧」と「変更内容」を先に提示する

### ② 承認制
・ユーザーの承認があるまで実装禁止

### ③ スコープ固定
・CURRENT_EXECUTION の範囲のみ実行
・Stepを飛ばさない

### ④ 変更範囲制限
・指定ファイル以外は触らない
・既存構造を変更しない

### ⑤ 設計優先
・TIMはLLM中心構造
・Memory / State / Data Layerを前提とする
・旧Brain/Agent構造に戻さない

### ⑥ 禁止事項
・勝手な最適化
・リファクタ
・新規Agent追加
・アーキテクチャ変更

### ⑦ フェーズ制御
Step 2 の間は以下のみ許可：
・ファイル作成
・docstring作成
・構造定義

以下は禁止：
・LLM接続
・外部API
・ビジネスロジック実装

