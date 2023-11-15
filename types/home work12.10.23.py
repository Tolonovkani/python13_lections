
# 1) Напишите функцию, которая принимает строку и вычисляет количество букв верхнего и нижнего регистра.
# s = 'The quick Brow Fox' 
# lower_ = list(filter(lambda x: x.islower(),list(s))) 
# upper_ = list(filter(lambda x: x.isupper(),list(s))) 
# print('Количество символов в верхнем регистре:', len(upper_)) 
# print('Количество символов в нижнем регистре:', len(lower_))
# =============================================================
# 2) Напишите функцию, которая принимает число n и генерирует словарь, чьи ключи состоят из чисел от 1 до n, а их значения -- куб ключей. Пример: передано число 5. В результате должны получить словарь {1: 1, 2: 8, 3: 27, 4: 64}
# def func():
#     n = int(input())
#     dict_ = {i: i ** 3 for i in range(1, n + 1)}
#     return dict_
# print(func())
# ==============================================
# 3) Напишите функцию sum_range(start, end), которая суммирует все целые числа
#     от значения «start» до величины «end» включительно. Если пользователь задаст
#     первое число большее чем второе, просто поменяйте их местами.
# def sum_range(start, end):
#     if start > end:
#         start, end = end, start
#     s = 0
#     for i in range (start, end+1):
#         s += i
#     return s
    
# a, b = map(int, input().split())
# print(sum_range(a, b))
#================================================ 
# 4) Напишите функцию, которая принимает слово и возвращает True, если слово изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False
# def Election(x, y, z):
#     if x + y + z >= 2:
#         return 1
#     elif x + y + z < 2:
#         return 0
# x = int(input())
# y = int(input())
# z = int(input())
# print(Election(x, y, z))
# 5) Напишите функцию, которая проверяет, сколько раз каждое слово в переданной фразе было использовано. Например: “Money, money, money, it’s always sunny, in the richmen’s world
# ”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1, world: 1.

# def count_words():
#     t = input('Vvedite text').lower().split()
#     spis = []
#     for i in t:
#         spis.append(i)
#         if i in t:
#             continue
#     dict_ = {u: spis.count(u) for u in spis}
#     print(dict_)

# count_words()


