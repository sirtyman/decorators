from utils.decorators import timer


@timer
def waste_some_time(num_times):
    """Some function that consumes the CPU power and thus delays execution of a code."""
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])


if __name__ == "__main__":
    print(f"__name__: {waste_some_time.__name__}")
    print(f"__doc__: {waste_some_time.__doc__}")
    waste_some_time(num_times=10)
    waste_some_time(num_times=100)
