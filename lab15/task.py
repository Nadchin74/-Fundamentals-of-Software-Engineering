import math
import random
import itertools
import time

# --- БЛОК 1: Базова математика та прості цикли ---

def task_1_sum_n():
    """Сума чисел від 1 до N (цикл for)"""
    n = int(input("Введіть число N: "))
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"Сума чисел від 1 до {n} = {total}")

def task_2_factorial():
    """Факторіал числа (бібліотека math)"""
    n = int(input("Введіть число: "))
    print(f"Факторіал {n}! = {math.factorial(n)}")

def task_3_even_numbers():
    """Парні числа в діапазоні (цикл for + if)"""
    limit = int(input("Введіть межу діапазону: "))
    evens = [x for x in range(limit + 1) if x % 2 == 0]
    print(f"Парні числа: {evens}")

def task_4_multiplication_table():
    """Таблиця множення для числа (цикл for)"""
    num = int(input("Введіть число для таблиці: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def task_5_check_prime():
    """Перевірка на просте число (цикли + логіка)"""
    n = int(input("Введіть число: "))
    if n < 2:
        print("Не є простим.")
        return
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(f"Число {n} є простим? -> {is_prime}")

# --- БЛОК 2: Робота з рядками ---

def task_6_reverse_string():
    """Реверс рядка (слайсинг або цикл)"""
    s = input("Введіть рядок: ")
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    print(f"Реверс: {reversed_s}")

def task_7_count_vowels():
    """Підрахунок голосних (цикл for + in)"""
    text = input("Введіть текст (лат.): ").lower()
    vowels = "aeiouy"
    count = sum(1 for char in text if char in vowels)
    print(f"Кількість голосних: {count}")

def task_8_palindrome():
    """Перевірка на паліндром"""
    s = input("Введіть слово: ").lower().replace(" ", "")
    print(f"Паліндром? -> {s == s[::-1]}")

def task_9_char_frequency():
    """Частота символів (словник + цикл)"""
    s = input("Введіть рядок: ")
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    print("Частота символів:", freq)

def task_10_ascii_codes():
    """Вивід ASCII кодів символів рядка"""
    s = input("Введіть рядок: ")
    codes = [ord(c) for c in s]
    print(f"ASCII коди: {codes}")

# --- БЛОК 3: Списки та масиви ---

def task_11_max_in_list():
    """Знайти максимум без max()"""
    nums = [random.randint(1, 100) for _ in range(10)]
    print(f"Список: {nums}")
    my_max = nums[0]
    for n in nums:
        if n > my_max:
            my_max = n
    print(f"Максимум: {my_max}")

def task_12_remove_duplicates():
    """Видалення дублікатів (set)"""
    lst = [1, 2, 2, 3, 4, 4, 5, 1]
    print(f"Оригінал: {lst}")
    print(f"Без повторів: {list(set(lst))}")

def task_13_list_sum_average():
    """Сума та середнє арифметичне"""
    lst = [random.randint(1, 50) for _ in range(5)]
    total = sum(lst)
    avg = total / len(lst)
    print(f"Список: {lst}, Сума: {total}, Середнє: {avg}")

def task_14_positive_negative():
    """Розділення списку на додатні та від'ємні"""
    lst = [random.randint(-10, 10) for _ in range(10)]
    pos = [x for x in lst if x > 0]
    neg = [x for x in lst if x < 0]
    print(f"Список: {lst}\n+: {pos}\n-: {neg}")

def task_15_sort_custom():
    """Сортування бульбашкою (вкладені цикли)"""
    arr = [random.randint(1, 20) for _ in range(6)]
    print(f"До: {arr}")
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(f"Після: {arr}")

# --- БЛОК 4: Геометрія та Math ---

def task_16_hypotenuse():
    """Теорема Піфагора"""
    a = float(input("Катет a: "))
    b = float(input("Катет b: "))
    c = math.sqrt(a**2 + b**2)
    print(f"Гіпотенуза: {c:.2f}")

def task_17_circle_area():
    """Площа кола"""
    r = float(input("Радіус: "))
    area = math.pi * (r**2)
    print(f"Площа: {area:.2f}")

def task_18_degrees_to_radians():
    """Градуси в радіани"""
    deg = float(input("Градуси: "))
    print(f"Радіани: {math.radians(deg):.2f}")

def task_19_solve_quadratic():
    """Квадратне рівняння ax^2 + bx + c = 0"""
    print("Рівняння: ax^2 + bx + c = 0")
    a, b, c = map(float, input("Введіть a, b, c через пробіл: ").split())
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"x1 = {x1}, x2 = {x2}")
    elif D == 0:
        print(f"x = {-b / (2*a)}")
    else:
        print("Коренів немає")

def task_20_gcd():
    """НСД двох чисел (math.gcd)"""
    a, b = map(int, input("Введіть два числа: ").split())
    print(f"НСД({a}, {b}) = {math.gcd(a, b)}")

# --- БЛОК 5: Генератори та Itertools ---

def task_21_fibonacci():
    """Числа Фібоначчі (цикл while)"""
    n = int(input("Кількість чисел Фібоначчі: "))
    a, b = 0, 1
    result = []
    count = 0
    while count < n:
        result.append(a)
        a, b = b, a + b
        count += 1
    print(result)

def task_22_permutations():
    """Усі перестановки списку (itertools)"""
    data = [1, 2, 3]
    print(f"Перестановки {data}:")
    print(list(itertools.permutations(data)))

def task_23_accumulate():
    """Накопичувальна сума (itertools)"""
    data = [1, 2, 3, 4, 5]
    print(f"Дані: {data}")
    print(f"Накопичувальна сума: {list(itertools.accumulate(data))}")

def task_24_cartesian_product():
    """Декартовий добуток (вкладені цикли або itertools)"""
    colors = ['Red', 'Blue']
    sizes = ['S', 'M']
    print([ (c, s) for c in colors for s in sizes ])

def task_25_infinite_count():
    """Імітація лічильника (itertools)"""
    print("Перші 5 чисел з нескінченного лічильника:")
    counter = itertools.count(start=10, step=5)
    for _ in range(5):
        print(next(counter), end=" ")
    print()

# --- БЛОК 6: Патерни та малювання ---

def task_26_star_square():
    """Квадрат із зірочок (вкладені цикли)"""
    size = int(input("Розмір: "))
    for i in range(size):
        print("* " * size)

def task_27_triangle_left():
    """Трикутник (лівий)"""
    h = int(input("Висота: "))
    for i in range(1, h + 1):
        print("*" * i)

def task_28_pyramid():
    """Піраміда"""
    h = int(input("Висота: "))
    for i in range(h):
        print(" " * (h - i - 1) + "*" * (2 * i + 1))

def task_29_matrix_transpose():
    """Транспонування матриці"""
    matrix = [[1, 2], [3, 4], [5, 6]]
    print("Матриця:", matrix)
    transposed = [[row[i] for row in matrix] for i in range(2)]
    print("Транспонована:", transposed)

def task_30_number_triangle():
    """Числовий трикутник"""
    n = 5
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# --- БЛОК 7: Реальні задачі та ігри ---

def task_31_guess_number():
    """Гра 'Вгадай число' (while + random)"""
    target = random.randint(1, 10)
    guess = 0
    while guess != target:
        guess = int(input("Вгадайте число (1-10): "))
        if guess < target: print("Більше!")
        elif guess > target: print("Менше!")
    print("Вітаю! Ви вгадали.")

def task_32_currency_converter():
    """Конвертер валют"""
    rate = 41.5  # Приблизний курс USD до UAH
    usd = float(input("Сума в USD: "))
    print(f"Сума в UAH: {usd * rate:.2f}")

def task_33_celsius_to_fahrenheit():
    """Конвертер температур"""
    c = float(input("Градуси Цельсія: "))
    f = (c * 9/5) + 32
    print(f"Фаренгейт: {f:.2f}")

def task_34_password_generator():
    """Генератор паролів"""
    length = int(input("Довжина пароля: "))
    chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$"
    password = "".join(random.choice(chars) for _ in range(length))
    print(f"Пароль: {password}")

def task_35_leap_year():
    """Перевірка високосного року"""
    year = int(input("Рік: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Рік високосний")
    else:
        print("Рік не високосний")

def task_36_simple_calculator():
    """Простий калькулятор (функції)"""
    a = float(input("Число 1: "))
    op = input("Дія (+, -, *, /): ")
    b = float(input("Число 2: "))
    
    if op == '+': print(a + b)
    elif op == '-': print(a - b)
    elif op == '*': print(a * b)
    elif op == '/' and b != 0: print(a / b)
    else: print("Помилка")

def task_37_timer():
    """Простий таймер зворотного відліку"""
    sec = int(input("Секунд до старту: "))
    while sec > 0:
        print(sec)
        sec -= 1
        # time.sleep(1) # Закоментовано для швидкості, розкоментуйте для реального часу
    print("Старт!")

def task_38_bmi_calculator():
    """Індекс маси тіла"""
    w = float(input("Вага (кг): "))
    h = float(input("Зріст (м): "))
    bmi = w / (h ** 2)
    print(f"ІМТ: {bmi:.2f}")

def task_39_digit_sum():
    """Сума цифр числа"""
    num = input("Введіть число: ")
    total = sum(int(digit) for digit in num if digit.isdigit())
    print(f"Сума цифр: {total}")

def task_40_rock_paper_scissors():
    """Камінь, ножиці, папір"""
    choices = ['камінь', 'ножиці', 'папір']
    comp = random.choice(choices)
    user = input("камінь, ножиці чи папір? ").lower()
    print(f"Комп'ютер: {comp}")
    if user == comp: print("Нічия!")
    elif (user == 'камінь' and comp == 'ножиці') or \
         (user == 'ножиці' and comp == 'папір') or \
         (user == 'папір' and comp == 'камінь'):
        print("Ви перемогли!")
    else:
        print("Ви програли!")

# --- ГОЛОВНЕ МЕНЮ ---

def main():
    tasks = [
        task_1_sum_n, task_2_factorial, task_3_even_numbers, task_4_multiplication_table, task_5_check_prime,
        task_6_reverse_string, task_7_count_vowels, task_8_palindrome, task_9_char_frequency, task_10_ascii_codes,
        task_11_max_in_list, task_12_remove_duplicates, task_13_list_sum_average, task_14_positive_negative, task_15_sort_custom,
        task_16_hypotenuse, task_17_circle_area, task_18_degrees_to_radians, task_19_solve_quadratic, task_20_gcd,
        task_21_fibonacci, task_22_permutations, task_23_accumulate, task_24_cartesian_product, task_25_infinite_count,
        task_26_star_square, task_27_triangle_left, task_28_pyramid, task_29_matrix_transpose, task_30_number_triangle,
        task_31_guess_number, task_32_currency_converter, task_33_celsius_to_fahrenheit, task_34_password_generator, task_35_leap_year,
        task_36_simple_calculator, task_37_timer, task_38_bmi_calculator, task_39_digit_sum, task_40_rock_paper_scissors
    ]

    while True:
        print("\n" + "="*40)
        print("МЕНЮ ПРАКТИЧНИХ ЗАВДАНЬ (PYTHON)")
        print("="*40)
        print("Введіть номер завдання (1-40) для запуску.")
        print("Введіть 0 для виходу.")
        
        try:
            choice = int(input("Ваш вибір: "))
            if choice == 0:
                print("Дякую за роботу! До побачення.")
                break
            
            if 1 <= choice <= 40:
                print(f"\n--- Запуск Завдання {choice} ---")
                tasks[choice - 1]() # Виклик відповідної функції
                input("\nНатисніть Enter для повернення в меню...")
            else:
                print("Невірний номер завдання. Спробуйте ще раз.")
        except ValueError:
            print("Будь ласка, введіть число.")

if __name__ == "__main__":
    main()