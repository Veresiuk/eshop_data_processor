"""Модуль декораторів для оптимізації та контролю виконання."""

from functools import wraps
from time import perf_counter
from typing import Any, Callable


def measure_time(func: Callable) -> Callable:
    """Декоратор для заміру часу виконання функції."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start_time
        print(f"[Timer] {func.__name__}: {elapsed:.8f} s")
        return result
    return wrapper


def repeat(count: int = 1) -> Callable:
    """Параметризований декоратор для повторення виконання."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = None
            for _ in range(count):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator