import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None, config_path: str = "config.json"):
        self.defaults = defaults or {}
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        config = self.defaults.copy()
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as file:
                    file_config = json.load(file)
                    if isinstance(file_config, dict):
                        config.update(file_config)
            except (json.JSONDecodeError, OSError):
                pass
        return config

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.config[key] = value

    def save(self) -> None:
        with open(self.config_path, "w", encoding="utf-8") as file:
            json.dump(self.config, file, indent=2)

    def reload(self) -> None:
        self.config = self._load_config()

    def as_dict(self) -> Dict[str, Any]:
        return self.config.copy()