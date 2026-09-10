import os
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

def load_config(path: str) -> Dict[str, Any]:
    if not path:
        logger.error("configuration path missing")
        raise ValueError("path cannot be empty")

    if not os.path.exists(path):
        logger.error(f"config file not found at {path}")
        return {}

    try:
        with open(path, 'r') as f:
            data = f.read()
            if not data.strip():
                logger.warning(f"config file {path} is empty")
                return {}
            return dict(line.split('=') for line in data.splitlines() if '=' in line)
    except (IOError, PermissionError) as e:
        logger.critical(f"failed to access config file: {e}")
        return {}
    except ValueError as e:
        logger.error(f"malformed configuration format: {e}")
        return {}

class ConfigError(Exception):
    pass

def validate_config(config: Dict[str, Any], required_keys: list) -> None:
    missing = [key for key in required_keys if key not in config]
    if missing:
        raise ConfigError(f"missing required configuration keys: {', '.join(missing)}")