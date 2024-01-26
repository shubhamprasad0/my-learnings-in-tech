def add_highlight(func):
    def wrapper(*args, **kwargs):
        return f"""
{"-" * 80}
{func(*args, **kwargs)}
{"-" * 80}
"""

    return wrapper

@add_highlight
def create_greeting(name):
    return f"Hello {name}, how are you doing?"

# The return value here is actually the return value of the wrapper inside add_highlight
#
# So, the wrapper function inside the decorator decides what to do with the return value
# of the decorated function
greet_shubham = create_greeting("Shubham")

print(greet_shubham)