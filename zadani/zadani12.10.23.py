# 1) '''Напишите декоратор, который проверяет, что функция вызывается с определенными типами аргументов.'''

# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         return f'Большие {original_result.upper()}'
#     return wrapper


# @uppercase
# def greet():
#     return 'маленькие буквы'


# print(greet())

# 2) '''Создайте декоратор, который автоматически преобразует результат функции в другой тип данных,'''
# def decrator(func):
#     def wrapper():
#         print('decarotor worked!')
#         try:
#             if isinstance(func(), list):
#                 return tuple(func())
#             elif isinstance(func(), tuple):
#                 return set(func())
#             elif isinstance(func(), set):
#                 return str(func())
#             elif isinstance(func(), float):
#                 return int(func())
#             elif isinstance(func(), int):
#                 return str(func())
#             elif isinstance(func(), str):
#                 return list(func())
#         except TypeError:
#             print('неправильный тип данных!')
#     return wrapper
              

# @decrator
# def a():
#     return 1

# print(a())


# 3) '''Реализуйте декоратор, который ограничивает максимальное количество вызовов функции.'''

from functools import wraps

def countcall(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f'{func.__name__} has been called {wrapper.count} times')
        return result
    wrapper.count = 0
    return wrapper

@countcall
def process_data():
    pass 

process_data()
process_data has been called 1 times
process_data()
process_data has been called 2 times
process_data()
process_data has been called 3 times

# 4) '''Напишите декоратор, который автоматически логирует исключения, возникающие внутри функции.'''

# #

# 5) '''Создайте декоратор, который выполняет аутентификацию пользователя перед вызовом функции.'''


# 6) '''Реализуйте декоратор, который изменяет значение возвращаемого результата функции, например, умножая его на определенный коэффициент.'''

# #

# 7) '''Напишите декоратор, который ограничивает доступ к функции только определенным пользователям или ролям.'''
# import datetime 

# def dec(func):
#     def wrapper(*args, **kwargs):
#         if datetime.datetime.now().hour > 10 and datetime.datetime.now().hour < 15:
#             func()
#             print(datetime.datetime.now().hour)
#     return wrapper
    
# @dec
# def func():
#     print('работаеть')

# func()

# 8) '''Создайте декоратор, который преобразует аргументы функции в определенный формат перед её выполнением, например, в строку в верхнем регистре.'''

# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         return f'aaaa {original_result.upper()}'
#     return wrapper


# @uppercase
# def greet():
#     return 'aaaa'


# print(greet())

# 9) '''Напишите декоратор, который устанавливает максимальное время выполнения функции и завершает её, если оно превышено.'''

# import time

# def time_of_function(function):
#     def wrapped(*args):
#         start_time = time.perf_counter_ns()
#         res = function(*args)
#         print(time.perf_counter_ns() - start_time)
#         return res
#     return wrapped

# @time_of_function
# def func(first, second):
#     return bin(int(first, 2) + int(second, 2))


# print(func("111", "0000"))


# 10) '''Напишите декоратор, который ограничивает доступ к функции только в определенное время суток.'''
# def retry(func):
#     def _wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except:
#             time.sleep(1)
#             func(*args, **kwargs)
#     return _wrapper

# @retry
# def might_fail():
#     print("might_fail")
#     raise Exception

# might_fail()