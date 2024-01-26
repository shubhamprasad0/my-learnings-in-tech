def my_decorator(func):
    def wrapper():
        print("Something before")
        func()
        print("Something after")

    return wrapper


# @my_decorator instead of scream_loudly = my_decorator(scream_loudly)
@my_decorator
def scream_loudly():
    print("HELLOOOO!")

scream_loudly()