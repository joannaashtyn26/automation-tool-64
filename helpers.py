import functools
import time
from typing import Callable, Any, Dict

def memoize(func: Callable) -> Callable:
    cache: Dict[tuple, Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def throttle(interval: float) -> Callable:
    def decorator(func: Callable) -> Callable:
        last_called: Dict[str, float] = {'time': 0.0}

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_time = time.monotonic()
            elapsed = current_time - last_called['time']
            if elapsed < interval:
                time.sleep(interval - elapsed)
            result = func(*args, **kwargs)
            last_called['time'] = time.monotonic()
            return result
        return wrapper
    return decorator

class BatchProcessor:
    def __init__(self, size: int = 100):
        self.size = size
        self.buffer = []

    def add(self, item: Any) -> list:
        self.buffer.append(item)
        if len(self.buffer) >= self.size:
            return self.flush()
        return []

    def flush(self) -> list:
        data = self.buffer
        self.buffer = []
        return data