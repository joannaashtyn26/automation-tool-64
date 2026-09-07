import logging
import sys
from pathlib import Path
from typing import Optional


def get_logger(
    name: str = "automation",
    log_file: Optional[Path] = None,
    level: int = logging.INFO,
) -> logging.Logger:
    """Configures and returns a structured logger instance.

    Args:
        name: Name of the logger instance.
        log_file: Optional path to a file where logs should be written.
        level: Logging level threshold.

    Returns:
        Configured Logger instance with formatted output.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def set_log_level(logger: logging.Logger, level_name: str) -> None:
    """Updates the logging level for an existing logger.

    Args:
        logger: Target logger instance to update.
        level_name: String representation of desired level (e.g., 'DEBUG').
    """
    numeric_level = getattr(logging, level_name.upper(), logging.INFO)
    logger.setLevel(numeric_level)
    for handler in logger.handlers:
        handler.setLevel(numeric_level)
