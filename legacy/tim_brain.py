# TIM Brain (Strategy Enabled)

import json
from janome.tokenizer import Tokenizer
from state.tim_task_state import TIMTaskState
from .agents.intelligence_agent import IntelligenceAgent
from .agents.execution_agent import ExecutionAgent
from .agents.strategy_agent import StrategyAgent


class TIMBrain:

    def __init__(self):
        self.state = TIMTaskState()
        self.intelligence_agent = IntelligenceAgent()
        self.execution_agent = ExecutionAgent()
        self.strategy_agent = StrategyAgent()
        self.learning_file = "state/tim_learning.json"
        self.tokenizer = Tokenizer()

    def load_learning(self):
        with open(self.learning_file, "r") as f:
            return json.load(f)

    def save_learning(self, data):
        with open(self.learning_file, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def tokenize(self, text):
        return [token.surface for token in self.tokenizer.tokenize(text)]

    def detect_intent(self, user_input):
        learning = self.load_learning()
        tokens = self.tokenize(user_input)

        for intent, words in learning["keywords"].items():
            for word in words:
                if word in tokens:
                    return intent

        return "general"

    def extract_keywords(self, text):
        return set(self.tokenize(text))

    def similarity_score(self, input1, input2):
        k1 = self.extract_keywords(input1)
        k2 = self.extract_keywords(input2)

        if not k1 and not k2:
            return 0

        return len(k1 & k2) / len(k1 | k2)

    def decide(self, intent, previous_intent, score):
        if previous_intent is None:
            return "EXECUTE"

        if intent == previous_intent and score > 0.6:
            return "REUSE"

        if score < 0.2:
            return "EXECUTE"

        return "HOLD"

    def auto_learn(self, user_input, intent):
        learning = self.load_learning()
        tokens = self.tokenize(user_input)

        if intent not in learning["keywords"]:
            learning["keywords"][intent] = []

        for token in tokens:
            if len(token) > 1 and token not in learning["keywords"][intent]:
                learning["keywords"][intent].append(token)

        self.save_learning(learning)

    def format_output(self, purpose, situation, judgment, action, risk):
        return {
            "Purpose": purpose,
            "Situation": situation,
            "Judgment": judgment,
            "Action": action,
            "Risk": risk
        }

    def process(self, user_input):
        previous_state = self.state.load()

        intent = self.detect_intent(user_input)

        score = 0
        previous_intent = None

        if previous_state:
            score = self.similarity_score(user_input, previous_state["user_input"])
            previous_intent = previous_state["intent"]

        if any(k in user_input for k in ["こどハピ", "既存", "拡張", "横展開", "スポンサー"]):
            decision = "EXECUTE"

        decision = self.decide(intent, previous_intent, score)

        if decision == "REUSE":
            return self.format_output(
                purpose="過去に近い依頼に対して、既存の判断を再利用する",
                situation="同一テーマで再依頼されており、過去の判断・実行結果をそのまま活用できる状態です",
                judgment="新規対応は不要です。過去の判断をそのまま適用するのが最適です。優先度は低く、追加リスクもありません。",
                action="過去の判断をそのまま適用し、追加対応は行わずに進めてください",
                risk="リスクは低いが、前提条件が変わっていないかの確認は必要です"
            )

        if decision == "HOLD":
            return self.format_output(
                purpose="この新規事業案が実行すべきものかを判断する",
                situation="判断に必要な情報が不足しており、このまま実行すると精度の低い意思決定になる可能性がある状態です",
                judgment="現時点では判断材料が不足しており、実行すべき段階ではありません。まず事業の前提条件を整理する必要があります。優先度は低です。",
                action="不足している情報を確認し、判断条件を整理したうえで再評価してください",
                risk="不明確な状態で進めると、時間とリソースを無駄に消費するリスクがあります"
            )

        tasks = self.strategy_agent.run(intent, user_input)

        task_record = self.state.create_task_record(user_input, intent, tasks)

        for task in tasks:
            if task["agent"] == "intelligence":
                result = self.intelligence_agent.run(task)
            else:
                result = self.execution_agent.run(task)

            task_record = self.state.update_progress(task_record, result)

        self.state.save(task_record)

        self.auto_learn(user_input, intent)

        return self.format_output(
            purpose="この新規事業案が実行すべきものかを判断する",
            situation=f"今回の依頼は新規テーマであり、過去の判断資産を流用できないため、新たに対応が必要な状態です",
            judgment="現時点では小さく検証を開始すべきです。いきなり大きく投資する段階ではなく、仮説検証を通じて成立性を見極めるのが適切です。優先度は中〜高です。",
            action="まずスポンサー候補を3社仮定し、それぞれの提供価値（教育×PR）を整理してください。その上で1社に対して仮提案を作り、小さく検証を開始してください",
            risk="顧客課題や市場の検証が不十分なまま進めると、作っただけで売れないリスクがあります"
        )


if __name__ == "__main__":
    brain = TIMBrain()

    print(brain.process("市場を分析して"))
    print(brain.process("新しいサービスを作って"))
