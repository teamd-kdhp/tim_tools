# TIM Task State

import json
import os


class TIMTaskState:

    def __init__(self):
        self.file_path = "state/tim_state.json"

    def create_task_record(self, user_input, intent, tasks):
        return {
            "user_input": user_input,
            "intent": intent,
            "tasks": tasks,
            "status": "created",
            "progress": [],
        }

    def update_progress(self, task_record, execution_result):
        task_record["progress"].append(execution_result)
        task_record["status"] = "in_progress"
        return task_record

    def save(self, task_record):
        with open(self.file_path, "w") as f:
            json.dump(task_record, f, indent=2)

    def load(self):
        if not os.path.exists(self.file_path):
            return None
        with open(self.file_path, "r") as f:
            return json.load(f)

