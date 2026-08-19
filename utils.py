import json
from typing import Any, Dict, List

def load_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data: Dict[str, Any], file_path: str) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    return [item for sublist in nested_list for item in sublist]


def unique_elements(input_list: List[Any]) -> List[Any]:
    return list(set(input_list))


def merge_dictionaries(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    merged = dict1.copy()
    merged.update(dict2)
    return merged
