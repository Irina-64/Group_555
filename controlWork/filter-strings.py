def filter_strings(array):
    result = []
    for string in array:
        if len(string) <= 3:
            result.append(string)
    return result

# Ввод массива с клавиатуры
array = input("Введите элементы массива через пробел: ").split()

# Фильтрация массива
filtered_array = filter_strings(array)

# Вывод отфильтрованного массива
print("Отфильтрованный массив:", filtered_array)
