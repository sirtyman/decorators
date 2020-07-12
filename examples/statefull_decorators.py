import functools
from utils.decorators import count_calls


@count_calls
def say_whee():
    print("Whee!")


if __name__ == "__main__":
    for _ in range(100):
        say_whee()
