import os
import json
from typing import List, Dict, Any, Callable

def read_text_file(path: str) -> str:
    """Read text content from file.
    Args:
        path: file path to read.
    Returns:
        file content string.
    """
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def write_text_file(path: str, content: str) -> None:
    """Write content to file.
    Args:
        path: file path to write.
        content: text to write.
    """
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

def list_files_with_extension(directory: str, extension: str) -> List[str]:
    """List files matching extension.
    Args:
        directory: search directory.
        extension: file extension.
    Returns:
        list of file paths.
    """
    files: List[str] = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extension):
                files.append(os.path.join(root, filename))
    return files

def load_config(config_path: str) -> Dict[str, Any]:
    """Load config from JSON.
    Args:
        config_path: path to JSON.
    Returns:
        config dict.
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge dicts with override.
    Args:
        dict1: first dict.
        dict2: second dict.
    Returns:
        merged dict.
    """
    merged: Dict[str, Any] = dict1.copy()
    merged.update(dict2)
    return merged

def apply_function_to_list(items: List[Any], func: Callable[[Any], Any]) -> List[Any]:
    """Apply func to list items.
    Args:
        items: input items.
        func: function to apply.
    Returns:
        list of results.
    """
    return [func(item) for item in items]