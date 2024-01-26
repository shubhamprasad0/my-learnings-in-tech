import functools

def repeat(_func=None, *, num_times=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    
    if _func is None:
        return decorator
    else:
        return decorator(_func)


# Here, we want that if no arguments are given, then it uses the default values
# Otherwise, the provided arguments are used.
# In case of no arguments, we want to use `@repeat` instead of `@repeat()`
@repeat(num_times=5)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Shubham")