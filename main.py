
array = []  # текущий массив программы


def main():
    global array
    while True:
        print("\n===== МЕНЮ =====")
        print("1. Ввод размера массива")
        print("2. Создание массива")
        print("3. Просмотр созданного массива")
        print("4. Выполнение функций")
        print("5. Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "1":
            input_size()
        elif choice == "2":
            print("создание массива")
        elif choice == "3":
            print("просмотр массива")
        elif choice == "4":
            print("выполнение функций")
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
            print(f'Массив {rows} x {cols} успешно создан.')
            return rows, cols
        print("Числа должны быть положительными!")


if __name__ == "__main__":
    main()
