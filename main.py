
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
            print("ввод размера")
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


if __name__ == "__main__":
    main()
