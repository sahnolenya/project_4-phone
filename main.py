from dlya_func import clean_phone_numbers, multiply # Импортируем функции

import pandas as pd

input_file = "C:\\Users\\sakhn\\OneDrive\\Рабочий стол\\phone_numbers.xlsx"
output_file = "C:\\Users\\sakhn\\OneDrive\\Рабочий стол\\cleaned_phone_numbers.xlsx"

def main():
    try:
        df = pd.read_excel(input_file)
        phone_numbers = df["phone_number"]  # Предполагается, что столбец называется "phone_number"

        # Вызов функции из dlya_func.py
        cleaned_numbers = clean_phone_numbers(phone_numbers)

        df["Очищенный номер"] = cleaned_numbers
        df.to_excel(output_file, index=False)
        print(f"Данные сохранены в файл: {output_file}")

        # Пример вызова функции multiply (для демонстрации)
        multiply(cleaned_numbers)

    except FileNotFoundError:
        print(f"Файл не найден: {input_file}")
    except KeyError:
        print("Столбец 'phone_number' не найден в файле.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Инициализационный скрипт
if __name__ == "__main__":
    main()

