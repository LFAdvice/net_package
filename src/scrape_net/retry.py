import time
import random
import functools
import logging

logger = logging.getLogger("scrape_net.retry")

def retry(
    attempts: int = 5,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: float = 0.3,
    exceptions=(Exception,),
):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            _delay = delay

            for attempt in range(1, attempts + 1):

                try:
                    return func(*args, **kwargs)

                except exceptions as e:

                    if attempt == attempts:
                        logger.error(
                            "retry failed func=%s attempts=%d",
                            func.__name__,
                            attempts,
                        )
                        raise

                    sleep_time = _delay + random.uniform(0, jitter)

                    logger.warning(
                        "retry func=%s attempt=%d sleep=%.2f error=%s",
                        func.__name__,
                        attempt,
                        sleep_time,
                        repr(e),
                    )

                    time.sleep(sleep_time)

                    _delay *= backoff

        return wrapper

    return decorator
