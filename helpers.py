import os
import time
from typing import Any, Callable, Dict, List, Union


def deep_get(data: Dict[str, Any], keys: Union[str, List[str]], default: Any = None) -> Any:
    if isinstance(keys, str):
        keys = keys.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
        else:
            return default
        if current is None:
            return default
    return current


def safe_write(filepath: str, content: str) -> None:
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def retry(retries: int = 3, delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < retries - 1:
                        time.sleep(delay)
            if last_exception:
                raise last_exception
            raise RuntimeError("Execution failed")
        return wrapper
    return decorator
