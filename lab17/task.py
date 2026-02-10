import random
import time
from collections import Counter, defaultdict

# --- БЛОК 1: Створення та основи множин (Sets) ---

def task_1_create_set():
    """Створення множини різними способами"""
    s1 = {1, 2, 3}
    s2 = set([3, 4, 5])
    print(f"Літерал: {s1}")
    print(f"Зі списку: {s2}")

def task_2_add_element():
    """Додавання елементів .add()"""
    s = {1, 2}
    print(f"До: {s}")
    s.add(3)
    s.add(2) # Дублікат не додасться
    print(f"Після додавання 3 та 2: {s}")

def task_3_remove_element():
    """Видалення: .remove() vs .discard()"""
    s = {1, 2, 3, 4}
    s.remove(2)      # Викине помилку, якщо нема
    s.discard(10)    # Не викине помилку, якщо нема
    print(f"Результат: {s}")

def task_4_pop_element():
    """Метод .pop() - видаляє випадковий елемент"""
    s = {"apple", "banana", "cherry"}
    removed = s.pop()
    print(f"Видалено: {removed}")
    print(f"Залишилось: {s}")

def task_5_clear_set():
    """Очищення множини"""
    s = {1, 2, 3}
    s.clear()
    print(f"Очищена множина: {s}")

# --- БЛОК 2: Операції над множинами ---

def task_6_union():
    """Об'єднання (| або union)"""
    A = {1, 2, 3}
    B = {3, 4, 5}
    print(f"A | B: {A | B}")

def task_7_intersection():
    """Перетин (& або intersection)"""
    A = {1, 2, 3}
    B = {3, 4, 5}
    print(f"A & B (спільні): {A & B}")

def task_8_difference():
    """Різниця (- або difference)"""
    A = {1, 2, 3}
    B = {3, 4, 5}
    print(f"A - B (тільки в А): {A - B}")
    print(f"B - A (тільки в В): {B - A}")

def task_9_symmetric_difference():
    """Симетрична різниця (^): унікальні для обох"""
    A = {1, 2, 3}
    B = {3, 4, 5}
    print(f"A ^ B: {A ^ B}")

def task_10_subsets():
    """Підмножини та надмножини"""
    A = {1, 2}
    B = {1, 2, 3, 4}
    print(f"A є підмножиною B? {A.issubset(B)}")
    print(f"B є надмножиною A? {B.issuperset(A)}")

# --- БЛОК 3: Створення та основи словників (Dictionaries) ---

def task_11_create_dict():
    """Створення словника"""
    d = {"name": "Ivan", "age": 20}
    print(f"Словник: {d}")
    print(f"Тип: {type(d)}")

def task_12_access_value():
    """Доступ за ключем"""
    d = {"brand": "Ford", "model": "Mustang"}
    print(f"Model: {d['model']}")

def task_13_get_method():
    """Безпечний доступ .get()"""
    d = {"a": 1}
    print(f"Існуючий ключ: {d.get('a')}")
    print(f"Неіснуючий (default): {d.get('b', 'Not Found')}")

def task_14_add_update():
    """Додавання та зміна значень"""
    d = {"x": 10}
    d["x"] = 20    # Оновлення
    d["y"] = 30    # Додавання
    print(f"Оновлений: {d}")

def task_15_remove_dict_item():
    """Видалення з словника .pop()"""
    d = {"a": 1, "b": 2, "c": 3}
    val = d.pop("b")
    print(f"Видалено значення: {val}")
    print(f"Словник: {d}")

# --- БЛОК 4: Методи словників ---

def task_16_keys():
    """Метод .keys()"""
    d = {"name": "Alex", "age": 25}
    print(f"Ключі: {list(d.keys())}")

def task_17_values():
    """Метод .values()"""
    d = {"name": "Alex", "age": 25}
    print(f"Значення: {list(d.values())}")

def task_18_items():
    """Метод .items() - пари"""
    d = {"a": 1, "b": 2}
    for k, v in d.items():
        print(f"Key: {k}, Value: {v}")

