"""Application constants and default configuration settings."""

from enum import Enum
from pathlib import Path
from typing import Final


class Environment(str, Enum):
    """Execution environment modes."""

    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class TaskStatus(str, Enum):
    """Task execution status codes."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3
BACKOFF_FACTOR: Final[float] = 1.5

BASE_DIR: Final[Path] = Path(__file__).resolve().parent
DEFAULT_CONFIG_PATH: Final[Path] = BASE_DIR / "config.json"
DEFAULT_LOG_PATH: Final[Path] = BASE_DIR / "app.log"


def get_environment_defaults(env: Environment) -> dict[str, int | float]:
    """Retrieve environment-specific default timeout and retry settings.

    Args:
        env: Target execution environment.

    Returns:
        Dictionary containing timeout, max_retries, and backoff_factor.
    """
    if env == Environment.DEVELOPMENT:
        return {"timeout": 10, "max_retries": 1, "backoff_factor": 1.0}
    if env == Environment.STAGING:
        return {"timeout": 20, "max_retries": 2, "backoff_factor": 1.2}
    return {
        "timeout": DEFAULT_TIMEOUT,
        "max_retries": MAX_RETRIES,
        "backoff_factor": BACKOFF_FACTOR,
    }
