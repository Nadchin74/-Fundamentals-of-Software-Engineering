import random
import time
import os
import sys

# --- БЛОК 1: Основи (Try-Except) ---

def task_1_zero_division():
    """Базове перехоплення ZeroDivisionError"""
    print("Спроба поділити 10 на 0...")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("--> Спіймано помилку: Ділення на нуль неможливе!")

def task_2_value_error():
    """Перехоплення ValueError (некоректне перетворення)"""
    print("Спроба перетворити 'abc' на число...")
    try:
        num = int("abc")
    except ValueError as e:
        print(f"--> Помилка значення: {e}")

def task_3_index_error():
    """Вихід за межі списку IndexError"""
    lst = [1, 2, 3]
    print(f"Список має 3 елементи. Звертаємось до 10-го...")
    try:
        print(lst[10])
    except IndexError:
        print("--> Помилка: Такого індексу не існує.")

def task_4_key_error():
    """Відсутність ключа в словнику KeyError"""
    d = {"user": "admin"}
    print("Шукаємо ключ 'password'...")
    try:
        print(d["password"])
    except KeyError:
        print("--> Помилка: Ключ не знайдено.")

def task_5_type_error():
    """Операції з несумісними типами TypeError"""
    print("Додаємо число 5 до рядка '5'...")
    try:
        res = "5" + 5
    except TypeError as e:
        print(f"--> Помилка типу: {e}")

def task_6_generic_exception():
    """Перехоплення будь-якої помилки (Exception)"""
    try:
        x = 1 / 0
    except Exception as e:
        print(f"--> Спіймано загальний клас помилки: {type(e).__name__}")

def task_7_multiple_excepts():
    """Кілька блоків except для різних ситуацій"""
    try:
        # Змініть знаменник на 0, щоб перевірити іншу гілку
        val = int("abc") 
        res = 10 / 1
    except ZeroDivisionError:
        print("--> Ділення на нуль")
    except ValueError:
        print("--> Спіймали ValueError (це не число)")

def task_8_grouped_except():
    """Групування помилок в один рядок"""
    try:
        d = {}
        print(d["missing"])
    except (KeyError, IndexError) as e:
        print(f"--> Помилка доступу до даних: {e}")

def task_9_variable_scope():
    """Змінна помилки 'e' існує тільки в блоці except"""
    try:
        1/0
    except ZeroDivisionError as e:
        print(f"--> Всередині блоку: {e}")
    # print(e) -> Це викликало б помилку, бо e вже видалено

def task_10_pass_error():
    """Ігнорування помилки (pass)"""
    print("Ігноруємо помилку конвертації...")
    try:
        int("garbage")
    except ValueError:
        pass 
    print("--> Програма продовжила роботу без зупинки.")

# --- БЛОК 2: Else та Finally ---

def task_11_else_block():
    """Блок else виконується, якщо помилок НЕ було"""
    try:
        res = 10 / 2
    except ZeroDivisionError:
        print("Помилка")
    else:
        print(f"--> Успіх! Блок else спрацював. Результат: {res}")

def task_12_else_fail():
    """Else не спрацює, якщо була помилка"""
    try:
        res = 10 / 0
    except ZeroDivisionError:
        print("--> Спіймали помилку (блок else пропущено)")
    else:
        print("Це не надрукується")

def task_13_finally_basic():
    """Блок finally виконується ЗАВЖДИ"""
    try:
        print("Спроба ділення на нуль...")
        1 / 0
    except ZeroDivisionError:
        print("--> Обробка помилки")
    finally:
        print("--> FINALLY: Цей текст виводиться у будь-якому випадку.")

def task_14_file_finally():
    """Закриття файлу в finally (безпека ресурсів)"""
    f = None
    try:
        f = open("ghost_file.txt", "r")
    except FileNotFoundError:
        print("--> Файл не знайдено.")
    finally:
        if f:
            f.close()
            print("Файл закрито.")
        else:
            print("--> FINALLY: Файл навіть не відкрився, очистка не потрібна.")

