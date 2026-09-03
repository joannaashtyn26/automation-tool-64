import time
import functools
import logging
from typing import Callable, Any, Type, Union, Tuple

logger = logging.getLogger('automation_tool')

def retry(
    exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]],
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt_tries = tries
            attempt_delay = delay
            while attempt_tries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(
                        'Retrying %s in %s seconds due to: %s',
                        func.__name__,
                        attempt_delay,
                        e
                    )
                    time.sleep(attempt_delay)
                    attempt_tries -= 1
                    attempt_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator