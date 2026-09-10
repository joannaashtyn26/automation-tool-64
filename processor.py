import sys

def validate_input(data):
    if not isinstance(data, dict):
        return False
    if 'id' not in data or not isinstance(data['id'], int):
        return False
    return True

def run_process(data_stream):
    for entry in data_stream:
        if not validate_input(entry):
            print(f"invalid input encountered: {entry}", file=sys.stderr)
            continue
        try:
            execute_task(entry)
        except Exception as e:
            print(f"processing error: {e}", file=sys.stderr)

def execute_task(data):
    print(f"processing item {data['id']}")

if __name__ == '__main__':
    mock_data = [{'id': 1}, {'id': 'invalid'}, {'id': 2}]
    run_process(mock_data)