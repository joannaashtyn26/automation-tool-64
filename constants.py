"""Constants for the automation-tool-64 application.

This module provides all necessary constant values used throughout the tool.
All constants are typed using Final from typing for immutability indication.
"""

from __future__ import annotations

from typing import Any, Dict, Final, List

class AutomationConstants:
    """Holds all constant values for the automation tool.

    Provides a centralized place for configuration constants.
    """

    DEFAULT_TIMEOUT: Final[int] = 30
    MAX_RETRIES: Final[int] = 5
    RETRY_BACKOFF: Final[float] = 2.0
    LOG_LEVEL: Final[str] = "INFO"
    BASE_URL: Final[str] = "https://api.automation-tool-64.example"
    USER_AGENT: Final[str] = "AutomationTool64/0.1"
    MAX_PARALLEL_TASKS: Final[int] = 10
    BUFFER_SIZE: Final[int] = 8192
    ENABLE_DEBUG: Final[bool] = False
    SESSION_TIMEOUT: Final[int] = 300
    MAX_FILE_SIZE: Final[int] = 10485760
    ALLOWED_PROTOCOLS: Final[List[str]] = ["http", "https"]
    DEFAULT_ENCODING: Final[str] = "utf-8"
    ERROR_THRESHOLD: Final[int] = 3
    CACHE_SIZE: Final[int] = 1000
    QUEUE_MAX_SIZE: Final[int] = 500
    HEARTBEAT_INTERVAL: Final[int] = 60
    CONNECTION_POOL_SIZE: Final[int] = 20

def get_all_constants() -> Dict[str, Any]:
    """Retrieve all defined constants as a dictionary.

    Returns:
        A dictionary containing all constant names and their values.
    """
    constants: Dict[str, Any] = {}
    for attr in dir(AutomationConstants):
        if not attr.startswith("_") and attr.isupper():
            constants[attr] = getattr(AutomationConstants, attr)
    return constants

def get_constant(name: str) -> Any:
    """Get a specific constant by its name.

    Args:
        name: The uppercase name of the constant to retrieve.

    Returns:
        The value of the constant if found.

    Raises:
        KeyError: If the constant name does not exist.
    """
    if hasattr(AutomationConstants, name) and name.isupper():
        return getattr(AutomationConstants, name)
    raise KeyError(f"Constant {name} not found")
