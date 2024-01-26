import functools

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

@count_calls
def say_hello(name):
    print(f"Hello, {name}!")

@count_calls
def say_bye(name):
    print(f"Bye, {name}!")

say_hello("Shubham")
say_hello("John")
say_hello("Doe")


say_bye("Shubham")
say_bye("John")
say_bye("Doe")