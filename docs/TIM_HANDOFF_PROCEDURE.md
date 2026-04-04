# 🔴 TIM 新スレッド引き継ぎ手順（26年4月5日・修正版）

————————————————

## 🔴 ① 旧スレッドでやること（あなた → 旧スレッドへ指示）

### まず、Mac mini のターミナルで以下を実行する

cd /Users/agent-a/openclaw/tim_tools
pwd
cat docs/TIM_HANDOFF_TEMPLATE.md

### 確認ポイント
- pwd の結果が /Users/agent-a/openclaw/tim_tools になっていること
- その上で docs/TIM_HANDOFF_TEMPLATE.md の内容が表示されること

👉 出てきた内容をすべてコピー  
👉 あなたが旧スレッドにそのまま貼る（＝指示する）

### 注意
- cd をせずに cat を実行しないこと
- ~ のまま実行するとエラーになる

---

## 🔴 ② 旧スレッドに対してあなたが出す指示内容

以下を実行してください。

1. docs/TIM_STATUS.md を最新状態に更新  
2. docs/TIM_TASK_BOARD.md を最新状態に更新  
3. docs/TIM_CURRENT_EXECUTION.md を最新状態に更新  

ルール：
- 推測は禁止
- 実際の現状のみを反映
- スコープを広げない
- 不要な改善を入れない

---

## 🔴 ③ Mac miniでやること（あなた）

cd /Users/agent-a/openclaw/tim_tools
pwd

echo "===== TIM STATUS ====="
cat docs/TIM_STATUS.md

echo ""
echo "===== TIM TASK BOARD ====="
cat docs/TIM_TASK_BOARD.md

echo ""
echo "===== TIM CURRENT EXECUTION ====="
cat docs/TIM_CURRENT_EXECUTION.md

echo ""
echo "===== TIM START PROMPT ====="
cat docs/TIM_START_PROMPT.md

echo ""
echo "===== TIM HANDOFF RULES ====="
cat docs/TIM_HANDOFF_RULES.md

echo ""
echo "===== TIM BRAIN ====="
cat core/tim_brain.py

👉 出てきた内容をすべてコピー（順番維持）

---

## 🔴 ④ 新スレッドでやること

貼る順番（絶対）

1. 上のコピー内容  
2. FIRST RESPONSE FORMAT  

---

## 🔴 FIRST RESPONSE FORMAT

## 🔴 FIRST RESPONSE FORMAT (MANDATORY)

You MUST output ONLY:

1. Current state
2. Active task
3. Current structure (Brain / Agents)
4. ONE relevant file and WHY

DO NOT:
- Start implementation
- Expand scope
- Add new agents

---

## 🔴 ⑤ 新スレッドの最初の返信後

Proceed.

Follow CURRENT_EXECUTION strictly.

Start from Step 1.

Do NOT expand scope.

Do NOT redesign Brain or Agents.

日本語で進める。

---

# 🔴 運用ルール

① Brain優先  
- core/tim_brain.py を最初に確認  
- Agentに逃がさない  

② スコープ固定  
- CURRENT_EXECUTION以外禁止  

③ 推測禁止  
- STATUSベースのみ  

④ 構造変更禁止  
- Agent追加禁止  

---

# 🔴 よくあるミス

❌ cdせずにcatする  
❌ pwd確認しない  
❌ FIRST RESPONSE先貼り  
❌ STATUS不足  

---

# 🔴 一言

必ず /Users/agent-a/openclaw/tim_tools に移動してから作業する
