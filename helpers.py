import re


def validate_input_data(data: dict) -> bool:
    """
    Validates core input structure and data types.
    """
    required_keys = {'task_id', 'payload', 'priority'}
    if not all(key in data for key in required_keys):
        return False

    if not isinstance(data['task_id'], int) or data['task_id'] < 0:
        return False

    if not isinstance(data['payload'], str) or not data['payload'].strip():
        return False

    if not isinstance(data['priority'], int) or not (1 <= data['priority'] <= 5):
        return False

    return True


def sanitize_payload(payload: str) -> str:
    """
    Strips control characters and limits payload length.
    """
    cleaned = re.sub(r'[\x00-\x1f\x7f]', '', payload)
    return cleaned[:1024].strip()


def process_input_stream(data_list: list):
    """
    Main processing loop with integrated validation logic.
    """
    processed = []
    for entry in data_list:
        if not validate_input_data(entry):
            continue

        entry['payload'] = sanitize_payload(entry['payload'])
        processed.append(entry)

    return processed