import random

# --- БЛОК 1: Створення та базові операції ---

def task_1_create_list():
    """Створення списку різних типів даних"""
    my_list = [1, "Python", 3.14, True, [1, 2]]
    print(f"Створено список: {my_list}")
    print(f"Тип даних: {type(my_list)}")

def task_2_create_tuple():
    """Створення кортежу (tuple)"""
    my_tuple = (10, 20, "Apple", 5.5)
    print(f"Створено кортеж: {my_tuple}")
    print(f"Тип даних: {type(my_tuple)}")

def task_3_access_elements():
    """Доступ за індексом"""
    lst = ["a", "b", "c", "d", "e"]
    print(f"Список: {lst}")
    print(f"Перший елемент [0]: {lst[0]}")
    print(f"Останній елемент [-1]: {lst[-1]}")

def task_4_change_element():
    """Зміна елементу списку"""
    lst = [10, 20, 30, 40]
    print(f"До: {lst}")
    lst[1] = 999
    print(f"Після зміни lst[1] = 999: {lst}")

def task_5_tuple_immutability():
    """Демонстрація незмінності кортежу"""
    tpl = (1, 2, 3)
    print(f"Кортеж: {tpl}")
    print("Спроба змінити tpl[0] = 100...")
    try:
        tpl[0] = 100
    except TypeError as e:
        print(f"Помилка! {e}")
        print("Кортежі не можна змінювати.")

# --- БЛОК 2: Методи додавання та видалення ---

def task_6_append():
    """Метод append()"""
    lst = []
    for i in range(5):
        lst.append(random.randint(1, 10))
    print(f"Заповнений список: {lst}")

def task_7_insert():
    """Метод insert() - вставка за індексом"""
    lst = ["start", "end"]
    print(f"До: {lst}")
    lst.insert(1, "middle")
    print(f"Після insert(1, 'middle'): {lst}")

def task_8_extend():
    """Метод extend() - розширення списку"""
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    lst1.extend(lst2)
    print(f"Об'єднаний список: {lst1}")

def task_9_remove():
    """Метод remove() - видалення за значенням"""
    lst = [10, 20, 30, 20, 40]
    print(f"Список: {lst}")
    lst.remove(20)
    print(f"Після remove(20) (видаляє перше входження): {lst}")

def task_10_pop():
    """Метод pop() - видалення за індексом"""
    lst = ["a", "b", "c", "d"]
    print(f"Список: {lst}")
    deleted = lst.pop(2)
    print(f"Видалено елемент з індексом 2: {deleted}")
    print(f"Список після pop: {lst}")

def task_11_clear():
    """Очищення списку"""
    lst = [1, 2, 3, 4, 5]
    print(f"Було: {lst}")
    lst.clear()
    print(f"Стало: {lst}")

# --- БЛОК 3: Зрізи (Slicing) ---

def task_12_slice_basic():
    """Простий зріз [start:end]"""
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Список: {lst}")
    print(f"Зріз [2:6]: {lst[2:6]}")

def task_13_slice_step():
    """Зріз з кроком [::step]"""
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Кожен другий [::2]: {lst[::2]}")

def task_14_slice_reverse():
    """Реверс через зріз [::-1]"""
    s = "Hello Python"
    lst = list(s)
    print(f"Оригінал: {lst}")
    print(f"Реверс: {lst[::-1]}")

def task_15_tuple_slicing():
    """Зрізи на кортежах"""
    tpl = (10, 20, 30, 40, 50)
    print(f"Кортеж: {tpl}")
    print(f"Перші три [:3]: {tpl[:3]}")

# --- БЛОК 4: Вбудовані функції ---

def task_16_len():
    """Довжина списку len()"""
    lst = [random.random() for _ in range(random.randint(5, 15))]
    print(f"Список: {lst}")
    print(f"Кількість елементів: {len(lst)}")

def task_17_min_max():
    """Функції min() та max()"""
    lst = [random.randint(1, 100) for _ in range(10)]
    print(f"Список: {lst}")
    print(f"Min: {min(lst)}, Max: {max(lst)}")

