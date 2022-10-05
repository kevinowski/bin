import datetime
from os import getlogin

def wrapper(func):
    def func1(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('Logging', 'a', encoding="UTF-8") as file:
            file.write(f"Logged at: {datetime.datetime.now()} used {func.__name__} by {getlogin()}\n")
        return result
    return func1
