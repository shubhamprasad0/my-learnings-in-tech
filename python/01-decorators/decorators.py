import functools

def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper

def count_calls(func):
    '''
    This decorator counts how many times its decorated function is called
    '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Call {wrapper.count} of {func.__name__!r}")
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper