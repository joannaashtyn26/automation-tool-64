import json
from typing import Dict, List, Optional

class CoreAutomation:
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.errors: List[Dict] = []

    def process_data(self, data: List[Dict]) -> Dict:
        if not isinstance(data, list):
            return {"status": "error", "message": "data must be a list"}
        if not data:
            return {"status": "error", "message": "no data provided"}
        results = []
        for item in data:
            try:
                if not isinstance(item, dict):
                    raise ValueError("item must be a dictionary")
                if "value" not in item:
                    raise KeyError("missing value key")
                value = item["value"]
                if not isinstance(value, (int, float)):
                    raise TypeError("value must be numeric")
                if value == 0:
                    raise ZeroDivisionError("division by zero")
                result = 100 / value
                results.append({"input": item, "result": result})
            except (ValueError, KeyError, TypeError, ZeroDivisionError) as e:
                error_info = {"item": item, "error": str(e)}
                self.errors.append(error_info)
                results.append({"input": item, "result": None, "error": str(e)})
            except Exception as e:
                error_info = {"item": item, "error": f"unexpected: {str(e)}"}
                self.errors.append(error_info)
                results.append({"input": item, "result": None, "error": str(e)})
        return {
            "status": "completed",
            "results": results,
            "error_count": len(self.errors)
        }

    def save_results(self, results: Dict, filepath: str) -> bool:
        try:
            with open(filepath, "w") as f:
                json.dump(results, f, indent=2)
            return True
        except (IOError, OSError) as e:
            self.errors.append({"error": f"save failed: {str(e)}"})
            return False

    def get_errors(self) -> List[Dict]:
        return self.errors

if __name__ == "__main__":
    core = CoreAutomation({"automation": "enabled"})
    test_data = [
        {"value": 10},
        {"value": 0},
        {"value": "invalid"},
        {},
        {"value": 5},
        {"value": 2.5}
    ]
    output = core.process_data(test_data)
    print(json.dumps(output, indent=2))
    saved = core.save_results(output, "output.json")
    print(f"Save successful: {saved}")
    print("Captured errors:", core.get_errors())
