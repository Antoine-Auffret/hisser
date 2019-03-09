from contextlib import contextmanager
from time import clock, perf_counter


_state = {}


def reset_state():
    _state.clear()


def print_state():
    for name, (r, c) in _state.items():
        print('##', name, r, c, flush=True)


@contextmanager
def profile(name):  # pragma: no cover
    real = perf_counter()
    cpu = clock()
    try:
        yield
    finally:
        real_duration = perf_counter() - real
        cpu_duration = clock() - cpu
        old_real, old_cpu = _state.get(name, (0, 0))
        _state[name] = real_duration + old_real, cpu_duration + old_cpu


def profile_func(func):  # pragma: no cover
    def inner(*args, **kwargs):
        with profile(func.__name__):
            return func(*args, **kwargs)
    return inner