def task_18_sum():
    """Сума елементів sum()"""
    nums = (5, 10, 15, 20)
    print(f"Кортеж чисел: {nums}")
    print(f"Сума: {sum(nums)}")

def task_19_sorted():
    """Функція sorted() vs метод .sort()"""
    lst = [5, 1, 8, 3]
    print(f"Оригінал: {lst}")
    new_lst = sorted(lst)
    print(f"sorted(lst) (повертає новий): {new_lst}")
    lst.sort()
    print(f"lst.sort() (змінює поточний): {lst}")

def task_20_count():
    """Підрахунок входжень .count()"""
    lst = [1, 2, 3, 1, 1, 4, 5]
    print(f"Список: {lst}")
    print(f"Кількість одиниць: {lst.count(1)}")

def task_21_index():
    """Пошук індексу .index()"""
    fruits = ("apple", "banana", "cherry", "date")
    target = "cherry"
    if target in fruits:
        print(f"Кортеж: {fruits}")
        print(f"Індекс '{target}': {fruits.index(target)}")

# --- БЛОК 5: Спискові включення (List Comprehensions) ---

def task_22_squares_comp():
    """Квадрати чисел"""
    squares = [x**2 for x in range(10)]
    print(f"Квадрати (0-9): {squares}")

def task_23_filter_comp():
    """Фільтрація (тільки парні)"""
    nums = [random.randint(1, 50) for _ in range(15)]
    evens = [x for x in nums if x % 2 == 0]
    print(f"Всі: {nums}")
    print(f"Парні: {evens}")

def task_24_string_comp():
    """Обробка рядків у списку"""
    words = ["hello", "world", "python"]
    upper_words = [w.upper() for w in words]
    print(f"До: {words}")
    print(f"Після: {upper_words}")

def task_25_nested_comp():
    """Створення матриці"""
    matrix = [[j for j in range(3)] for i in range(3)]
    print("Матриця 3x3:")
    for row in matrix:
        print(row)

# --- БЛОК 6: Перетворення та операції ---

def task_26_tuple_to_list():
    """Конвертація типів list() <-> tuple()"""
    tpl = (1, 2, 3)
    lst = list(tpl)
    lst.append(4)
    new_tpl = tuple(lst)
    print(f"Був кортеж: {tpl}")
    print(f"Став список (змінили): {lst}")
    print(f"Знову кортеж: {new_tpl}")

def task_27_unpacking():
    """Розпакування кортежу"""
    coordinates = (10, 25)
    x, y = coordinates
    print(f"Координати: {coordinates}")
    print(f"x = {x}, y = {y}")

def task_28_join_split():
    """Перетворення Рядок <-> Список"""
    s = "Python is awesome"
    words = s.split()
    print(f"Split: {words}")
    rejoined = "-".join(words)
    print(f"Join: {rejoined}")

def task_29_enumerate():
    """Використання enumerate()"""
    animals = ["cat", "dog", "bird"]
    print("Список з індексами:")
    for index, value in enumerate(animals):
        print(f"{index}: {value}")

def task_30_zip():
    """Об'єднання списків zip()"""
    names = ["Anna", "Bob", "Mike"]
    ages = [25, 30, 35]
    combined = list(zip(names, ages))
    print(f"Імена: {names}")
    print(f"Вік: {ages}")
    print(f"Разом: {combined}")

# --- БЛОК 7: Практичні завдання ---

def task_31_remove_duplicates():
    """Видалення дублікатів (через set)"""
    lst = [1, 2, 2, 3, 4, 4, 4, 5]
    unique = list(set(lst))
    print(f"З дублями: {lst}")
    print(f"Унікальні: {unique}")

def task_32_find_second_largest():
    """Знайти друге найбільше число"""
    nums = [random.randint(1, 100) for _ in range(10)]
    print(f"Список: {nums}")
    unique_sorted = sorted(list(set(nums)))
    if len(unique_sorted) >= 2:
        print(f"Друге найбільше: {unique_sorted[-2]}")
    else:
        print("Список замалий")

