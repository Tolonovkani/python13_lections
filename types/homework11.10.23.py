# Задача 1
# list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]
# print(list_1)
# print()
# def ls(a):
#     names = [i for i in a if type(i) == str]
#     names = sorted(names)
#     print(f'Список имен { names}')
#     nums_int = [i for i in a if type(i) == int]
#     nums_int = sorted(nums_int)
#     nums_int = nums_int[::-1]
#     print(f'Список с целыми числами {nums_int}')
#     nums_float = 0
#     for i in a:
#         if type(i) == float:
#             nums_float += i
#     print(f'Сумма цифр с плавающей точкой: {nums_float}')
# ls(list_1)
# =====================================
   # Задача 2
# def sandv(razm, list_):
#     list_ = ', '.join(list_)
#     print(f'{razm} сендвич со следующими ингридиентами: {list_}')
# sandv('Большой', ['майонез', 'колбаса', 'огурец', 'сыр'])
# print()
# sandv('Маленький', ['яйцо', 'кетчуп', 'сосиска'])
# print()
# sandv('Средний', ['морковка', 'капуста', 'котлета', 'чеснок'])

# ===========================================
# Задача 3
# def car(proizvod, model, **dop_info):
#     b = []
#     b.append(proizvod)
#     b.append(model)
#     for k, v in dop_info.items():
#         b.append(k + ' is')
#         if type(v) == int:
#             v = str(v)
#         b.append(v + ',')
#     b = ' '.join(b)
#     b.replace(b[-1], '.l')
#     print(b)
# car('Subary', 'Outback', color='red', year=2022, engine='v12')



# ===========================================
# Задача 4
# flag = True


# def count_letters(str_, letter, num):
#     a = 0
#     b = 0
#     str_ = str_.lower()
#     if letter in str_:
#         b = str_.count(letter)
#     if num in str_:
#         a = str_.count(num)
#     elif letter == 'выход' or num == 'выход':
#         global flag
#         flag = False
#     print(f'Количество цифр {num}: {a} \nКоличесвто букв  {letter}: {b}')
    
# while True:
#     count_letters(input('Введите текст: '), input('Какую букву ищем? '), input('Какую цифру ищем? '))
# ========================================
 # Задача 5


# dict_ = {'Асан': 'Директор', 'Айбек': 'Python разработчик', 'Малдыбек': 'Учитель'}
# def work(a):
#     for k, y in a.items():
#         print(f'Работник {k}, занимает должность {y}')
# work(dict_)
# ===============================
# 6 задача
# def calc1():
#     while True:
#         a = input('Число a: ')
#         if 'q' in a:
#             break
#         elif a == '':
#             print('Нет ничего приятнее, чем знание о твоих знаниях!')
#             continue

#         b = input('Число b: ')
#         if 'q' in b:
#             break
#         elif b == '':
#             print('Нет ничего приятнее, чем знание о твоих знаниях!')
#             continue
# ========================================
# задача 7
#         math = input('Тип операции (+, -, /, *): ')
#         if 'q' in math:
#             break
#         elif math == '':
#             print('Нет ничего приятнее, чем знание о твоих знаниях!')
#             continue

#         a = float(a)
#         b = float(b)
        
#         if math=='+':
#             print(a+b)

#         elif math=='-':
#             print(a-b)

#         elif math=='/':
#             if b != 0:
#                 print(a/b)
#             else:
#                 print('!')

#         elif math=='*':
#             print(a*b)

#         else:
#             print('Ошибка')
# calc1()