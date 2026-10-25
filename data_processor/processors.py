"""Модуль обробки, фільтрації, групування та індексації товарів."""

from collections import Counter, defaultdict, deque
from collections.abc import Callable

# Черга deque для фіксації останніх операцій
operation_log: deque[str] = deque(maxlen=5)


def get_unique_categories(items: list[dict]) -> set[str]:
    """Повертає множину унікальних категорій (Set comprehension)."""
    operation_log.append("get_unique_categories")
    return {item["category"] for item in items}


def create_product_index(items: list[dict]) -> dict[int, dict]:
    """Створює індекс товарів за кодом/ID для пошуку за O(1) (Dict comprehension)."""
    operation_log.append("create_product_index")
    return {item["id"]: item for item in items}


def filter_by_category(items: list[dict], category: str) -> list[dict]:
    """Фільтрує товари за категорією (List comprehension)."""
    operation_log.append(f"filter_by_category({category})")
    return [item for item in items if item["category"] == category]


def group_by_category(items: list[dict]) -> dict[str, list[dict]]:
    """Групує товари за категоріями за допомогою defaultdict."""
    operation_log.append("group_by_category")
    grouped = defaultdict(list)
    for item in items:
        grouped[item["category"]].append(item)
    return dict(grouped)


def count_products_by_category(items: list[dict]) -> Counter:
    """Підраховує кількість найменувань товарів у кожній категорії через Counter."""
    operation_log.append("count_products_by_category")
    return Counter(item["category"] for item in items)


def filter_items(
    items: list[dict], predicate: Callable[[dict], bool]
) -> list[dict]:
    """Універсальна функція фільтрації вищого порядку."""
    operation_log.append("filter_items")
    return [item for item in items if predicate(item)]