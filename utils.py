from typing import Any, Dict, List, Union


def flatten_dict(
    d: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flattens a nested dictionary."""
    items: List[tuple[str, Any]] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def get_by_path(
    d: Dict[str, Any], path: Union[str, List[str]], default: Any = None
) -> Any:
    """Retrieves a value from a nested dictionary using a dot-separated path."""
    if isinstance(path, str):
        path = path.split(".")

    current = d
    for key in path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def safe_cast(value: Any, to_type: type, default: Any = None) -> Any:
    """Safely casts a value to a given type, returning default on failure."""
    try:
        if to_type is bool and isinstance(value, str):
            return value.lower() in ("true", "1", "t", "y", "yes")
        return to_type(value)
    except (ValueError, TypeError):
        return default
