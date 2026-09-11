import json
import os
from typing import Any, Dict, Optional

def load_json(path: str) -> Optional[Dict[str, Any]]:
    if not os.path.exists(path):
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_json(data: Dict[str, Any], path: str) -> bool:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def ensure_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunk_list(data: list, size: int):
    for i in range(0, len(data), size):
        yield data[i:i + size]