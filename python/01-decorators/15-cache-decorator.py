import functools
from decorators import count_calls

def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        cache_key = ", ".join(args_repr + kwargs_repr)
        if not wrapper.cache.get(cache_key):
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]
    wrapper.cache = {}
    return wrapper

@cache
@count_calls
def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(20))
print(fibonacci.count)