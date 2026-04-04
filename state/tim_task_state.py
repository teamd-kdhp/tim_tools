# TIM Task State


class TIMTaskState:

    def create_task_record(self, user_input, intent, tasks):
        return {
            "user_input": user_input,
            "intent": intent,
            "tasks": tasks,
            "status": "created",
        }

