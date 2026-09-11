from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
from typing import Callable, Any, Dict, List

class TaskEngine:
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers

    @lru_cache(maxsize=1024)
    def _resolve_task(self, name: str) -> Callable[..., Any]:
        tasks = {
            "uppercase": lambda x: str(x).upper(),
            "strip": lambda x: str(x).strip(),
            "reverse": lambda x: str(x)[::-1]
        }
        return tasks.get(name, lambda x: x)

    def execute_batch(self, tasks: List[Dict[str, Any]]) -> List[Any]:
        results = [None] * len(tasks)
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_index = {
                executor.submit(self._run_task, task): i
                for i, task in enumerate(tasks)
            }
            for future in as_completed(future_to_index):
                index = future_to_index[future]
                try:
                    results[index] = future.result()
                except Exception as exc:
                    results[index] = exc
        return results

    def _run_task(self, task: Dict[str, Any]) -> Any:
        task_type = task.get("type", "noop")
        data = task.get("data")
        func = self._resolve_task(task_type)
        return func(data)
