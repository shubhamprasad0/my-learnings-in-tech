def my_decorator(func):
    def wrapper():
        print("Something happening before calling func()")
        func()
        print("Something happening after calling func()")

    return wrapper

def scream_loudly():
    print("HELLOOOOOO!")

scream_loudly = my_decorator(scream_loudly)

scream_loudly()