def task_15_return_finally():
    """Finally спрацьовує навіть при return з функції"""
    def demo():
        try:
            return "Результат функції"
        finally:
            print("--> FINALLY: Спрацював ПЕРЕД виходом з функції!")
    print(f"Виклик: {demo()}")

# --- БЛОК 3: Генерація виключень (raise) ---

def task_16_raise_basic():
    """Штучний виклик помилки raise"""
    try:
        raise ValueError("Це моя спеціальна помилка")
    except ValueError as e:
        print(f"--> Перехоплено: {e}")

def task_17_validate_age():
    """Валідація даних через raise"""
    age = -5
    print(f"Перевіряємо вік: {age}")
    try:
        if age < 0:
            raise ValueError("Вік не може бути від'ємним!")
    except ValueError as e:
        print(f"--> Валідація не пройшла: {e}")

def task_18_assert():
    """Використання assert для налагодження"""
    x = 10
    print(f"X = {x}. Очікуємо > 20.")
    try:
        assert x > 20, "X має бути більше 20"
    except AssertionError as e:
        print(f"--> Assert спрацював: {e}")

def task_19_raise_from():
    """Ланцюжок виключень (raise ... from)"""
    try:
        try:
            val = int("not_number")
        except ValueError as e:
            # Ми перепаковуємо помилку в інший тип
            raise RuntimeError("Критична помилка обчислень") from e
    except RuntimeError as e:
        print(f"--> Спіймано нову помилку: {e}")
        print(f"--> Причина (cause): {e.__cause__}")

def task_20_re_raise():
    """Прокидання помилки далі (raise без аргументів)"""
    print("Ловимо помилку, пишемо лог і кидаємо її далі...")
    try:
        try:
            1/0
        except ZeroDivisionError:
            print("   (Лог: сталася помилка, кидаю вище)")
            raise # Кидає ту ж саму помилку далі
    except ZeroDivisionError:
        print("--> Спіймали на рівень вище!")

# --- БЛОК 4: Власні виключення (Custom Exceptions) ---

class MyCustomError(Exception):
    """Базовий клас власної помилки"""
    pass

class NegativeAmountError(MyCustomError):
    """Специфічна помилка для фінансів"""
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Сума не може бути від'ємною: {amount}")

def task_21_custom_exception():
    """Використання власного класу помилки"""
    try:
        raise MyCustomError("Щось пішло не так у моїй логіці")
    except MyCustomError as e:
        print(f"--> Спіймано MyCustomError: {e}")

def task_22_bank_simulation():
    """Симуляція банку з власною помилкою"""
    balance = 100
    withdraw = 150
    print(f"Баланс: {balance}, Спроба зняти: {withdraw}")
    try:
        if withdraw > balance:
            raise MyCustomError("Недостатньо коштів на рахунку")
    except MyCustomError as e:
        print(f"--> Банк відмовив: {e}")

def task_23_inheritance_error():
    """Спадкування помилок"""
    try:
        raise NegativeAmountError(-500)
    except MyCustomError as e: # Ловимо батьківський клас
        print(f"--> Спіймано через батьківський клас (поліморфізм): {e}")

def task_24_args_in_error():
    """Доступ до аргументів помилки"""
    try:
        raise ValueError("Code 404", "Not Found")
    except ValueError as e:
        print(f"--> Аргументи помилки (.args): {e.args}")

def task_25_str_magic_method():
    """Перевизначення __str__ у помилці"""
    class DetailedError(Exception):
        def __str__(self):
            return ">>> !!! УВАГА: КРИТИЧНА ПОМИЛКА !!! <<<"
    try:
        raise DetailedError()
    except DetailedError as e:
        print(e)

# --- БЛОК 5: Робота з файлами та системою ---

