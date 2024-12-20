import pandas as pd

input_file = "C:\\Users\\sakhn\\OneDrive\\Рабочий стол\\phone_numbers.xlsx"

output_file = "C:\\Users\\sakhn\\OneDrive\\Рабочий стол\\cleaned_phone_numbers.xlsx"

try:
  
    df = pd.read_excel(input_file)

    
    phone_numbers = df["phone_number"]

    cleaned_numbers = []
    for number in phone_numbers:
        
        number_str = str(number)
        cleaned_number = ""
        
        for char in number_str:
            if char.isdigit():
                cleaned_number += char
        cleaned_numbers.append(cleaned_number)

    
    df["Очищенный номер"] = cleaned_numbers

    
    df.to_excel(output_file, index=False)
    print(f"Данные сохранены в файл: {output_file}")


except FileNotFoundError:
    print(f"Файл не найден: {input_file}")
except KeyError:
    print("Столбец 'Телефон' не найден в файле.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
