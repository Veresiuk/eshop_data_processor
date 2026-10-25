"""Модуль збереження та ініціалізації товарів інтернет-магазину."""

products: list[dict] = [
    {
        "id": 101,
        "name": "Ноутбук ASUS ROG",
        "category": "Електроніка",
        "price": 45000.0,
        "quantity": 7,
        "dimensions": (35.4, 25.1, 2.2),  # tuple (довжина, ширина, висота в см)
    },
    {
        "id": 102,
        "name": "Смартфон Samsung S23",
        "category": "Електроніка",
        "price": 32000.0,
        "quantity": 3,
        "dimensions": (14.6, 7.0, 0.7),
    },
    {
        "id": 103,
        "name": "Офісне крісло Ergonomic",
        "category": "Меблі",
        "price": 8500.0,
        "quantity": 12,
        "dimensions": (65.0, 65.0, 115.0),
    },
    {
        "id": 104,
        "name": "Кавомашина DeLonghi",
        "category": "Побутова техніка",
        "price": 18500.0,
        "quantity": 4,
        "dimensions": (24.0, 44.0, 36.0),
    },
    {
        "id": 105,
        "name": "Механічна клавіатура Keychron",
        "category": "Електроніка",
        "price": 4200.0,
        "quantity": 15,
        "dimensions": (31.0, 12.0, 3.5),
    },
    {
        "id": 106,
        "name": "Пилосос Dyson",
        "category": "Побутова техніка",
        "price": 24000.0,
        "quantity": 2,
        "dimensions": (25.0, 26.0, 126.0),
    },
]