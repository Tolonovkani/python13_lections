

# 1) Создайте функцию, которая генерирует рандомное (случайно сгенерированное) число и выводит на окно терминала через команду print(). Далее создайте декоратор, который журналирует это событие. То есть функция декоратор должна писать в dict() предложение: «Функция …………… была запущена успешно», а ключом будет уникальный идентификатор (id).

# def dec(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         print(f'Функция {func.__name__} была запущена успешно')
#         d = dict()
#         d[func(*args, **kwargs)] = f'Функция {func.__name__}'
#         print(d)
#     return wrapper

# @dec
# def rand():
#     from random import randint
#     return randint(0, 100)

# rand()

# @dec
# def randomizer():
#     from random import randint
#     return randint(0, 100)

# randomizer()
# ==============================================================

# 2) Напишите функцию, которая принимает фразу, и возвращает его сокращенную форму.
# Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest -- FYI и т.п.
# def shorter(phrase):
#     phrase_dict = phrase.split()
#     for i in range(len(phrase_dict)):
#         print(phrase_dict[i][0], end = '')

# shorter('Соединенные Штаты Америки')

# 3) Заядлый турист ведет тщательный учет своих походов. Во время последнего похода, который занял ровно шаги, за каждым шагом отмечалось, был ли это подъем в гору ,, или спуск ,шаг. Походы всегда начинаются и заканчиваются на уровне моря, и каждый шаг вверх или вниз представляет собойизменение единицы высоты. Мы определяем следующие термины:

# Гора – это последовательность последовательных ступенек над уровнем моря, начиная со ступеньки вверх от уровня моря и заканчивая ступенькой вниз до уровня моря.
# Долина — это последовательность последовательных ступеней ниже уровня моря, начиная со ступеньки вниз от уровня моря и заканчивая ступенькой вверх до уровня моря.
# Зная последовательность подъемов и спусков во время похода, найдите и выведите количество пройденных долин .

# пример 1:
#  path = 8
#  steps = 'UDDDUDUU'
#  result = 1 dolina

# пример 2:
#  path = 10
#  steps = 'DUDDDUUDUU'
#  result = 2 dolina

# def uch(steps):
#     count = 0
#     kolvo_0 = 0
#     for i in steps:
        
#         if i == 'U':
#             count += 1
#         elif i == 'D':
#             count -= 1
#             if count == 0:
#                 continue
#         if count == 0:
#             kolvo_0 += 1
#     print(kolvo_0)

# uch('DUDDDUUDUU')