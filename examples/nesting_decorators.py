from utils.decorators import repeat,debug, timer


@debug
@timer
@repeat(times=20)
def greet(name):
    print(f"Hello {name}")


if __name__ == "__main__":
    greet("My Lord")
