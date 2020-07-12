from utils.decorators import repeat


@repeat
def greeting(name):
    print(f"Hello {name}")


@repeat(times=10)
def greetings(name):
    print(f"Good morning: {name}")


if __name__ == "__main__":
    greeting("My Lord")
    greetings("My Lord")
