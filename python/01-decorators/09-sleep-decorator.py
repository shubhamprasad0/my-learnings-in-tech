import functools
import time


def wait_1_sec(func):
    def wrapper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper

@wait_1_sec
def countdown(counts=5):
    if counts < 1:
        print("Liftoff")
    else:
        print(counts)
        countdown(counts - 1)

countdown(10)