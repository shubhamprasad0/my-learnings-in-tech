PLUGINS = {}

# Decorators don't need to wrap the function. They can even return them unwrapped.
# Here, we are creating a lightweight plugin architecture where the functions
# register themselves as plugins when they are decorated with @register.
# The register decorator just saves the reference of the function, and returns
# it unwrapped. So, we don't need any functools.wraps or any inner function too.
def register(func):
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    print(f"Hello {name}!")

@register
def say_good_morning(name):
    print(f"Good morning, {name}!")

# The above architecture saves us from creating a list of these
# available greeter plugins. The plugins register themselves with
# the @register decorator. We can then use them from the PLUGINS dict.

def greet(name, greeting_type="hello"):
    PLUGINS[f"say_{greeting_type}"](name)

greet("Shubham", "hello")
greet("Shubham", "good_morning")