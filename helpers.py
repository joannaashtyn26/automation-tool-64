import os
import json
import time
from functools import wraps
from typing import Any, Callable, Dict, List, Generator, Optional

def load_json(path: str) -> Dict[str, Any]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path: str, data: Dict[str, Any]) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def retry_decorator(max_attempts: int = 3, delay: float = 1.0) -> Callable[[Callable], Callable]:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            if last_exception:
                raise last_exception
            return None
        return wrapper
    return decorator

def ensure_dir_exists(path: str) -> str:
    os.makedirs(path, exist_ok=True)
    return path

def flatten_nested_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    items: List[tuple[str, Any]] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_nested_dict(v, new_key, sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def split_into_chunks(data: List[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def get_env(key: str, default: Optional[Any] = None) -> Optional[Any]:
    return os.getenv(key, default)

def safe_delete_file(path: str) -> bool:
    try:
        if os.path.exists(path):
            os.remove(path)
            return True
        return False
    except OSError:
        return False