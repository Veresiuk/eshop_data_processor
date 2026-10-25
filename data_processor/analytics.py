"""Модуль аналітики, розрахунків та замикань."""

from collections.abc import Callable
from typing import Any
from data_processor.decorators import measure_time


@measure_time
def calculate_total_inventory_value(items: list[dict]) -> float:
    """Обчислює загальну вартість усіх залишків на складі (Generator expression)."""
    return sum(item["price"] * item["quantity"] for item in items)


def calculate_average_price(*prices: float) -> float:
    """Обчислює середнє значення довільної кількості цін (*args)."""
    if not prices:
        return 0.0
    return sum(prices) / len(prices)


def create_product_record(**fields: Any) -> dict[str, Any]:
    """Створює новий товарний запис із довільних іменованих параметрів (**kwargs)."""
    return dict(fields)


def find_most_expensive_product(items: list[dict]) -> dict | None:
    """Знаходить найдорожчий товар у каталозі (Lambda)."""
    if not items:
        return None
    return max(items, key=lambda item: item["price"])


def sort_products_by_price(items: list[dict], descending: bool = True) -> list[dict]:
    """Сортує товари за ціною (Lambda)."""
    return sorted(items, key=lambda item: item["price"], reverse=descending)


def create_low_stock_filter(threshold: int) -> Callable[[dict], bool]:
    """
    Closure (Замикання): повертає функцію, яка пам'ятає граничну кількість threshold
    та визначає товари з кількістю нижче заданої.
    """
    def is_low_stock(item: dict) -> bool:
        return item["quantity"] < threshold
    return is_low_stock