def task_19_check_key():
    """Перевірка наявності ключа (in)"""
    d = {"user": "admin"}
    if "user" in d:
        print("Ключ 'user' знайдено")

def task_20_copy_dict():
    """Копіювання словника"""
    d1 = {"a": 1}
    d2 = d1.copy()
    d2["a"] = 100
    print(f"Оригінал: {d1} (не змінився)")
    print(f"Копія: {d2}")

# --- БЛОК 5: Практичні перетворення ---

def task_21_list_to_set():
    """Видалення дублікатів зі списку"""
    lst = [1, 2, 2, 3, 3, 3, 4]
    unique = list(set(lst))
    print(f"Список: {lst}")
    print(f"Унікальні: {unique}")

def task_22_lists_to_dict():
    """Два списки -> Словник (zip)"""
    keys = ["name", "age", "city"]
    vals = ["Anna", 22, "Kyiv"]
    d = dict(zip(keys, vals))
    print(d)

def task_23_dict_comprehension():
    """Словникове включення (квадрати)"""
    squares = {x: x**2 for x in range(1, 6)}
    print(f"Квадрати: {squares}")

def task_24_set_comprehension():
    """Множинне включення"""
    text = "hello world"
    vowels = {char for char in text if char in "aeiou"}
    print(f"Голосні в тексті: {vowels}")

def task_25_count_chars():
    """Частота символів (через get)"""
    s = "banana"
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    print(f"Частота: {counts}")

# --- БЛОК 6: Складніші задачі та бібліотеки ---

def task_26_counter():
    """collections.Counter"""
    lst = ["a", "b", "a", "c", "b", "a"]
    c = Counter(lst)
    print(f"Counter: {c}")
    print(f"Найпоширеніший: {c.most_common(1)}")

def task_27_defaultdict():
    """collections.defaultdict"""
    # Дозволяє не перевіряти чи існує ключ
    dd = defaultdict(int)
    words = ["apple", "pear", "apple"]
    for w in words:
        dd[w] += 1
    print(f"Результат: {dict(dd)}")

def task_28_frozen_set():
    """frozenset (незмінна множина)"""
    fs = frozenset([1, 2, 3])
    print(f"Frozenset: {fs}")
    try:
        fs.add(4)
    except AttributeError:
        print("Помилка: Frozenset не можна змінювати")

def task_29_nested_dict():
    """Вкладені словники"""
    students = {
        "Student1": {"math": 90, "history": 80},
        "Student2": {"math": 75, "history": 85}
    }
    print(f"Оцінка Student1 з math: {students['Student1']['math']}")

def task_30_merge_dicts():
    """Об'єднання словників (update)"""
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    d1.update(d2)
    print(f"Оновлений d1: {d1}")

# --- БЛОК 7: Часова складність та реальні задачі ---

def task_31_time_complexity():
    """Порівняння швидкості пошуку (Set vs List)"""
    size = 1000000
    large_list = list(range(size))
    large_set = set(range(size))
    target = size - 1

    start = time.time()
    _ = target in large_list
    list_time = time.time() - start

    start = time.time()
    _ = target in large_set
    set_time = time.time() - start

    print(f"Пошук у List: {list_time:.6f} сек (O(n))")
    print(f"Пошук у Set:  {set_time:.6f} сек (O(1))")
    print(f"Set швидший у {list_time/set_time:.0f} разів!")

def task_32_unique_words():
    """Кількість унікальних слів у реченні"""
    text = "python is good python is cool"
    words = text.split()
    unique = set(words)
    print(f"Всього слів: {len(words)}")
    print(f"Унікальних: {len(unique)}")

def task_33_sort_dict_by_value():
    """Сортування словника за значенням"""
    d = {"apple": 5, "banana": 2, "cherry": 10}
    sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
    print(f"Відсортовано: {sorted_d}")

def task_34_invert_dict():
    """Інверсія словника (ключ <-> значення)"""
    d = {"a": 1, "b": 2, "c": 3}
    inverted = {v: k for k, v in d.items()}
    print(f"Оригінал: {d}")
    print(f"Інверсія: {inverted}")

