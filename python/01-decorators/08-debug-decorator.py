import functools

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print("-"*40 + " <START> " + "-"*40)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"Function {func.__name__!r} returned {value!r}")
        print("-"*40 + "  <END>  " + "-"*40)

    return wrapper


@debug
def add(*args, **kwargs):
    s = sum(args)
    s += sum(kwargs.values())
    return s

@debug
def print_participants(names_and_roles):
    for name, role in names_and_roles.items():
        print(f"{name} -> {role}")


add(1, 2, 3, v1=2, v2=5)
print_participants({
    "Shubham": "Admin",
    "John": "Member"
})