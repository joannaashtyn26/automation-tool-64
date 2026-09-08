import os
import json
import shutil
from pathlib import Path
from typing import Any, Dict

def ensure_directory(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

def read_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(data: Dict[str, Any], file_path: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def safe_remove(path: str) -> None:
    path_obj = Path(path)
    if path_obj.is_file() or path_obj.is_symlink():
        path_obj.unlink()
    elif path_obj.is_dir():
        shutil.rmtree(path_obj)

def get_env_variable(key: str, default: str = None) -> str:
    return os.environ.get(key, default)

def format_byte_size(size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"