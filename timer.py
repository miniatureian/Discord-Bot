import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print(f'Finished {func.__name__!r} in {start - end:4f} seconds')
        return value
    return wrapper_timer
