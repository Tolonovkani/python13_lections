# """
# 1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.

# class Circle:
#     color = 'Blue'
#     pi = 3.14

#     def __init__(self, rad, color=color) -> None:
#         self.rad = rad
#         self.color = color
    
#     def metod(self):
#         return f'Площад {self.rad ** 2 * self.pi} цвет{self.color}'
#     def __str__(self) -> str:
#         return f'Площад {self.rad ** 2 * self.pi} цвет{self.color}'
        

# kr = Circle(9)
# kr.color = 'red'
# print(kr)


# 2) Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например: "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.


# class Song:
#     def __init__(self,name,avtor,year) -> None:
#         self.name = name
#         self.avtor = avtor
#         self.year = year

#     def show_author(self):
#         print(f'этот песни автор  {self.avtor}')
#     def show_title (self):
#         print(f'названия песни  {self.name}')
#     def show_year(self):
#         print(f'песня вышла  {self.year} году')

# k1 = Song('Москва любить', 'Скриптонит', '2019')
# k1.show_author()
# k1.show_title()
# k1.show_year()
        
# 3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.

# class Taxi:
#     def __init__(self,name_com,pay_p: int,pay_kl: int) -> None:
#         self.name = name_com
#         self.pay_p = pay_p
#         self.pay_kl = pay_kl
    
#     def price(self,km):
#         return f'стоиость поездки: {km * self.pay_kl + self.pay_p} coм'
    

# namba = Taxi('Namba', 100, 20)
# print(namba.price(10))

# yandex = Taxi('Yandex', 100, 15)
# print(yandex.price(10))

# jorgo = Taxi('Jorgo', 100, 10)
# print(jorgo.price(10))



# 4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
# Затем объявите экземляр класса и вызовите метод.
# class Phonebook:
#     def __init__(self,first_name,last_name,nomber):
#         self.name = first_name + ' ' + last_name + ' ' + str(nomber)
       
#     def get_info(self):
#         print(f'Контакт {self.name} ')

# book = Phonebook("Тимур", "Ибрагимович", +996555777888)
# book.get_info()
        


# 5) Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 8%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
# """
class Salary:
    def __init__(self, clas) -> None:
        self.classa = clas
        nalog = 8
        