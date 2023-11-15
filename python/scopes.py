# Облость видимости и пространство имен(scopes)
# Технология которая опредиляет контекст имени, в рамках которого мы можем использовать

# built -iins(Встроенная область видомисти) -> print,len,
# global(Гллобальная)-> облость одного файла
# enclosed()не локальная ()
# x = 200
# def myFunc():
#     print(x)
#     a = 300
#     print(a)
#     return a

# myFunc()
# print(a)


# a = 10 # global
# print # built_ini

# def hello(): #global
#     a = 'hello'#local
#     print(a, 'local inside in func')

# hello()
# print(a, 'global')

# LEGB - local enclosed gloobal built-ins
#    ---------->>>>>>.
# ------------------------------------------------
# enclosed
# замкнутное пространство имен - локальное пространство, у которого есть внутреннее(вложение) локадьное пространство

# x = 'global'
# print(x , '1' ) #global

# def enclosed(): # global
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x, '3') # local

#     print(x, '2') #enclosed
#     local()
#     print(x, '4') #enclosed

# enclosed()
# print(x, '5') # global

# =======================
# global -> позволяет изменять значение глобальной переменной

#  nonlocal -> позволяет изменять значение не локальный (замкнутой) переменной находиться внутри локальной облости

# var = 0

# def increment(): #LEGB
#     global var
#     var += 1  #var = var + 1
#     print(var)
    
# increment()
# increment()
# increment()
# increment()
# increment()

# -----------------------------------
# def  counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num +=1
#         return num
#     return increment

# c_steps = counter()
# c_squats = counter()
# # print(c_steps)
# print(c_steps())
# print(c_steps())
# print(c_steps())
# print(c_steps())
# print(c_steps())
# print(c_steps())
# print(c_squats())
# print(c_squats())
# print(c_steps())
# print(c_steps())
# -------------------------------
# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num +=1
#         return num
#     return increment

# def showStats(heros, walkers):
#     print()
#     print(f'Jonh Snow  ты убил: \n\tгероев: {heroes} \n\tбелых ходоkов:{walkers}')
#     print()

# counter_heroes = counter()
# counter_walkers = counter()
# heroes = 0
# walkers = 0

# print('Приветсвую вас, король Севера Jonh Snow, в игре престолов!')
# while True:
#     print('Тебе доступно следующие действия:')
#     print('1-убить героя, 2-убить ходока, 3-статистика,4-выйты из игры')
#     choice = input('ведите что хотите сделать:').strip()
#     if  choice == '1':
#         heroes == counter_heroes()
#         print('вы обезглавили Ланистера!')
#     elif choice == '2':
#         walkers == counter_walkers()
#         print('Вы убили белого ходока!')
#     elif choice == '3':
#         showStats(heroes,walkers)
#     elif choice == '4':
#         print('Bye bye!')
#         break