def task_33_filter_by_len():
    """Фільтр слів за довжиною > 5"""
    words = ["apple", "banana", "kiwi", "strawberry", "fig"]
    long_words = [w for w in words if len(w) > 5]
    print(f"Слова: {words}")
    print(f"Довгі (>5): {long_words}")

def task_34_swap_elements():
    """Поміняти місцями перший і останній елемент"""
    lst = [1, 2, 3, 4, 5]
    print(f"До: {lst}")
    lst[0], lst[-1] = lst[-1], lst[0]
    print(f"Після: {lst}")

def task_35_flatten_list():
    """Вирівнювання вкладеного списку"""
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = [num for sublist in nested for num in sublist]
    print(f"Вкладений: {nested}")
    print(f"Плоский: {flat}")

def task_36_random_choice():
    """Випадковий елемент зі списку"""
    colors = ["Red", "Green", "Blue", "Yellow"]
    print(f"Кольори: {colors}")
    print(f"Випало: {random.choice(colors)}")

def task_37_shuffle():
    """Перемішування списку"""
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Порядок: {deck}")
    random.shuffle(deck)
    print(f"Перемішано: {deck}")

def task_38_common_elements():
    """Спільні елементи двох списків"""
    a = [1, 2, 3, 4, 5]
    b = [4, 5, 6, 7, 8]
    common = list(set(a) & set(b))
    print(f"A: {a}, B: {b}")
    print(f"Спільні: {common}")

def task_39_dict_from_lists():
    """Створення словника з двох списків"""
    keys = ["name", "age", "city"]
    values = ["Alice", 25, "Kyiv"]
    my_dict = dict(zip(keys, values))
    print(f"Ключі: {keys}")
    print(f"Значення: {values}")
    print(f"Словник: {my_dict}")

def task_40_average_of_tuples():
    """Середнє значення елементів у списку кортежів"""
    data = [(10, 20), (30, 40), (50, 60)]
    averages = [sum(t)/len(t) for t in data]
    print(f"Дані: {data}")
    print(f"Середні значення: {averages}")

# --- ГОЛОВНЕ МЕНЮ ---

def main():
    tasks = [
        task_1_create_list, task_2_create_tuple, task_3_access_elements, task_4_change_element, task_5_tuple_immutability,
        task_6_append, task_7_insert, task_8_extend, task_9_remove, task_10_pop,
        task_11_clear, task_12_slice_basic, task_13_slice_step, task_14_slice_reverse, task_15_tuple_slicing,
        task_16_len, task_17_min_max, task_18_sum, task_19_sorted, task_20_count,
        task_21_index, task_22_squares_comp, task_23_filter_comp, task_24_string_comp, task_25_nested_comp,
        task_26_tuple_to_list, task_27_unpacking, task_28_join_split, task_29_enumerate, task_30_zip,
        task_31_remove_duplicates, task_32_find_second_largest, task_33_filter_by_len, task_34_swap_elements, task_35_flatten_list,
        task_36_random_choice, task_37_shuffle, task_38_common_elements, task_39_dict_from_lists, task_40_average_of_tuples
    ]

    while True:
        print("\n" + "="*50)
        print("ЛАБОРАТОРНА РОБОТА: СПИСКИ ТА КОРТЕЖІ")
        print("="*50)
        print("1-5: Створення та доступ")
        print("6-11: Методи списків (Add/Remove)")
        print("12-15: Зрізи (Slicing)")
        print("16-21: Вбудовані функції та пошук")
        print("22-25: Спискові включення (List Comprehensions)")
        print("26-30: Перетворення та специфічні функції")
        print("31-40: Практичні задачі")
        print("-" * 50)
        
        try:
            choice = int(input("Введіть номер завдання (1-40) або 0 для виходу: "))
            if choice == 0:
                print("Завершення роботи.")
                break
            
            if 1 <= choice <= 40:
                print(f"\n--- Завдання {choice} ---")
                tasks[choice - 1]()
                input("\nНатисніть Enter, щоб продовжити...")
            else:
                print("Невірний номер. Спробуйте 1-40.")
        except ValueError:
            print("Будь ласка, введіть число.")

if __name__ == "__main__":
    main()