import json
from typing import Any, Dict, List

class DataProcessor:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.processed_items: List[Dict[str, Any]] = []

    def load_data(self, filepath: str) -> List[Dict[str, Any]]:
        with open(filepath, 'r') as file:
            return json.load(file)

    def process_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        processed = item.copy()
        if 'value' in processed:
            processed['value'] = processed['value'] * self.config.get('multiplier', 1)
        processed['status'] = 'processed'
        return processed

    def batch_process(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        results = []
        for item in items:
            result = self.process_item(item)
            results.append(result)
            self.processed_items.append(result)
        return results

    def save_output(self, filepath: str, data: List[Dict[str, Any]]):
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=2)

    def run(self, input_file: str, output_file: str) -> List[Dict[str, Any]]:
        data = self.load_data(input_file)
        processed = self.batch_process(data)
        self.save_output(output_file, processed)
        return processed