def task_26_file_not_found_safe():
    """Безпечне читання файлу"""
    filename = "config_missing.ini"
    try:
        with open(filename, "r") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"--> Файл '{filename}' не знайдено. Використовуємо дефолтні налаштування.")

def task_27_permission_error_sim():
    """Симуляція помилки доступу"""
    # Спроба відкрити поточну директорію як файл викликає PermissionError
    try:
        with open(".", "r") as f: 
            pass
    except (PermissionError, IsADirectoryError) as e:
        print(f"--> Помилка доступу до файлової системи: {e}")

def task_28_import_error():
    """Обробка відсутнього модуля"""
    print("Спроба імпортувати неіснуючий модуль...")
    try:
        import non_existent_module 
    except ImportError:
        print("--> Модуль не знайдено. Програма перейшла в автономний режим.")

def task_29_attribute_error():
    """Звернення до неіснуючого атрибуту/методу"""
    x = 10
    try:
        x.append(5) # У int немає методу append
    except AttributeError as e:
        print(f"--> Помилка атрибуту: {e}")

def task_30_safe_write():
    """Безпечний запис з очищенням"""
    filename = "temp_lab18_test.txt"
    try:
        f = open(filename, "w")
        f.write("Test data")
    except OSError:
        print("Помилка запису")
    finally:
        f.close()
        print(f"--> Файл {filename} записано і закрито.")
        if os.path.exists(filename):
            os.remove(filename) # Прибираємо за собою
            print("--> Тестовий файл видалено.")

# --- БЛОК 6: Реальні сценарії та логіка ---

def task_31_input_validation_loop():
    """Цикл, що вимагає правильного вводу"""
    print("Симуляція вводу числа користувачем...")
    fake_inputs = ["слово", "два", "123"] # Емулюємо ввід
    
    for val in fake_inputs:
        print(f"Користувач ввів: '{val}'")
        try:
            num = int(val)
            print(f"--> Успіх! Прийнято число: {num}")
            break
        except ValueError:
            print("--> Це не число. Спробуйте ще раз.")

def task_32_safe_dict_lookup():
    """Безпечне отримання налаштувань"""
    config = {"host": "localhost", "port": 8080}
    
    # Спосіб 1: .get()
    timeout = config.get("timeout", 30) # Дефолтне 30
    
    # Спосіб 2: try-except
    try:
        db_name = config["db_name"]
    except KeyError:
        db_name = "default_db"
        print(f"--> Налаштування 'db_name' відсутнє. Встановлено: {db_name}")

def task_33_retry_logic():
    """Логіка повторних спроб (Retry Pattern)"""
    print("Спроба з'єднання з сервером...")
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        try:
            attempts += 1
            if random.random() < 0.7: # 70% шанс збою
                raise ConnectionError("Connection refused")
            print("--> З'єднання встановлено успішно!")
            break
        except ConnectionError as e:
            print(f"   Спроба {attempts} невдала: {e}")
            time.sleep(0.1)
    else:
        print("--> Не вдалося підключитися після всіх спроб.")

def task_34_json_parse():
    """Обробка помилок JSON"""
    import json
    bad_json = "{'name': 'Ivan'}" # JSON вимагає подвійні лапки, це викличе помилку
    try:
        data = json.loads(bad_json)
    except json.JSONDecodeError as e:
        print(f"--> Некоректний формат JSON: {e}")

def task_35_recursion_limit():
    """Обробка переповнення стеку"""
    def infinite_recursion(n):
        return infinite_recursion(n+1)
    
    print("Запускаємо нескінченну рекурсію...")
    try:
        # sys.setrecursionlimit(1000) # Можна зменшити ліміт для тесту
        # infinite_recursion(0)
        raise RecursionError("maximum recursion depth exceeded") # Емуляція для швидкості
    except RecursionError:
        print("--> Спіймано RecursionError: Глибина стеку перевищена.")

def task_36_keyboard_interrupt():
    """Обробка Ctrl+C (KeyboardInterrupt)"""
    print("Емуляція натискання Ctrl+C...")
    try:
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        print("--> Програму зупинено користувачем.")

