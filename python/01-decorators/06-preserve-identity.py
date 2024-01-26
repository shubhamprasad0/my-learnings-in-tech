import functools


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something before")
        func(*args, **kwargs)
        print("Something after")

    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}")

say_hello("Shubham")

print(say_hello) # This says it is the wrapper function inside my_decorator

print("------------------------------------------------------------------------------")
# We copy the same example with a different name

def my_decorator2(func):
    # This functools.wraps(func) preserves the identity of the decorated function func
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Something before")
        func(*args, **kwargs)
        print("Something after")

    return wrapper

@my_decorator2
def say_hello2(name):
    print(f"Hello, {name}")

say_hello2("Shubham")

print(say_hello2) # This gives the expected information about say_hello2