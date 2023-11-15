# """"
# Tasks: 
# 1) Dollar. 
# Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в долларизованный формат: 
# dollarize(123456.78901) -> "$123,456.80" 
# dollarize(-123456.7801) -> "-$123,456.78" 
# dollarize(1000000) -> "$1,000,000" 
# Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода: init - инициализирует значение атрибута amount 
# update - задаёт объекту новое значение amount 
# repr - возвращает значение float 
# str - метод, который реализует логику функции dollarize() 
# //Вывод должен выглядеть следующим образом: 
# cash = MoneyFmt(12345678.021) 
# print(cash) -- выводит "$12,345,678.02" 
# cash.update(100000.4567) 
# print(cash) -- выводит "$100,000.46" 
# cash.update(-0.3) 
# print(cash) -- выводит "-$0.30" 
# repr(cash) -- выводит -0.3 
# """
# print("ZADACHA --- 1")
# =============================
# def dollarize(amount):
#     if isinstance(amount, float):
#         formatted_amount = "${:.2f}".format(amount)
#         return formatted_amount

# class MoneyFmt:
#     def __init__(self, amount):
#         if isinstance(amount, (int, float)):
#             self.amount = float(amount)
#         else:
#             raise ValueError("Amount must be an int or float")

#     def update(self, amount):
#         if isinstance(amount, (int, float)):
#             self.amount = float(amount)
#         else:
#             raise ValueError("Amount must be an int or float")

#     def __repr__(self):
#         return str(self.amount)

#     def __str__(self):
#         return dollarize(self.amount)


# cash = MoneyFmt(12345678.021)
# print(cash) 

# cash.update(100000.4567)
# print(cash) 

# cash.update(-0.3)
# print(cash) 

# print(repr(cash)) 

        
# """
# 2) Велосипед. 
# Создайте класс Bike в котором будут инициализированы следующие атрибуты: self.cost (стоимость) 
# self.make (производитель) 
# self.model (модель) 
# self.year (год выпуска) 
# self.condition (состояние) 
# self._sale_price = None (цена для продажи, по умолчанию None) 
# self.sold = False (продан или нет, по умолчания False) 
# Также укажите мин. прибыль, которая должна прийти с продажи велосипеда. Создайте метод для указания цены для продажи, который принимает цену и если она меньше стоимости, то ставит дефолтную цену для продажи (стоимость + мин. прибыль). 
# Для ремонта велосипеда будет использоваться метод service, которая принимает стоимость ремонта и новое состояние велосипеда, соответственно продажная цена велосипеда возрастает на столько, сколько обошелся ремонт и возвращает нынешнюю цену для продажи. При продаже велосипеда будет использоваться метод sell, который меняет значение self.sold на
# True и возвращает прибыль с продажи. 
# Допишите метод get_default_bike, который будет создавать дефолтный велосипед. Создайте объект bike = Bike.get_default_bike() и используете его методы и получите значения всех его атрибутов. 

# print("\nZADACHA --- 2")


# class Bike:
    
#     min_profit = 50

#     def __init__(self, cost, make, model, year, condition):
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self._sale_price = None  
#         self.sold = False

#     def set_sale_price(self, price):
#         if price < self.cost + self.min_profit:
#             self._sale_price = self.cost + self.min_profit
#         else:
#             self._sale_price = price

#     def service(self, repair_cost, new_condition):
    
#         self._sale_price += repair_cost
#         self.condition = new_condition
#         return self._sale_price

#     def sell(self):
#         self.sold = True
#         profit = self._sale_price - self.cost
#         return profit

#     @classmethod
#     def get_default_bike(cls):
#         return cls(200, "BrandX", "ModelY", 2022, "Good")


# bike = Bike.get_default_bike()

 
# bike.set_sale_price(250)
# print(f"Cost: {bike.cost}")
# print(f"Make: {bike.make}")
# print(f"Model: {bike.model}")
# print(f"Year: {bike.year}")
# print(f"Condition: {bike.condition}")
# print(f"Sale Price: {bike._sale_price}")
# print(f"Sold: {bike.sold}")


# new_sale_price = bike.service(15, "Отлично")
# print(f"Новая цена продажи после обслужевания: {new_sale_price}")


# profit = bike.sell()
# print(f"Прбыль от прадажи: {profit}")
# print(f"Продано: {bike.sold}")

# """
# 3) Герой. 
# Разработайте программу по следующему описанию. 
# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня. 
# В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки. 
# Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего команде с более длинным списком, поднимается уровень. Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.
# """