def task_35_common_in_lists():
    """Спільні елементи (через set intersection)"""
    l1 = [1, 2, 3, 4, 5]
    l2 = [4, 5, 6, 7, 8]
    common = list(set(l1) & set(l2))
    print(f"Спільні: {common}")

def task_36_filter_dict():
    """Фільтрація словника (ціна > 100)"""
    prices = {"bread": 20, "caviar": 500, "milk": 40, "truffle": 1000}
    expensive = {k: v for k, v in prices.items() if v > 100}
    print(f"Дорогі товари: {expensive}")

def task_37_max_key():
    """Ключ з максимальним значенням"""
    scores = {"Ann": 80, "Bob": 95, "Charlie": 88}
    winner = max(scores, key=scores.get)
    print(f"Переможець: {winner} ({scores[winner]})")

def task_38_set_operations_string():
    """Унікальні літери двох слів"""
    w1 = "hello"
    w2 = "world"
    print(f"Літери в обох: {set(w1) & set(w2)}")
    print(f"Всі унікальні літери: {set(w1) | set(w2)}")

def task_39_database_simulation():
    """Імітація бази даних (ID -> Record)"""
    db = {
        101: {"name": "Alice", "role": "User"},
        102: {"name": "Bob", "role": "Admin"}
    }
    user_id = 102
    if user_id in db:
        print(f"Доступ надано: {db[user_id]['name']}")
    else:
        print("Користувача не знайдено")

def task_40_conflict_explanation():
    """Пояснення конфліктів хешування"""
    print("У Python словники та множини працюють на основі хеш-таблиць.")
    print("Конфлікт (колізія) - це коли hash(key1) == hash(key2).")
    print("Python вирішує це методом 'відкритої адресації' (Open Addressing).")
    print("Часова складність у середньому O(1), у гіршому (багато колізій) O(n).")

# --- ГОЛОВНЕ МЕНЮ ---

def main():
    tasks = [
        task_1_create_set, task_2_add_element, task_3_remove_element, task_4_pop_element, task_5_clear_set,
        task_6_union, task_7_intersection, task_8_difference, task_9_symmetric_difference, task_10_subsets,
        task_11_create_dict, task_12_access_value, task_13_get_method, task_14_add_update, task_15_remove_dict_item,
        task_16_keys, task_17_values, task_18_items, task_19_check_key, task_20_copy_dict,
        task_21_list_to_set, task_22_lists_to_dict, task_23_dict_comprehension, task_24_set_comprehension, task_25_count_chars,
        task_26_counter, task_27_defaultdict, task_28_frozen_set, task_29_nested_dict, task_30_merge_dicts,
        task_31_time_complexity, task_32_unique_words, task_33_sort_dict_by_value, task_34_invert_dict, task_35_common_in_lists,
        task_36_filter_dict, task_37_max_key, task_38_set_operations_string, task_39_database_simulation, task_40_conflict_explanation
    ]

    while True:
        print("\n" + "="*50)
        print("ЛАБОРАТОРНА: МНОЖИНИ ТА СЛОВНИКИ")
        print("="*50)
        print("1-10:  Базові операції з множинами (Sets)")
        print("11-20: Базові операції зі словниками (Dicts)")
        print("21-25: Перетворення та включення (Comprehensions)")
        print("26-30: Розширені можливості (Counter, Defaultdict)")
        print("31-40: Реальні задачі та алгоритми")
        print("-" * 50)
        
        try:
            choice = int(input("Введіть номер завдання (1-40) або 0 для виходу: "))
            if choice == 0:
                print("Завершення роботи.")
                break
            
            if 1 <= choice <= 40:
                print(f"\n--- Завдання {choice} ---")
                tasks[choice - 1]()
                input("\nНатисніть Enter...")
            else:
                print("Невірний номер.")
        except ValueError:
            print("Будь ласка, введіть число.")

if __name__ == "__main__":
    main()