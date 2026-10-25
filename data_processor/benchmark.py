"""Модуль експериментального порівняння швидкості пошуку (Benchmark)."""

from time import perf_counter


def run_benchmark() -> None:
    """Порівнює лінійний пошук у списку та прямий доступ у dict."""
    sizes = [1_000, 10_000, 100_000]
    results = []

    print("\n" + "=" * 60)
    print("БЕНЧМАРК: Пошук товару в List O(n) vs Dict-index O(1)")
    print("=" * 60)

    for size in sizes:
        # Синтетичні дані
        dataset = [
            {"id": i, "name": f"Product_{i}", "price": 100.0, "quantity": 10}
            for i in range(size)
        ]
        target_id = size - 1  # Найгірший випадок — останній елемент

        # 1. Пошук у списку
        t_start = perf_counter()
        _ = None
        for item in dataset:
            if item["id"] == target_id:
                _ = item
                break
        time_list = perf_counter() - t_start

        # 2. Пошук у dict індексі
        index = {item["id"]: item for item in dataset}
        t_start = perf_counter()
        _ = index.get(target_id)
        time_dict = perf_counter() - t_start

        results.append((size, time_list, time_dict))

    print(f"{'Кількість (records)':<20} | {'List Search (s)':<18} | {'Dict Search (s)':<18}")
    print("-" * 62)
    for size, tl, td in results:
        print(f"{size:<20} | {tl:<18.8f} | {td:<18.8f}")
    print("=" * 60 + "\n")