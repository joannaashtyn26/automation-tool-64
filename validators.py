import re
import json

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str) or not email:
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def is_valid_url(url: str) -> bool:
    if not isinstance(url, str) or not url:
        return False
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[^\s]*)?$"
    return bool(re.match(pattern, url))

def is_valid_ipv4(ip: str) -> bool:
    if not isinstance(ip, str) or not ip:
        return False
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(pattern, ip))

def is_valid_port(port) -> bool:
    try:
        p = int(port)
        return 1 <= p <= 65535
    except (ValueError, TypeError):
        return False

def is_positive_number(value) -> bool:
    try:
        return float(value) > 0
    except (ValueError, TypeError):
        return False

def is_non_empty(value) -> bool:
    if isinstance(value, str):
        return len(value.strip()) > 0
    elif isinstance(value, (list, dict, set, tuple)):
        return len(value) > 0
    return False

def is_valid_json(data: str) -> bool:
    if not isinstance(data, str):
        return False
    try:
        json.loads(data)
        return True
    except (json.JSONDecodeError, TypeError, ValueError):
        return False

def validate_range(value, min_val, max_val) -> bool:
    try:
        v = float(value)
        return min_val <= v <= max_val
    except (ValueError, TypeError):
        return False