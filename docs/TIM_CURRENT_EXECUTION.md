# TIM CURRENT EXECUTION

## Phase
REBUILD / ALIGNMENT

## Step
Brain-centered route restored

## Active Task
Document the restored current route and fix the source of truth before further implementation

## 状態
- core/tim_main.py → legacy.tim_brain.TIMBrain.process() で動作確認済み
- legacy Brain 単体実行 OK
- tim_main 経由呼び出し OK
- 戻り値は dict
- 自然会話出力は未対応
- Memory / State / Data / Context Builder の統合は未完了

## Scope
- 現状固定のみ
- ドキュメント整合
- 実装拡張しない
- 要件に沿った正ルートを明確化する

## 禁止
- Cursor由来の壊れた経路を正としない
- core/tim_core.py を起点に戻さない
- 新規機能を追加しない
- Data Layer / Connector 接続を先に進めない
- アーキテクチャ変更をしない

## Source of Truth
CURRENT_EXECUTION が絶対

## Current Valid Route
core/tim_main.py
→ legacy.tim_brain.TIMBrain.process()
→ legacy agents
→ state/tim_task_state.py
