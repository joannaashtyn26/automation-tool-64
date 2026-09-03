import json
from typing import Any, Dict, Optional


def clean_data(data: Any) -> Any:
    if isinstance(data, dict):
        return {str(k): clean_data(v) for k, v in data.items() if v is not None}
    if isinstance(data, list):
        return [clean_data(i) for i in data]
    return data


def load_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def save_json_file(file_path: str, data: Any) -> bool:
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(clean_data(data), f, indent=4)
        return True
    except (TypeError, IOError):
        return False


def extract_field(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default