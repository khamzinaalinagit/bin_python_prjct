from funcs import (
    is_binary_string,
    find_binaries_in_text,
    find_binaries_in_file,
    find_binaries_in_url,
)


def mode_check_input():

    s = input("Введите строку: ")
    if is_binary_string(s):
        print("Строка является двоичным числом.")
    else:
        print("Строка НЕ является двоичным числом.")


def mode_search_in_text():

    text = input("Введите произвольный текст: ")
    binaries = find_binaries_in_text(text)
    if binaries:
        print("Найдены двоичные числа:")
        for b in binaries:
            print(b)
    else:
        print("Двоичных чисел не найдено.")


def mode_search_in_file():

    path = input("Введите путь к текстовому файлу: ")
    try:
        binaries = find_binaries_in_file(path)
    except FileNotFoundError:
        print("Файл не найден.")
        return
    except OSError as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    if binaries:
        print(f"Найдено {len(binaries)} двоичных чисел:")
        for b in binaries:
            print(b)
    else:
        print("В файле двоичных чисел не найдено.")


def mode_search_in_url():
    url = input("Введите URL (например, https://example.com): ")
    try:
        binaries = find_binaries_in_url(url)
    except Exception as e:
        print(f"Ошибка при обращении к URL: {e}")
        return

    if binaries:
        print(f"Найдено {len(binaries)} двоичных чисел на странице:")
        for b in binaries:
            print(b)
    else:
        print("На странице двоичных чисел не найдено.")


def main():
    while True:
        print("\n=== Поиск чисел в двоичной системе счисления ===")
        print("1 — Проверить, является ли строка двоичным числом")
        print("2 — Найти двоичные числа во введённом тексте")
        print("3 — Найти двоичные числа в файле")
        print("4 — Найти двоичные числа на веб-странице по URL")
        print("0 — Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            mode_check_input()
        elif choice == "2":
            mode_search_in_text()
        elif choice == "3":
            mode_search_in_file()
        elif choice == "4":
            mode_search_in_url()
        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Некорректный выбор. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
