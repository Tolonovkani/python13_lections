# Найти квадрат, куб, результат деления на 100 любого числа

# num1 = 5
# ->{'num:' 5, '2': 25, '3': 125, '100': 0.05}

# num1 =5 
# res = {'num': num1, '2': num1**2, '3': num1*3, '100': num1 / 100}
# print(res)


# num2 =75 
# res = {'num': num2, '2': num2**2, '3': num2*3, '100': num2 / 100}
# print(res)

# num3 =1154
# res = {'num':  num3, '2': num3**2, '3': num3*3, '100': num3 / 100}
# print(res)

# # DRY - Don't repeat yourself
# def do_operations(num: int):
#     res = {'num': num, '2': num**2, '3': num*3, '100': num / 100}
#     print(res)

# do_operations(16)
# do_operations(4356)
# do_operations(31)
# do_operations(1298)
# do_operations(567)

# =========================================
# функция - это именнованая часть программыб которая содержить в себе определенный набор инсрукций, может вызываться других частях программы столько раз сколько угодно

# def name_of_func(<a,b>#параметры функции):
    # <body> # кодб какая то логика которая будет давать конечный резулльтат
    # <return> # оператор который помагает сохранить результат

    # name_of_func(5, 6 #аргументы)

# параметры функции - переменые которых мы временна сохраняем данные которые передаем при вызове в функцию,доступны только внутри функции


# аргументы функции - данные которые мы передаем при вызове функции, они попадают в параметры по очередно

# print(len('string'))
# from typing import Iterable


# def our_len(obj: Iterable) -> int:
#     """Возващает длину итерируемого обьекта"""
#     print(obj)
#     i = 0
#     for item in obj:
#         i += 1
#         return f"result: {i}"

# ls = [1,2,3,4,5]
# str1 = 'Helo woorld s vami Jonh Snow!'

# print(our_len(ls))
# print(our_len(str1))
# print(len(str1))


# def isEven(num):
#     return True if num % 2 ==0 else False

# result = isEven(15)
# print(result)


# def isEven(num:  int) -> bool:
#     "Return True or False while after checking nimber for even!"
#     return True if num % 2 == 0 else False

# result = isEven(456)
# print(result)
# ==========================================================

# default параметры
# def sum_of_args(a: int, b: int, c: int=0) -> int:
#     return a + b + c

# print(sum_of_args(5, 6, 7))
# print(sum_of_args(9, 123, ))

# ============================================================
# пазицонные и именовыные аргументы

# def printParams(a, b, c):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')
    

# printParams(5, 10, 15)# пазиционые аргументы
# print()
# printParams(b = 5, a = 10, c = 15) # иименовыный аргументы
# print()
# printParams(5, c = 10, b = 15)
# ==================================================================
# оператор *
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [*a, *b]
# print(c)
# ==========================================
# * args,  **kwargs

# def get_some_data(a, b, *args, **kwargs):
#     print('parametry a  и  b:', a, b)
#     print('аргументы:', args)
#     print('именованные аргументы:', kwargs)


# get_some_data(1, 2, 3, 4, 5)



# def printScores(student: str, *scores):
#     '''prints info about ,student to terminal!'''
#     print(f'Name of student:{student}!')
#     print(f'AVG: {sum(scores) / len(scores), 1}')
#     print(scores, type(scores), '!!!')
#     for x in scores:
#         print('Score:', x)

# printScores('Jonh Snow',5, 5, 5, 4, 4, 2)



# def pritPetNames(owner: str, ** pets):
#     print(f'owner name {owner}!')
#     print(pets, type(pets), '!!!')
#     for pet, name in pets.items():
#         if type (name) == list:
#             print(f'{pet}', *name)
#         else:
#             print(f'{pet}: {name}')
       

# pritPetNames('Jonh Snow',dog='Pluto', cat='Garfild', fish=['Nemo', 'Dori', 'Golden'], turtle='Leonardo')
# ==============================================

# from random import choice, shuffle
# from string import ascii_letters, digits, punctuation

# symbols = ascii_letters + digits

# def generate_password(len_: int = 8) -> str:
#     '''Function generetes random string for passford, parametr len needs to give lenghts of password.if blank len_ = 8'''

#     res = [choice(symbols) for _ in range(len_ - 2)] + [choice(punctuation) for _ in range(2)]
#     shuffle(res)
#     return ''.join(res)

# print(generate_password())
# print(generate_password(12))
# print(generate_password(16))
# print(generate_password(9))
# ========================
# def bold(func):
#     def wrapper(*args, **kwargs):
#         res = '<bold>' + func(*args, **kwargs) + '</bold>'
#         return res
#     return wrapper
# def div(func):
#     def wrapper(*args, **kwargs):
#         res = '<div>' + func(*args, **kwargs) + '</div>'
#         return res
#     return wrapper

# @div
# @bold
# @div

# def get_name():
#     name = input('Vvedote svoe imya:')
#     return name

# res = get_name()
# print(res)
# ==============================================================
# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace: вызвала {func.__name__}()\nона приняла args:{args}, kwargs: {kwargs}')
#         res = func(*args, **kwargs)
#         print(f'Trace: вызвала {func.__name__}()\nона вернула: {res}')
#         return res
#     return wrapper
# @trace
# def say(name,adress):
#     return f'{name} --> {adress}'

# @trace
# def hello(name, last_name, country):
#     return f'hello {name} {last_name} from {country}'
# say('Sherlok Holms', 'Bakery Street 221B')
# print()
# hello(name ='Homer', last_name ='Simpson', country ='Canada')


