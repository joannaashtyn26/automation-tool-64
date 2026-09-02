import json

def safe_divide(a, b):
    try:
        return float(a) / float(b)
    except (ZeroDivisionError, ValueError, TypeError):
        return 0.0

def safe_list_access(lst, index):
    try:
        return lst[int(index)]
    except (IndexError, TypeError, ValueError):
        return None

def safe_json_load(data):
    try:
        if isinstance(data, (bytes, bytearray)):
            data = data.decode('utf-8')
        return json.loads(data)
    except (json.JSONDecodeError, TypeError, UnicodeDecodeError):
        return {}

def safe_file_read(path):
    try:
        if not isinstance(path, str):
            return ''
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except (FileNotFoundError, PermissionError, OSError):
        return ''

def safe_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0

def process_list(data):
    if not data:
        return []
    try:
        if isinstance(data, str):
            items = [safe_int(x.strip()) for x in data.split(',') if x.strip()]
            return items
        if isinstance(data, (list, tuple)):
            return [safe_int(x) for x in data]
        return [safe_int(data)]
    except Exception:
        return []

def run_automation_step(step_func, *args, **kwargs):
    try:
        return step_func(*args, **kwargs)
    except Exception:
        return None