def task_37_database_transaction_mock():
    """Імітація транзакції БД (Commit/Rollback)"""
    print("--- Початок транзакції ---")
    try:
        print("1. Знімаємо гроші...")
        print("2. Зараховуємо гроші...")
        if random.choice([True, False]):
            raise ConnectionError("Втрата зв'язку з БД!")
        print("--> COMMIT: Транзакція успішна.")
    except Exception as e:
        print(f"--> ПОМИЛКА: {e}")
        print("--> ROLLBACK: Відкат змін, повернення грошей.")

def task_38_api_request_mock():
    """Обробка HTTP кодів помилок"""
    codes = [200, 404, 500]
    status = random.choice(codes)
    print(f"Запит до API... Отримано статус {status}")
    try:
        if status == 404: raise ValueError("Resource Not Found")
        if status == 500: raise RuntimeError("Server Internal Error")
        print("--> Дані успішно отримано.")
    except (ValueError, RuntimeError) as e:
        print(f"--> API Error Handler: {e}")

def task_39_list_avg_safe():
    """Безпечне обчислення середнього"""
    lst = []
    try:
        avg = sum(lst) / len(lst)
    except ZeroDivisionError:
        print("--> Список порожній, середнє значення = 0")
        avg = 0

def task_40_warning_handling():
    """Робота з попередженнями (Warnings)"""
    import warnings
    print("Генеруємо попередження...")
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        warnings.warn("Ця функція застаріла", DeprecationWarning)
        if w:
            print(f"--> Спіймано попередження: {w[-1].message}")

# --- ГОЛОВНЕ МЕНЮ ---

def main():
    tasks = [
        task_1_zero_division, task_2_value_error, task_3_index_error, task_4_key_error, task_5_type_error,
        task_6_generic_exception, task_7_multiple_excepts, task_8_grouped_except, task_9_variable_scope, task_10_pass_error,
        task_11_else_block, task_12_else_fail, task_13_finally_basic, task_14_file_finally, task_15_return_finally,
        task_16_raise_basic, task_17_validate_age, task_18_assert, task_19_raise_from, task_20_re_raise,
        task_21_custom_exception, task_22_bank_simulation, task_23_inheritance_error, task_24_args_in_error, task_25_str_magic_method,
        task_26_file_not_found_safe, task_27_permission_error_sim, task_28_import_error, task_29_attribute_error, task_30_safe_write,
        task_31_input_validation_loop, task_32_safe_dict_lookup, task_33_retry_logic, task_34_json_parse, task_35_recursion_limit,
        task_36_keyboard_interrupt, task_37_database_transaction_mock, task_38_api_request_mock, task_39_list_avg_safe, task_40_warning_handling
    ]

    while True:
        print("\n" + "="*50)
        print("ЛАБОРАТОРНА №18: ОБРОБКА ВИКЛЮЧЕНЬ")
        print("="*50)
        print("1-10:  Базові типи (ZeroDivision, Value, Index...)")
        print("11-15: Блоки Else та Finally")
        print("16-20: Генерація (Raise, Assert)")
        print("21-25: Власні класи виключень (Custom)")
        print("26-30: Системні помилки (Файли, Імпорт)")
        print("31-40: Реальні сценарії (Retry, API, DB)")
        print("-" * 50)
        
        try:
            choice = int(input("Введіть номер завдання (1-40) або 0 для виходу: "))
            if choice == 0:
                print("Роботу завершено.")
                break
            
            if 1 <= choice <= 40:
                print(f"\n--- ЗАВДАННЯ {choice} ---")
                tasks[choice - 1]()
                input("\nНатисніть Enter...")
            else:
                print("Невірний номер. Спробуйте 1-40.")
        except ValueError:
            print("Будь ласка, введіть число.")
        except Exception as e:
            print(f"Критична помилка в меню: {e}")

if __name__ == "__main__":
    main()