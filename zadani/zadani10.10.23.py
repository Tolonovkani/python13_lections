# 1) Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
# def my_add(a: int, b: int) -> int:
#     return a + b

# print(my_add(4, 4))
 
# =====================================================================
# 2) Создайте функцию, которая будет принимать строку. Функция должна выводить длину этой строки(не использовать функцию len).

# def findLen(str):
#     counter = 0
#     while str[counter:]:
#         counter += 1
#     return counter

# str = "stroka"
# print(findLen(str))
# =================================================
# 3) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
# def example(first, second=3, third=5):
#     print(type(first))
#     print(type(second))
#     print(type(third))
# example('my string', third=4)
# ===================================================
# 4)Создайте функцию, которая должна принимать 2 числа и возвращать результат их деления.

# def calculations(a, b):
#     div = a / b
#     return div
# num1, num2 = int(input()), int(input())
# div = calculations(num1, num2)
# print(f'Результат деления: {div:.2f}')
# ====================================================
# 5) Создайте функцию, которая принимает словарь. Пройдитесь по словарю циклом и распечатайте все его ключи
# def my_function(**kwargs):
#     print(f'Самый легкий металл - {min(kwargs, key=kwargs.get)} {min(kwargs.values())}, самый тяжелый - {max(kwargs, key=kwargs.get)} {max(kwargs.values())}')
# my_function(осмий=22.61, цинк=7.1, золото=19.3, ртуть=13.6, олово=7.3)
# ===============================================================
# 6) Создайте функцию, которая принимает и выводит "It's odd number" если это число не кратно двум и "It's even number" в противном случае.
# def is_even(number: int) -> str:
#     return "It's even number" if number % 2 == 0 else "It's odd number"

# print(is_even(4))

# =====================================================
# 7) Напишите функцию, которая будет принимать строку и проверять является ли она палиндромом. Пробелы и регистр учитывать не нужно.
# # (Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например, число 101; слова "кок", "топот", "комок" и т.д.)
# def isPalindrome(string):
# #Конвертируем в строку, поскольку пользователь может ввести также и число
#     foo = str(string)
# #  foo[::-1] - это такой трюк переворачивающий строку, очень полезный
# # Идёт проверка, если перевёрнутая строка равна обычной строке, то это палиндром и возвращается значение True
#     if foo[::-1].startswith(foo):
#         return True
# # Иначе же возвращаем False
#     else:
#         return False
# ==================================================
# 8)Создайте функцию которая принимает от пользователя два числа. Она должна сравнить эти числа между собой и вывести максимальное значение.
# a = 5
# b = 4
# def maximer(a, b):
#     if a > b:
#         print('max=' + str(a))
#         return a
#     else:
#         print('max=' + str(b))
#         return b
 
 
# if __name__ == '__main__':
#     assert maximer(a=1, b=2)
# =================================================
# 9) Напишите функцию, которая принимает список чисел и возвращает их произведение.
# def masind(mas, i):
#     prod = 1
#     for j in mas[:i]:
#         prod *= j
#     return prod
 
# a = int(input())
# b = int(input())
# c = int(input())
 
# mas = [i for i in range(a, b, c)]
 
# i = int(input())
# z = masind(mas, i)
# print(z)
# ============================================================
# 10) Напишите функцию, которая принимает целое число и возвращает сумму всех его цифр. Например, число 123 --> 6
# n = int(input())
 
# suma = 123
# mult = 6
 
# while n > 0