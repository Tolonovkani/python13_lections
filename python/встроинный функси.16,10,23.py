# zip(iterables)- она соединяет каждый элемент итерируемых объектов между собой в тип данных tuple и возвращает итератор

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]
# res = list(zip(ls1, ls2))
# print(res)
# =============================================

# all(Iterable) -  Возвпащает True, если все элементы интерируемого объекта истина, иначе False

# ls = [[1, 2], 5, 'stroka', True, 1, '']
# print(all(ls))
# ================================================

# ip = '10.255.12.155' # true
# ip2 = '10.255.1y.155' # false

# result = all(x.isdigit() for x in ip.split('.'))
# print(result)

# result = all(x.isdigit() for x in ip2.split('.'))
# print(result)
# ====================================================
# any - Возвращает True, если хотябы один элемент истинна

# ls = [0, 0, 0, 0, '1']
# print(any(ls))
# ====================================================
# ignore = ('rm-rf', 'sudo', 'reset', 'poweroff')

# command = input('Vvedite comandu:')
# if any(x in command for x in ignore):
#     raise Exception('You do not have permissions!')

# print('OK!')
# ====================================================
# Анонимные функции - lambda(такие же функци только без названия)

# lambda функции могуть принимать сколько угодно аргументов, но всегда возвращает ондо выражение

# def sum_of_args(a, b):
#     res = a + b
#     return res

# print(sum_of_args(5, 15))
 
# func = lambda a, b: a + b
# print(func(5, 15))
# =================================================
# def myFunc(n):
#     return lambda a: a * n

# myDoubler = myFunc(2)
# myTripler = myFunc(3)
# print(myDoubler(50))
# print(myDoubler(123))
# print(myDoubler(7))
# print(myTripler(55))
# print(myTripler(100))
# ========================================================
# dict_ = {'Jonh': 50_000_000, 'Jamie': 100_000, 'Aibek': 1_000_000, 'Aigerim': 15}

# res = sorted(dict_.items(), key=lambda x: x[1])
# print(res)
# =============================================================
# map(function, iterable) -> применяет ко всем элементам iterable функцию которую мы передаем
# 1v
# ls = ['one', 'two', 'three', 'four', 'five']
# res = list(map(str.upper, ls))
# print(res)
# ==========================
#2v
#  for i in range(len(ls)):
#     ls[i] = ls[i].upper()
# print(ls)
# ======================================
# 1v
# names = ['Jonh', 'Sultan', 'Jamie', 'Reychel', 'Aibek']
# res = list(map(
#     lambda name: f'hello mr/mrs {name}!',
#     names))
# print(res)
# 2v
#  def func(name):
#     return f'Hello mr/mrs {name}!'
# res = list(map(func,names))
# print(res)
#3v
#  res = []
# for name in names:
#     res.append(func(name))
# print(names)
# print(res)
# =======================================
# dict_ = {1: 2, 3: 4, 5: 6}

# res = dict(map(
#     lambda x: (x[0], str(x[1])),
#     dict_.items()))
# print(res)
# ===========================================
#  TODO filter, reduce, enumarate,rapeat


# filter(function,iterable) - > приенят ко всем элементам iterable функцию который мы передали и возвпащает итератор с теми элементамидля которых функция вернула True

# ls = ['one', 'two', '', 'list', '100','1', 'jonh']

# 1v
# res = []
# for x in ls:
#     if x.isdigit():
#         res.append(x)

# print(res)
# 2v
# res = list(filter(str.isdigit, ls))
# print(res)

# ==============================================

# ls = ['jonh', 'codify', 'Aibek ', 'ono', 'bootcamp']
# res = list(filter(lambda x : len(x) > 5, ls))
# print(res)

# ==================================

# ls = [
#     {'name': 'Python', 'point': 10},
#     {'name': 'C++', 'point': 6},
#     {'name': 'JS', 'point': 8},
#     {'name': 'JAVA', 'point': 3},
#     {'name': 'C#', 'point': 0},
# ]
# res = list(filter(lambda dict_: dict_['point'] > 7, ls))
# print(res)
# /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=

# users = [
#     {'username ': 'Jonh', 'coments': ['i love you', 'Really good']}
#     {'username ': 'Reychel', 'coments': []}
#     {'username ': 'Steven', 'coments': ['Bishkek', 'Python']}
#     {'username ': 'Kira', 'coments': []}
#   ]
# res1 = list(filter(lambda a :  a ['coments'], users))
# res2 = list(filter(lambda a : not a ['coments'], users))
# print(res1)
# print()
# print(res2)
# =/=/=/==//=//==/=/=/=/=/=//===/==//==/=/=/
# names = ['Reichel', 'jonh', 'Sultan', 'Aigerim', 'Kira']
# a = list(map(lambda x: f' Hello Mr/mrs {x}', filter( lambda x : len(x) > 5, names)))
# print(a)
# =/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=

# FILTER
# a = ['Jon','Stew','Aiba','Akyl','Beka']
# b = list(filter(lambda x:x.startswith('A'), a))
# print(b)
# =========================
# list1 = [5, 5, 6, 6]
# list2 = list(filter(lambda x: x == 5, list1))
# print(list2)
# ============================
# Вычесление четные числа
# print(list(filter(lambda x: x % 2 == 0,[1, 2, 3, 4, 5, 6])))
# нечотные числа
# print(list(filter(lambda x: x % 2 != 0,[1, 2, 3, 4, 5, 6, 7, 8, 9])))
# ======================================

# dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
# dict_new = list(filter(lambda x: x['name'] == 'java', dict_a))
# print(dict_new)
# =========================================

# enumerate
# enumerate- она пронумеровывает каждый элемент внутри iterable, ее собственным индексом
# ls = ['one', 'two', 'Three', 'four', 'five'] 
# res = list(enumerate(ls, 1))
# print(res)
# ================================
# ls = ['one', 'two', 'Three', 'four', 'five']
# for i, x in enumerate(ls):
#     print(f'Index: {i}, Element: {x}!')
# -------------------------------------------
# reduce

# reduce- Функция Reduce () принимает функцию и последовательность и возвращает одно значение, рассчитанное следующим образом:
# 1. Первоначально функция вызывается с первыми двумя элементами из последовательности, и результат возвращается.
# 2. Затем функция вызывается снова с результатом, полученным на шаге 1, и следующим значением в последовательности. Этот процесс повторяется до тех пор, пока в последовательности не появятся элементы.
# from functools import reduce

# ls = [1, 2, 3, 4, 5]
# res = reduce(lambda a, b: a + b, ls)
# les = reduce(lambda a, b: a * b, ls)
# print(res,les)
# =========================
# repeat
# from itertools import repeat

# for x in repeat(lambda x: x * 5, 5):
#     print(x,)
# =================================
from itertools import repeat
from random import choices
from string import ascii_letters, digits
from statistics import mean

symbols = '_()$!%+-@#'
q_pass = int(input('Vvedite kolichestva poroley: '))


result = {
    f(choices(ascii_letters, k=10), 
      choices(digits,k=5),
      choices(symbols, k=2))
    for f in repeat(lambda a,d,s:''.join(set(a+d+s)) , q_pass)
    } 

print(result)
print(f'Quantity of passfords: {len(result)}')
dlina = [len(x) for x in result]
print(f'Avarege len: {mean(dlina)}')