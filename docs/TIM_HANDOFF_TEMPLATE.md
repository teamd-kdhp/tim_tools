🔴 TIM 新スレッド引き継ぎ手順（26年4月5日・完全版）
————————————————

🔴 ① 旧スレッドでやること（あなた → 旧スレッドへ指示）

まず、Mac mini のターミナルで以下を実行する

cd /Users/agent-a/openclaw/tim_tools
pwd
cat docs/TIM_HANDOFF_TEMPLATE.md

確認ポイント
・pwd の結果が /Users/agent-a/openclaw/tim_tools になっていること
・その上で docs/TIM_HANDOFF_TEMPLATE.md の内容が表示されること

👉 出てきた内容をすべてコピー
👉 あなたが旧スレッドにそのまま貼る（＝指示する）

注意
・cd /Users/agent-a/openclaw/tim_tools をせずに cat docs/TIM_HANDOFF_TEMPLATE.md を実行しないこと
・~ のまま実行すると、No such file or directory になる

————————————————

🔴 ② 旧スレッドに対してあなたが出す指示内容

👉 あなたが旧スレッド（ChatGPT）に対して以下を実行させる

指示内容（そのまま使う）

以下を実行してください。
・docs/TIM_STATUS.md を最新状態に更新
・docs/TIM_TASK_BOARD.md を最新状態に更新
・docs/TIM_CURRENT_EXECUTION.md を最新状態に更新

ルール：
・推測は禁止
・実際の現状のみを反映
・スコープを広げない
・不要な改善を入れない

————————————————

🔴 ③ Mac miniでやること（あなた）

👉 あなた自身が実行する

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

確認ポイント
・pwd の結果が /Users/agent-a/openclaw/tim_tools になっていること

👉 出てきた内容をすべてコピー（順番維持）

————————————————

🔴 ④ 新スレッドでやること（あなた → 新スレッドへ入力）

👉 あなたが新スレッドに貼る

貼る順番（絶対）
1. ③でコピーした内容（STATUS などすべて）
2. FIRST RESPONSE FORMAT（テンプレ）

FIRST RESPONSE FORMAT（あなたが貼る）

## 🔴 FIRST RESPONSE FORMAT (MANDATORY)

You MUST output ONLY:

1. Current state
2. Current development phase
3. Current step
4. Active task
5. Current structure (TIM / Layers)
6. ONE relevant file and WHY

DO NOT:
- Start implementation
- Expand scope
- Add new agents
- Change architecture

————————————————

🔴 ⑤ 新スレッドの最初の返信後（あなた → 新スレッドへ指示）

👉 新スレッドの ChatGPT に対して、あなたがこれを送る

Proceed.

Follow CURRENT_EXECUTION strictly.

Start from Step 2.

Do NOT expand scope.

Do NOT redesign architecture.

日本語で進める。

————————————————

🔴 運用ルール（あなたが常に守る / 指示する）

① Core優先ルール
👉 あなたが必ず確認させる
・tim_core.py を起点に構造を見る
・Layer構造（Memory / State / Data）を優先する
・旧来の Brain / Agents 発想に戻させない

② スコープ固定
👉 あなたが制御する
・CURRENT_EXECUTION 以外はやらせない
・勝手な改善は禁止
・今の Step 以外の話を始めたら止める

③ 推測禁止
👉 あなたが明示的に制御する
・STATUS にないことは禁止
・必ず現状ベース
・実際に書かれている内容のみで判断させる

④ 構造変更禁止
👉 あなたが止める
・Agent追加禁止
・Layer構造変更禁止
・LLM中心設計を崩させない

⑤ Development Order 固定
👉 あなたが必ず守らせる
・Step 1: Architecture Fix
・Step 2: File Structure
・Step 3: LLM Gateway
・Step 4: Minimal Conversation
・Step 5: Memory Layer
・Step 6: State Layer
・Step 7: Data Layer
・Step 8: Context Builder
・Step 9: Thinking Template Optimization

・順番を飛ばさせない
・Step 2 中に Step 3 以降へ進ませない

————————————————

🔴 よくあるミス（あなたが防ぐ）

❌ cd /Users/agent-a/openclaw/tim_tools をせずに cat docs/TIM_HANDOFF_TEMPLATE.md を実行する
❌ pwd を確認せずに進める
❌ FIRST RESPONSE FORMAT を先に貼る
❌ STATUS を貼らない
❌ CURRENT_EXECUTION を曖昧にする
❌ Step 2 なのに Step 1 に戻す
❌ Current structure を Brain / Agents のままにする
❌ ChatGPT が Layer構造を見ずに旧Brain発想で進める
❌ 実装禁止フェーズなのにコードを書き始める
❌ LLM未接続なのに prompt 最適化を始める

————————————————

🔴 一言まとめ

👉 必ず repo root に移動してから、テンプレや各 md を読むこと
👉 pwd で /Users/agent-a/openclaw/tim_tools を確認してから進めること
👉 新スレッドでは CURRENT_EXECUTION を最優先にすること
👉 今は Step 2（File Structure）であり、実装はまだしないこと
👉 構造は TIM / Layers であり、旧 Brain / Agents に戻さないこと

