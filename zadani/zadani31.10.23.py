# """
# 1)Создайте класс и объявите в нём 3 метода: публичный, защищённый и приватный. Затем создайте экземпляр данного класса и вызовите по очереди каждый из методов.
# """
# --------------------------------------
# class Tefal:
#     def turn_on(self):
#         print('разогревание воды')

#     def _a2(self):
#         print('Проверка температуры воды')

#     def __turn_off(self):
#         print("Автоматический выключение")

# a = Tefal()
# a.turn_on()
# a._a2()
# a._Tefal__turn_off()
# -----------------------------------------------
# """
# 2)Определите класс A, в нём объявите метод method1, который печатает строку "Hello World". Затем создайте класс B, который будет наследоваться от класса A. Создайте экземпляр от класса B, и через него вызовите метод method1.
# """
# class A:
#     def method1(self):
#         print("hello world")

# class B(A):
#     pass

# a = B()
# a.method1()

# """
# 3)Объявите класс Car, в котором будет приватный атрибут экземпляра speed. Затем определите метод set_speed, который будет устанавливать значение скорости и метод show_speed, с помощью которого Вы будете получать значение скорости.
# """
# class Car:
#     def __init__(self):
#         self.__speed = 0
    
    
    
#     def set_speed(self, speed):
#         if speed >= 0:
#             self.__speed = speed
#         else:
#             print('скорость не может быть не отрицательной')


#     def show_speed(self):
#         return self.__speed
    
# my_car = Car()
# my_car.set_speed(120)


# current_speed = my_car.show_speed()
# print(f"Текущая скорость: {current_speed} км/ч")

# """
# 4)Перепишите класс Car из предыдущего задания.
# Перепишите метод set_speed() с использование декоратора @speed.setter, а метод show_speed() с использованием декоратора @property, для того чтобы можно было работать с данным классом следующим образом:


# class Car:
#     def __init__(self):
#         self.__speed = 0  

#     @property
#     def speed(self):
#         return self.__speed

#     @speed.setter
#     def speed(self, new_speed):
#         if new_speed >= 0:
#             self.__speed = new_speed
#         else:
#             print("Скорость не может быть отрицательной.")


# car = Car()
# car.speed = 120
# print(car.speed)

# """
# 5. Создайте класс Car. Пропишите в init параметры make, model, year, odometer, fuel.
# Пусть у показателя odometer будет первоначальное значение 0, а у fuel 70.
# Добавьте метод drive, который будет принимать расстояние в км. В самом начале проверьте,
# хватит ли вам бензина из расчета того, что машина расходует 10 л / 100 км (1л - 10 км) . Если
# его хватит на введенное расстояние, то пусть этот метод добавляет эти километры к значению
# одометра, но не напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью приватного
# метода __subtract_fuel, затем пусть распечатает на экран “Let’s drive!”. Если же бензина не Let’s drive!”. Если же бензина не
# хватит, то распечатайте “Let’s drive!”. Если же бензина не Need more fuel, please, fill more!”
# """
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0
#         self.__fuel = 70 

#     def drive(self, distance):
       
#         fuel_needed = distance / 10  # Расход топлива: 10 литров на 100 км
#         if fuel_needed <= self.__fuel:
#             self.__subtract_fuel(fuel_needed)
#             self.__add_distance(distance)
#             print("Let's drive!")
#         else:
#             print("Need more fuel, please, fill more!")

#     def __add_distance(self, distance):
#         self.odometer += distance

#     def __subtract_fuel(self, fuel_used):
#         self.__fuel -= fuel_used

# my_car = Car("Toyota", "Camry", 2023)

# my_car.drive(300) 

# my_car.drive(800)  


# """
# 6)# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# # батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# # Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# # При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# # Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# # полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# # разряжен).
# # Также предусмотрите возможность заряжания батареи.
# # ""

# class MobilePhone:
#     def __init__(self, imei, os_info, battary=100):
#         self.__imei = imei
#         self.__battery_level = battary
#         self.__os_info = os_info

#     def play_music(self):
#         if self.__battery_level >= 5:
#             self.__consume_battery(5)
#             print("Playing music...")
#         else:
#             print("телефон разряжен")

#     def watch_video(self):
#         if self.__battery_level >= 7:
#             self.__consume_battery(7)
#             if self.__battery_level < 10:
#                 print("низкий уровень батареи, не смотрите видео.")
#             else:
#                 print("Watching video...")
#         else:
#             print("выбрасывайте ошибку, что телефон разряжен.")

#     def charge_battery(self, charge_percent):
#         if self.__battery_level == 0:
#             raise ValueError("телефон разряжен")
#         self.__battery_level = min(10, self.__battery_level + charge_percent)

#     def __consume_battery(self, percentage):
#         if self.__battery_level > 0:
#             self.__battery_level = max(5, self.__battery_level - percentage)
#         else:
#             raise ValueError("выбрасывайте ошибку, что телефон разряжен.")

# # Создание объекта MobilePhone
# my_phone = MobilePhone("123456789", "Android 12")

# # # Пример использования методы

# my_phone.charge_battery(50)  
# my_phone.play_music()  

# my_phone.charge_battery(30) 
# my_phone.watch_video()  
# print(my_phone._MobilePhone__battery_level)
