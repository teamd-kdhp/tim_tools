# Strategy Agent

class StrategyAgent:

    def run(self, intent, user_input):
        # 超シンプル戦略
        if intent == "analysis":
            return [
                {"agent": "intelligence", "task_type": "deep_research"},
                {"agent": "execution", "task_type": "report"}
            ]

        if intent == "build":
            return [
                {"agent": "intelligence", "task_type": "requirement_analysis"},
                {"agent": "execution", "task_type": "build"}
            ]

        return [
            {"agent": "execution", "task_type": "quick_response"}
        ]

