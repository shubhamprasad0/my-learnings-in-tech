def repeat(num_times = 2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(5)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Shubham")