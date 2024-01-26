from datetime import datetime

def silence_at_night(func):
    def wrapper():
        if 7 <= datetime.now().hour <= 22:
            func()
        else:
            print("HUSH!!")

    return wrapper

def scream_loudly():
    print("HELLOOOOOO!")

scream_loudly = silence_at_night(scream_loudly)

scream_loudly()