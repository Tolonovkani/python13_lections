# 1) Умножение соответствующих элементов двух списков: Используйте map и lambda, чтобы умножить соответствующие элементы двух списков.

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]

# res = list(map(lambda x, s: x * s, a,b  ))
# print(res)

# 2) Проверка, что в строке есть хотя бы одна гласная буква: Используйте any и lambda, чтобы проверить, что в строке есть хотя бы одна гласная буква.
# a = ['i love New York']
# print(list(map(lambda x: any(i in 'aeiouy'for i in x), a)))

# 3) Фильтрация слов с определенной длиной: Используйте filter и lambda для фильтрации слов в списке строк, имеющих заданную длину.

# fil = ['aaa','wwww', 'qqqqqq','kkkkkkkk']
# res = list(filter(lambda x: len(x) > 5, fil))
# print(res)

# 4) Проверка, что все элементы списка больше нуля: Используйте all и map, чтобы проверить, что все элементы в списке больше нуля.

# a = [1, 2, 3, 4, 0]
# res = list(map(lambda x: all(a) > 0, a))
# print(res)

# 5) Сумма квадратов четных чисел: Напишите программу, которая с использованием map и reduce находит сумму квадратов четных чисел в списке.
# from functools import reduce

# rom = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# res = reduce(lambda a,b:a + b,map(lambda x:x ** 2, filter(lambda x:x % 2 == 0, rom)))
# print(res)

