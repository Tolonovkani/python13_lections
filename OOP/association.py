# # Associotion - означает что внутри ондного объекта будет существовать другой объект в качастве аттрибута
# # 1 Композиция - сильная связь 
# # 2  Агрегация  - слабая связь

# # Компазиция - это когда стена не существует отдельно от комнаты. Она создается при создании комнаты и полностью управляется классом комнаты.

# # Агрегация  - это когда экземпляр двигателя создается где то в другом месте, передается в класс Авто в качестве параметре.


# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100
#     @property
#     def power(self):
#         return self._power
    
#     @power.setter
#     def power(self,value):
#         self._power = value

# class Iphone:
#     def __init__(self, color) -> None:
#         self.color = color
#         self.battery = Battery()

#         #когды мы создоем внутри класса объект от дпугого класса - композиция

# a = Iphone('silver')
# a.battery.power = 50
# print(a.battery.power)
# a.battery.charge()
# print(a.battery.power)
# del a
# # при удаленния айфон с ним удаляется батарейка


# class Nokia:
#     def __init__(self, color, battery) -> None:
#         self.color = color
#         self.battery = battery
#         #Агригат когда объект создается вне класса и передается внутрь агрегация


# battery = Battery()
# nokia1 = Nokia('black', battery)
# nokia1.battery.power = 50
# print(nokia1.battery.power)
# nokia1.battery.charge()
# print(nokia1.battery.power)
# del nokia1

# nokia2 = Nokia('white', battery)
# print(nokia2.battery.power)
# nokia2.battery.charge()
# print(nokia2.battery.power)
# ====================================================


# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.
from datetime import datetime, timedelta
from time import sleep

class Phone:
    def __init__(self, imei, os):
        self.__imei = imei
        self.__os = os
        self.__battery = 100

    @property
    def battery(self):
        if self.__battery < 0.5:
            raise Exception('Телефон разряжен!')
        print(f'Уровен заряда: {self.__battery}!')
        self.__battery -= 0.5

    
    @property
    def get_info(self):
        if self.__battery < 0.5:
             raise Exception('Телефон разряжен!')
        print(f'OS: {self.__os}, IMEI: {self.__imei}!')
        self.__battery -= 0.5

    def play_misic(self):
        if self.__battery < 5:
            raise Exception('Телефон разряжен!')
        print('Слушаем Мирбек А.!')
        self.__battery -= 5


    def play_video(self):
        if self.__battery < 10:
            raise Exception('Телефон разряжен!')
        print('смотрим давидича')
        self.__battery -= 7

    def charge_battery(self, sec):
        now = datetime.now #11:58:20
        end = (now() + timedelta(seconds=sec)).strftime('%H:%M:%S')
        # print(now()).strftime('%H:%M:%S')
        # print(end)
        while now().strftime('%H:%M:%S') != end:
            # print(now().strftime('%H:%M:%S'))
            sleep(1)
            if self.__battery < 100:
                self.__battery += 1
                if self.__battery > 100:
                    self.__battery = 100

            print(f'Идет зарядка батареи! Ваш уровен батареи: {self.__battery}!')

phone = Phone('777', 'ios 16')
phone.battery 
phone.battery
phone.get_info
phone.battery
phone.play_misic()
phone.battery
phone.play_video()
phone.play_video()
phone.battery
phone.charge_battery(20)
