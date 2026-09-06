import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

def load_json(path: str) -> Dict[str, Any]:
    file_path = Path(path)
    if not file_path.exists():
        return {}
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path: str, data: Dict[str, Any]) -> None:
    with open(Path(path), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def ensure_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

def get_env_var(key: str, default: Optional[str] = None) -> str:
    return os.getenv(key, default or "")

def flatten_list(nested_list: list) -> list:
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def chunk_list(data: list, size: int) -> list:
    return [data[i : i + size] for i in range(0, len(data), size)]