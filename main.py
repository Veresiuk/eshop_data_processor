"""Точка входу для запуску аналізу інтернет-магазину (Варіант 3)."""

from data_processor.analytics import (
    calculate_average_price,
    calculate_total_inventory_value,
    create_low_stock_filter,
    create_product_record,
    find_most_expensive_product,
    sort_products_by_price,
)
from data_processor.benchmark import run_benchmark
from data_processor.data import products
from data_processor.processors import (
    count_products_by_category,
    create_product_index,
    filter_by_category,
    filter_items,
    get_unique_categories,
    group_by_category,
    operation_log,
)


def print_catalog(title: str, items: list[dict]) -> None:
    """Друк списку товарів у зручному вигляді."""
    print(f"\n{title}")
    print("-" * 75)
    for p in items:
        dims = p.get("dimensions", (0, 0, 0))
        print(
            f"ID: {p['id']:<4} | Назва: {p['name']:<28} | "
            f"Категорія: {p['category']:<16} | Ціна: {p['price']:<9.2f} грн | "
            f"К-сть: {p['quantity']:<3} | Габарити: {dims}"
        )


def main() -> None:
    # 1. Повний список товарів
    print_catalog("Усі товари магазину (List of Dicts + Tuples):", products)

    # 2. Унікальні категорії (Set comprehension)
    unique_categories = get_unique_categories(products)
    print(f"\nУнікальні категорії (Set): {unique_categories}")

    # 3. Групування за категоріями (defaultdict)
    grouped = group_by_category(products)
    print("\nГрупування за категоріями (defaultdict):")
    for cat, items in grouped.items():
        print(f"  [{cat}]: {[item['name'] for item in items]}")

    # 4. Загальна вартість залишків (Агрегація + Декоратор)
    total_val = calculate_total_inventory_value(products)
    print(f"Загальна вартість залишків на складі: {total_val:,.2f} грн")

    # 5. Dict-index за кодом товару та швидкий пошук
    product_index = create_product_index(products)
    search_id = 104
    found = product_index.get(search_id)
    print(f"\nПошук товару за ID={search_id} (Dict-index): {found['name'] if found else 'Не знайдено'}")

    # 6. Фільтрація за категорією
    electronics = filter_by_category(products, "Електроніка")
    print_catalog("Товари категорії 'Електроніка' (List comprehension):", electronics)

    # 7. Найдорожчий товар (Lambda)
    most_expensive = find_most_expensive_product(products)
    if most_expensive:
        print(f"\nНайдорожчий товар: {most_expensive['name']} ({most_expensive['price']:.2f} грн)")

    # 8. Сортування за ціною (Lambda)
    sorted_catalog = sort_products_by_price(products, descending=True)
    print_catalog("Каталог, відсортований за спаданням ціни:", sorted_catalog)

    # 9. Closure (Замикання): товари із залишком менше ніж 5 шт.
    low_stock_limit = 5
    is_critical_stock = create_low_stock_filter(low_stock_limit)
    low_stock_products = [p for p in products if is_critical_stock(p)]
    print_catalog(f"Товари з критичним залишком (< {low_stock_limit} шт.) (Closure):", low_stock_products)

    # 10. Counter: кількість товарів за категоріями
    cat_counts = count_products_by_category(products)
    print("\nКількість найменувань за категоріями (Counter):")
    for cat, count in cat_counts.items():
        print(f"  {cat}: {count}")

    # 11. Демонстрація *args
    avg_price = calculate_average_price(45000.0, 32000.0, 8500.0, 18500.0)
    print(f"\nСередня ціна вибірки (*args): {avg_price:.2f} грн")

    # 12. Демонстрація **kwargs
    new_prod = create_product_record(
        id=107,
        name="Монітор Dell 27",
        category="Електроніка",
        price=11200.0,
        quantity=5,
        dimensions=(61.2, 36.4, 5.2),
    )
    print(f"\nСтворено новий товар (**kwargs): {new_prod}")

    # 13. Демонстрація deque
    print(f"\nОстанні виконані операції (collections.deque): {list(operation_log)}")

    # 14. Запуск експериментального бенчмарку
    run_benchmark()


if __name__ == "__main__":
    main()