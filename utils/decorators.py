import functools
import time


def debug(func):
    """Print the function signature and return value."""
    @functools.wraps(func)  # keep the original function __doc__ and __name__
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value

    return wrapper_debug


def do_twice(func):
    """Execute decorated function 2 times."""
    @functools.wraps(func)  # keep the original function __doc__ and __name__
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


def repeat(_func=None, *, times=2):
    """Decorator to repeat n-times execution of a function."""
    def decorator_repeat(func):
        @functools.wraps(func)  # keep the original function __doc__ and __name__
        def wrapper(*args, **kwargs):
            for _ in range(times):
                value = func(*args, *kwargs)
            return value
        return wrapper

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


def timer(func):
    """Print the runtime of the decorated function."""
    @functools.wraps(func)  # keep the original function __doc__ and __name__
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


def count_calls(func):
    """Count calls of a decorated function. This is the simple example of stateful decorator."""
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__}")
        return func(*args, **kwargs)
    # Add attribute to wrapped_count_calls. Note that decorators are created on compile time!
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls