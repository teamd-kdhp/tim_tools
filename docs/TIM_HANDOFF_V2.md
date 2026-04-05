# 🔴 TIM 新スレッド引き継ぎ手順（V2 / LLM-first版）

--------------------------------------------------

## 🔴 基本思想（最重要）

TIMは以下4つで成立する：

1. REQUIREMENTS（思想）
2. START_PROMPT（AI制御）
3. STATUS（現在地）
4. CURRENT_EXECUTION（タスク）

👉 この4つを正しく渡せば、TIMは完全再現できる

--------------------------------------------------

## 🔴 ① 旧スレッドでやること

Mac miniで実行：

cd /Users/agent-a/openclaw/tim_tools
pwd

cat docs/TIM_STATUS.md
cat docs/TIM_CURRENT_EXECUTION.md

確認：
・pwd が /Users/agent-a/openclaw/tim_tools であること

👉 出力をすべてコピー

--------------------------------------------------

## 🔴 ② 新スレッドに貼る内容（順番厳守）

① TIM_STATUS.md

② TIM_CURRENT_EXECUTION.md

③ TIM_START_PROMPT.md

④ TIM_REQUIREMENTS_V3.md

--------------------------------------------------

## 🔴 ③ FIRST RESPONSE FORMAT

## 🔴 FIRST RESPONSE FORMAT (MANDATORY)

You MUST output ONLY:

1. Current state
2. Current development phase
3. Current step
4. Active task
5. Current architecture (TIM / Layers)
6. ONE relevant file and WHY

DO NOT:
- Start implementation
- Expand scope
- Redesign architecture
- Introduce new concepts

--------------------------------------------------

## 🔴 ④ 新スレッドへの指示

Proceed.

Follow CURRENT_EXECUTION strictly.

Do NOT expand scope.
Do NOT redesign.

日本語で進める。

--------------------------------------------------

## 🔴 運用ルール

① LLM-first厳守
・TIMはLLM中心
・rule-based化は禁止

② スコープ固定
・CURRENT_EXECUTION以外やらない
・勝手な改善禁止

③ 推測禁止
・STATUSベースのみ
・書かれていないことは扱わない

④ 構造変更禁止
・Layer構造を守る
・新しい抽象化を勝手に作らない

--------------------------------------------------

## 🔴 削除された旧要素（使用禁止）

以下は使用しない：

・TIM_BRAIN
・Agent構造前提
・HANDOFF_TEMPLATE
・HANDOFF_RULES
・過去のBrain中心設計

理由：
👉 LLM-first設計と矛盾するため

--------------------------------------------------

## 🔴 一言まとめ

👉 REQUIREMENTS + START_PROMPT + STATUS + CURRENT_EXECUTION だけでTIMは再現できる
👉 順番を間違えると壊れる
👉 今は設計フェーズ、実装はまだしない

