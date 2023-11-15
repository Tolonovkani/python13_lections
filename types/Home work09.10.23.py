# Задача 1: Валидация пароля

# Пользователь хочет установить пароль для своей учетной записи. Пароль должен соответствовать следующим критериям:

#     Длина пароля должна быть не менее 8 символов.
#     Пароль должен содержать хотя бы одну заглавную букву (A-Z).
#     Пароль должен содержать хотя бы одну строчную букву (a-z).
#     Пароль должен содержать хотя бы одну цифру (0-9).
#     Пароль должен содержать хотя бы один специальный символ из множества: !@#$%^&*()_-+=<>?/

# Напишите программу, которая запрашивает у пользователя пароль и затем проверяет, удовлетворяет ли он всем критериям. Если пароль удовлетворяет всем критериям, программа должна сообщить, что пароль принят. В противном случае, программа должна вывести сообщение об ошибке, указывая, какие критерии не выполняются.

# while True:
#     b = 0
#     password = input('Vvedite parol: ')

#     if len(password) < 8:
#         raise Exception('parol doljen byt bolshe 8 simvolov!')
#     else:
#         b += 1

#     for i in password:
#         counter = 0
#         if i in '!@#$%^&*()_-+=<>?/':
#             counter += 1
#             break
#     if not counter > 0:
#         raise ValueError('v parole doljen byt hot odin simvol iz "!@#$%^&*()_-+=<>?/"!')
#     else:
#         b += 1

#     for i in password:
#         counter = 0
#         if i.isupper():
#             counter += 1
#             break
#     if not counter > 0:
#         raise ValueError('Doljna byt odna zaglavnaya bukva!')
#     else:
#         b += 1

#     for i in password:
#         counter = 0
#         if i.isdigit():
#             counter += 1
#             break
#     if not counter > 0:
#         raise ValueError('doljna byt odna cifra!')
#     else:
#         b += 1

#     for i in password:
#         counter = 0
#         if i.islower():
#             counter += 1
#             break
#     if not counter > 0:
#         raise ValueError('Doljna byt odna strochnaya bukva!')
#     else:
#         b += 1
    
#     if b == 5:
#         break

    


# Задача 2: Обработка ошибок при работе с элементами списка:

# Создайте список чисел и попробуйте выполнить некоторые операции над элементами списка. Обработайте исключения, такие как IndexError, ValueError и ZeroDivisionError.
# list_ = [1, 2, 3, 4, 5]
# print(list_)
# try:
#    num_1 = int(input('Vvedite index: '))
#    num_2 = int(input('Vvedite index: '))
#    print(list_[num_1] / list_[num_2])
# except IndexError:
#     print('vy vyshli za predely spiska!')
# except ValueError:
#     print('Vvedite pravilnyi index!')
# except ZeroDivisionError:
#     print('Cant divide by zero!')

# Задача 3: Поиск значения в словаре с обработкой исключения:

# Создайте словарь с данными (например, словарь с именами и возрастами людей). Затем запросите у пользователя имя и попробуйте найти возраст этой персоны в словаре. Обработайте исключение, если имя не найдено.
# dict_= {'Aibek': 21, 'Ali':15, 'Beka':18, 'ulan':20}
# print(dict_)
# try:
#   a = input('Vvedite name')
#   print(dict_[a])
# except KeyError:
#   print('Vvedite tolko name!')
# else:
#   print('No errors!')
# finally:
#   print('The end!')  
    
