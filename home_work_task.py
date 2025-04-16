# Задача 1: Проверка палиндрома
# Напишите функцию, которая проверяет, является ли строка палиндромом (читается одинаково в обоих направлениях).

text=input('Введите текст: ')

if text==text[::-1]:
    print(f'Текст "{text}" является палиндромом')
else:
    print('Не палиндром')


# Задача 2: Подсчет элементов в списке
# Напишите функцию, которая принимает список чисел и возвращает словарь, где ключи - это числа из списка, а значения - количество их повторений.

def count_occurrences(numbers):
    result = {}
    for num in numbers:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result

# Пример использования
nums = [1, 1, 4, 5, 2, 3, 4]
counts = count_occurrences(nums)
print("Словарь с подсчётом повторений:", counts)

# Задача 3: Поиск максимального и минимального элемента в списке
# Напишите функцию, которая принимает список чисел и возвращает кортеж из максимального и минимального элемента.

def find_max_min_num(numders):
    if not numders:
        return None
    else:
        return (max(numders), min(numders))

num=[7, 88, 1, 0, 5, -1]

result=find_max_min_num(num)
print(result)