import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}
        self.config = self.defaults.copy()

    def load(self, path: str) -> None:
        if os.path.exists(path):
            with open(path, 'r') as f:
                data = json.load(f)
                self.config.update(data)

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.config[key]

    def update(self, new_data: Dict[str, Any]) -> None:
        self.config.update(new_data)

def get_config(path: str, defaults: Dict[str, Any] = None) -> ConfigLoader:
    loader = ConfigLoader(defaults)
    loader.load(path)
    return loader