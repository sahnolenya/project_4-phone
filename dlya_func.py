def _to_tuple(l):
    """Преобразует список в кортеж."""
    return tuple(l)


def multiply(n):
    """Записывает в файл удвоенный кортеж чисел."""
    try:
        with open("file_name.txt", "w") as f:
            f.write(str(_to_tuple(n) * 2))  # Удвоение кортежа
    except Exception as e:
        print(f"Ошибка записи в файл: {e}")


def clean_phone_numbers(numbers):
    """Очищает номера телефонов от нецифровых символов."""
    cleaned_numbers = []
    for number in numbers:
        cleaned_number = ''.join(filter(str.isdigit, str(number)))
        cleaned_numbers.append(cleaned_number)
    return cleaned_numbers

