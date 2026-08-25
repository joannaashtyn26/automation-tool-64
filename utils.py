import os
import json
from typing import Any, Dict, List, Optional

def safe_file_read(path: str) -> Optional[str]:
    if not path or not isinstance(path, str):
        return None
    try:
        if not os.path.isfile(path):
            return None
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except (OSError, IOError, PermissionError, UnicodeDecodeError):
        return None

def safe_file_write(path: str, content: str) -> bool:
    if not path or not isinstance(path, str) or not isinstance(content, str):
        return False
    try:
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except (OSError, IOError, PermissionError):
        return False

def safe_json_parse(text: str) -> Optional[Dict[str, Any]]:
    if not text or not isinstance(text, str):
        return None
    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict):
            return parsed
        return None
    except (json.JSONDecodeError, TypeError, ValueError):
        return None

def process_data_list(items: List[Any]) -> List[str]:
    if not isinstance(items, list):
        return []
    result: List[str] = []
    for item in items:
        if item is None:
            continue
        try:
            str_item = str(item).strip()
            if str_item:
                result.append(str_item)
        except Exception:
            continue
    return result

def handle_dict_edge_cases(data: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(data, dict):
        return {}
    output: Dict[str, Any] = {}
    for key, value in data.items():
        if key is None or not isinstance(key, str):
            continue
        try:
            if value is None:
                output[key] = None
            elif isinstance(value, (int, float)):
                output[key] = max(0, value)
            elif isinstance(value, str):
                output[key] = value.strip() or "empty"
            else:
                output[key] = value
        except Exception:
            output[key] = "invalid"
    return output