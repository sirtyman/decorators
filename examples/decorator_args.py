from utils.decorators import repeat, repeat_v2


@repeat
def greeting(name):
    print(f"Hello {name}")


@repeat(times=10)
def greetings(name):
    print(f"Good morning: {name}")


@repeat_v2
def greeting_with_partial(name):
    print(f"Hello {name}")


@repeat_v2(times=3)
def greetings_with_partial(name):
    print(f"Hello {name}")


@repeat_v2(3)
def greetings_with_partial_v2(name):
    print(f"Hello {name}")


if __name__ == "__main__":
    greeting("My Lord")
    greetings("My Lord")
    greeting_with_partial("Marcin")
    greetings_with_partial("Ela")
    greetings_with_partial_v2("Zigi")

