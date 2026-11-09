import numpy as np


array = []  # текущий массив программы
rows = None
cols = None


def main():
    global array, rows, cols
    while True:
        print("\n===== МЕНЮ =====")
        print("1. Ввод размера массива")
        print("2. Создание массива")
        print("3. Просмотр созданного массива")
        print("4. Выполнение функций")
        print("5. Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "1":
            rows, cols = input_size()
            print(f"Размер массива: {rows} x {cols}")
        elif choice == "2":
            if rows is None:
                print("Сначала задайте размер массива (пункт 1)")
                continue
            print("1 — ввод вручную, 2 — автоматически, 3 — назад")
            sub = input("Выберите вариант: ").strip()
            if sub == "1":
                array = create_manual(rows, cols)
                print("Массив создан:")
                print(array)
            elif sub == "2":
                array = create_auto(rows, cols)
                print("Массив создан автоматически:")
                print(array)
            elif sub == "3":
                pass
            else:
                print("Нет такого пункта")
        elif choice == "3":
            if array is None:
                print("Массив еще не создан")
            else:
                print(array)
        elif choice == "4":
            functions_menu()
        elif choice == "5":
            print("Программа завершена")
            break
        else:
            print("Нет такого пункта")

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Введите целое число!")


def input_size():
    while True:
        rows = input_int("Количество строк: ")
        cols = input_int("Количество столбцов: ")
        if rows > 0 and cols > 0:
            return rows, cols
        print("Числа должны быть положительными!")

def create_manual(rows, cols):
    arr = np.zeros((rows, cols), dtype=int)
    print("Вводите элементы построчно:")
    for i in range(rows):
        for j in range(cols):
            arr[i, j] = input_int(f"Элемент [{i}][{j}] = ")
    return arr


def create_auto(rows, cols):
    return np.random.randint(0, 101, (rows, cols))

def func_16(arr):
    found = False
    for i in range(arr.shape[0]):
        if np.any(arr[i] == 10):
            print("Элемент 10 есть в строке", i)
            found = True
    if not found:
        print("Строк с элементом, равным 10, нет")

def func_18(arr):
    res = arr.copy()
    res[[0, -1]] = res[[-1, 0]]
    print("Массив после замены строк:")
    print(res)
    return res





def functions_menu():
    global array
    if array is None:
        print("Сначала создайте массив (пункты 1 и 2)")
        return
    while True:
        print("\n--- Выполнение функций ---")
        print("а. Задание 16: номера строк, где есть элемент, равный 10")
        print("б. Задание 18: поменять местами первую и последнюю строки")

        print("г. ")
        print("д. ")
        print("е. Назад")
        choice = input("Выберите пункт: ").strip().lower()
        if choice == "а":
            func_16(array)
        elif choice == "б":
            array = func_18(array)

        elif choice == "е":
            break
        else:
            print("Нет такого пункта")
        if choice != "е":
            input("Нажмите Enter, чтобы продолжить...")


if __name__ == "__main__":
    main()
