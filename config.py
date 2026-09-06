import json
from pathlib import Path
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, filepath: str, defaults: Dict[str, Any] = None):
        self.filepath = Path(filepath)
        self.defaults = defaults or {}
        self.config = self._load()

    def _load(self) -> Dict[str, Any]:
        if not self.filepath.exists():
            return self.defaults
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
                return {**self.defaults, **data}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def save(self) -> None:
        with open(self.filepath, 'w') as f:
            json.dump(self.config, f, indent=4)

    def update(self, **kwargs) -> None:
        self.config.update(kwargs)
        self.save()