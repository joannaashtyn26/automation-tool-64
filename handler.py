import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger("automation_tool.handler")

class TaskHandler:
    def __init__(self, raw_tasks: List[Dict[str, Any]]):
        self.raw_tasks = raw_tasks
        self.processed_count = 0
        self.failed_count = 0

    def validate_task(self, task: Dict[str, Any]) -> Tuple[bool, str]:
        if not isinstance(task, dict):
            return False, "task must be a dictionary"
        
        task_id = task.get("id")
        if task_id is None or not isinstance(task_id, (int, str)):
            return False, "missing or invalid task id"
        
        action = task.get("action")
        if not action or not isinstance(action, str):
            return False, f"task {task_id}: missing or invalid action"
        
        allowed_actions = {"status_check", "data_sync", "report_generation"}
        if action not in allowed_actions:
            return False, f"task {task_id}: unsupported action '{action}'"
        
        return True, ""

    def process_tasks(self) -> Dict[str, Any]:
        results = []
        for index, raw_task in enumerate(self.raw_tasks):
            is_valid, error_msg = self.validate_task(raw_task)
            if not is_valid:
                logger.warning(f"Validation failed at index {index}: {error_msg}")
                self.failed_count += 1
                continue

            task_id = raw_task["id"]
            action = raw_task["action"]
            
            results.append({"id": task_id, "status": "success", "action": action})
            self.processed_count += 1

        return {
            "processed": self.processed_count,
            "failed": self.failed_count,
            "results": results,
        }