import functools

class Counter:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@Counter
def say_hello(name):
    print(f"Hello, {name}!")

@Counter
def say_bye(name):
    print(f"Bye, {name}!")

say_hello("Shubham")
say_bye("Shubham")
say_hello("Neo")
say_bye("Neo")