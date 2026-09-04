import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "host": "localhost",
    "port": 8080,
    "debug": False,
    "retries": 3
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json") -> None:
        self.config_path = config_path
        self.settings = DEFAULT_CONFIG.copy()
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    user_config = json.load(f)
                    self.settings.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.settings[key]

    def __repr__(self) -> str:
        return f"ConfigLoader({self.settings})"