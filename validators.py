import re
from typing import Any, Dict

class ValidationError(Exception):
    pass

def validate_payload(data: Dict[str, Any]) -> None:
    if not isinstance(data, dict):
        raise ValidationError("Payload must be a dictionary")
    
    required_fields = ['id', 'action', 'timestamp']
    for field in required_fields:
        if field not in data:
            raise ValidationError(f"Missing required field: {field}")

    if not isinstance(data['id'], int):
        raise ValidationError("Field 'id' must be an integer")

    if not isinstance(data['action'], str) or not re.match(r'^[a-z_]+$', data['action']):
        raise ValidationError("Field 'action' must be a lowercase slug")

def validate_config(config: Dict[str, Any]) -> bool:
    try:
        if 'retry_limit' in config:
            if not isinstance(config['retry_limit'], int) or config['retry_limit'] < 0:
                return False
        if 'timeout' in config:
            if not isinstance(config['timeout'], (int, float)) or config['timeout'] <= 0:
                return False
        return True
    except Exception:
        return False