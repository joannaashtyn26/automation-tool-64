import time
import logging
from functools import wraps
from typing import Callable, Tuple, Type, Any

logger = logging.getLogger(__name__)

def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            mtries, mdelay = tries, delay
            while mtries > 0:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    mtries -= 1
                    if mtries == 0:
                        logger.error("Operation %s failed permanently: %s", func.__name__, e)
                        raise
                    logger.warning(
                        "Retrying %s in %.2f seconds (Error: %s), %d attempts left",
                        func.__name__,
                        mdelay,
                        e,
                        mtries,
                    )
                    time.sleep(mdelay)
                    mdelay *= backoff
        return wrapper
    return decorator