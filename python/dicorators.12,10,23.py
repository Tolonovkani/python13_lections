# # декораторы это функция которая позволяет без изменения кода расширать ее функсанал.

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'{func.__name__} была вызвана!')
#         func(*args, **kwargs)
#     return wrapper

# @decorator
# def printPetNames(owner: str, **pets):
#     print(f'Owner name {owner}!')
#     print(pets, type(pets), '!!!')
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')


# printPetNames('Kanybek', cow='murka', cat='tom', mouse='jerry', dog='aktosh')

# pythonic way -@

# def decorator(func):
#     def wrapper():
#         print('decorator worked!')
#         print(f'{func._name_} была вызвана!')
#         func()
#     return wrapper

# @decorator
# def get_name():
#     print(f'Owner name Jonh Snow!')

# get_name()
# ==================================
# import time

# def benchmark(funk):
#     def wrapper(*arg, **kwargs):
#         start = time.time()
#         funk(*arg, **kwargs)
#         finish  = time.time()
#         print(f'времия выполнение функции: {funk.__name__}, заняло: {finish - start}')
#     return wrapper
    
# @benchmark
# def loop():
#     i = 0 
#     num = 100_000_000
#     ls = []
#     while i < num:
#         ls.append(i)
#         i += 1

# # loop()

# @benchmark
# def add(number):
#     i = 0
#     ls = []
#     while i <= number:
#         ls.append(i)
#         i += 1

# loop()
# add(100_000_000)



