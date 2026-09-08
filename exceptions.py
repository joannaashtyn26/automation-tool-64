class AutomationError(Exception):
    """Base exception for automation-tool-64."""


class ConfigError(AutomationError):
    """Raised when configuration is invalid."""


class ExecutionError(AutomationError):
    """Raised when a process fails to execute."""


class ValidationError(AutomationError):
    """Raised when input validation fails."""


def raise_if_none(value, name):
    if value is None:
        raise ValidationError(f"{name} cannot be None")


def handle_error(err: Exception):
    print(f"[ERROR] {type(err).__name__}: {err}")


if __name__ == "__main__":
    try:
        raise_if_none(None, "TestField")
    except ValidationError as e:
        handle_error(e)