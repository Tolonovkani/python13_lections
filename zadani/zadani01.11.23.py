# """
# 1. Создайте класс Account и переопределите в нем методы init, repr, str и del.
# Объекты класса должны содержать атрибуты имени, баланса и города, где открыт счет.
# Метод init должен возвращать сообщение о создании счета, repr только имя держателя счета
# и баланс, а str сообщение с приветствием и также информацией о держателе счета, 
# балансе и филиале банка в котором зарегистрирован клиент, del в свою очередь сообщение об удаление 
# и слово "Пока!"

# class Account:
    
#     def __init__(self,name,balance,city) -> None:
#         self.name = name
#         self.balance = balance
#         self.city = city
#         print('счёт открыт')
#     def __repr__(self) -> str:
#         return f'{self.name}, {self.balance}'
#     def __str__(self) -> str:
#         return f'Здраствуйте {self.name} ваш баланс {self.balance} Optima '
#     def __del__(self):
#         return 'ваш счёт удалён пока'
    
# a = Account('Айба',500000, "Bishkek")
# print(a)
# print(a.__repr__())
# print(a.__del__())
# """
# 2. Определите класс MyNumber который наследуется от класса int. 
# У экземпляра класса должен быть обязательный атрибут value. 
# Переопределите методы сложения, вычитания, умножения и деления для класса таким  образом чтобы при при использовании операторов + - * / - результат возвращался с сообщением об использованном методе, 
# например:print(num + 5)  -------> "Это сложение и Ваш результат равен 10"
# # """
# class MyNumber(int):
#     def __init__(self, value):
#         super().__init__()  
#         self.value = value

#     def __add__(self, other):
#         result = super().__add__(other)  
#         return f"Это сложение и Ваш результат равен {result}"

#     def __sub__(self, other):
#         result = super().__sub__(other)  
#         return f"Это вычитание и Ваш результат равен {result}"

#     def __mul__(self, other):
#         result = super().__mul__(other)  
#         return f"Это умножение и Ваш результат равен {result}"

#     def __truediv__(self, other):
#         result = super().__truediv__(other) 
#         return f"Это деление и Ваш результат равен {result}"


# num = MyNumber(265)
# print(num + 3)  
# print(num - 2)  
# print(num * 4)  
# print(num / 2)  
# -=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-

# """
# 3. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
# элементов начиналась с 1. Например:
# x = MyList([1,2,3,4,5])
# x[1] → 1
# """
# class MyList(list):
#     def __init__(self,nomer):
#         self.nomer = nomer

#     def __getitem__(self,key):
#         if key > 0:
#             return self.nomer[key -1]
#         elif key < 0:
#             return self.nomer[key]
#         else:
#             raise IndexError

    
# x = MyList([1,2,3,4,5])
# print(x[1])
    
# """
# 4. Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: имя, фамилия, класс, и оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
# Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
# """

# class Student:
#     def __init__(self, first_name, last_name, grade, scores):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grade = grade
#         self.scores = scores

#     def average_score(self):
#         if self.scores:
#             total_score = sum(self.scores.values())
#             return total_score / len(self.scores)
#         else:
#             return 0

#     def __lt__(self, other):
#         return self.average_score() < other.average_score()

#     def __le__(self, other):
#         return self.average_score() <= other.average_score()

#     def __eq__(self, other):
#         return self.average_score() == other.average_score()

#     def __ne__(self, other):
#         return self.average_score() != other.average_score()

#     def __gt__(self, other):
#         return self.average_score() > other.average_score()

#     def __ge__(self, other):
#         return self.average_score() >= other.average_score()

# # Пример использования класса Student
# student1 = Student("John", "Doe", "10th", {'math': 70, 'history': 60, 'literature': 60})
# student2 = Student("Jane", "Smith", "10th", {'math': 60, 'history': 50, 'literature': 40})
# student3 = Student('Bob', 'Johnson', '10th', {'math': 50, 'history': 70, 'literature': 60})

# students = [student1, student2, student3]

# students.sort()  # Сортировка студентов по средней оценке
# for student in students:
#     print(f"{student.first_name} {student.last_name}: Average Grade = {student.average_score()}")



# """
# 5. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
# Также в методе new напишите условие для удаления
# пробелов и пустых строк в созданных словах.
# """

# class Word:
#     def __init__(self,value) -> None:
#         self.value = value.strip()
        

#     def __gt__(self,other):
#         return len(self.value) > len(other.value)
#     print('больше')
    
#     def __lt__(self,other):
#         return len(self.value) < len(other.value)
#     print('меньше')

#     def __le__(self,other):
#         return len(self.value) <= len(other.value)
#     print('меньше или равно')

#     def __ge__(self,other):
#         return len(self.value) >= len(other.value)
#     print('больше или равно')

#     def __str__(self):
#         return self.value

# a1 = Word('Hello word')
# a2 = Word('Hello')
# a3 = Word('Hello my friend')
# a4 = Word('hi')
# print(a1 > a2)
# print(a3 < a4)
# print(a2 <= a3)
# print(a1 >= a4)
# ========================================================
# 1),2),3) Создайте класс Person и объявите в нем 3 атрибута класса: name (public), phone_number(protected) и сard_number(private), атрибуты класса будут равны следующим значениям: "John", "+996 557 55 17 57" и "9999 9999 9999 9999". Создайте объект 'john' класса Person и выведите на экран все атрибуты класса.

# class Person:
#     def __init__(self,) -> None:
#         self.name = "John"
#         self.phone_number = '+996 777 77 77 77'
#         self.card_number = '9999 9999 9999 9999'

# john = Person()

# print('имя:', john.name)
# print('номер тел:', john.phone_number)
# print('номер карты:', john.card_number)

# 4) Продолжая изменять логику предыдущего задания создайте класс Person у которого будут следующие атрибуты экземпляра класса: name (public), phone_number(protected) и сard_number(private). При инициализации обьекта проверяйте введенные имя. Для этого напишите приватный метод validate_name для валидации имени: данный метод будет проверять длину имени, если длина имени меньше двух то возвращайте имя по дефолту John, если же введенное пользователем имя больше двух, то необходимо возвращать имя с заглавной буквы (JOHN -> John, john -> John и тд). Создайте экземпляр sam класса Person со значениями ("SAM", "+996 557 55 17 57" и "9999 9999 9999 9999") и выведите на экран все его атрибуты
# 
# class Person:
#     def __init__(self,name, phone_number, card_number) -> None:
#         self.name = self.validate_name(name)
#         self._phone_number = phone_number
#         self.__card_number = card_number

#     def validate_name(self, name):
#         if len(name) < 2:
#             return 'John'
#         else:
#             return name.capitalize()
        
# sam = Person('SAB', '+996 777 77 77 77', '9999 9999 9999 9999')
# print("Имя:", sam.name)
# print("Номер телефона:", sam._phone_number)
# print("Номер карты:", sam._Person__card_number)

# 5) На этот раз заказчик передумал и попросил вас переписать предыдущий класс, теперь его интересует только валидация номера телефона и номера карты. Создайте класс Person у которого будут следующие атрибуты экземпляра класса: name (public), phone_number(protected) и сard_number(private). При инициализации обьекта проверяйте введенный номер телефона и номер карты. Для этого напишите приватный метод validate_phone_number и защищенный метод validate_cart_number.
# Метод validate_phone_number сначала проверяет на то чтобы номер телефона являлся типом int иначе возвращаем None далее нужно также проверять, чтобы номер начинался на 999 иначе возвращается None
# Метод validate_cart_number в первую очередь также проверяет то что бы номер карты являлся типом int иначе возвращаем None далее нужно также проверять что чтобы количество цифр в номере карт была ровно 16 иначе также возвращаем None. Создайте экземпляр 'tolik' класса Person c правильными данными и выведите на экран все его атрибуты

# class Person:
#     def __init__(self,name, phone_number, card_number) -> None:
#         self.name = name
#         self._phone_number = self.validate_phone_number(phone_number)
#         self.__card_number = self.validate_card_number(card_number)
    
#     def validate_phone_number(self,phone_number):
#         if isinstance(phone_number, int) and str(phone_number).startswith('999'):
#             return phone_number
#         else:
#             return None
        
#     def validate_card_number(self,card_number):
#         if isinstance(card_number, int) and len(str(card_number)) == 16:
#             return card_number

#         else:
#             return None
        
# tolik = Person("Tolik", 99955551757, 9999999999999999)


# print("Имя:", tolik.name)
# print("Номер телефона:", tolik._phone_number)
# print("Номер карты:", tolik._Person__card_number)

# 6) Необходимо написать класс Game у которого есть приватный атрибут класса "level" который равен нулю и атрибут экземпляра класса name (ваше имя).
# Класс Game должен иметь методы для увеличения уровня игры (play) и получения текущего уровня (get_level).
# Метод play принимает в себя переменную hours и проверяет если значение этой переменной больше двух то уровень игры увеличивается на единицу иначе ничего не происходит. Так как атрибут класса "level" приватный и поэтому недоступен извне, необходимо реализовать метод "get_level" который возвращает значение атрибута "level".
# Создайте экземпляр "game" класса Game. Выведите на экран значение атрибута "level" затем два раза используйте метод play чтобы уровень игры поднялся на два, после снова выведите на экран значение атрибута "level".    

# class Game:

#     __level=0

#     def __init__(self,name):
#         self.name = name
    
#     def play(self,hours):
#         if hours > 2:
#             self.__class__.__level += 1

#     def get_level(self):
#         return self.__class__.__level

# game = Game('Ваша имя')

# print('Начальный уровен игры:', game.get_level())
# game.play(1)
# game.play(3)

# print('Уровен игры  после игры', game.get_level())
# ========================================================

# 7) Необходимо написать класс Game у которого есть приватный атрибут класса "level" который равен нулю и атрибут экземпляра класса name (ваше имя).
# Класс Game должен иметь два метода: "set_level" и приватный метод "validate_name". 
# При инициализации экземпляра класса вызывается приватный метод validate_name который возвращает имя в котором первая буква в верхнем регистре, а остальные в нижнем (JOHN -> John).
# Также в классе необходимо реализовать метод "set_level" который принимает в себя переменную "level" и увеличивает  значение приватного атрибута класса "level" на значение этой переменной которую передали только в том случае если имя обьекта (который сейчас играет в эту игру) "Tolik", иначе выведите на экран '"имя_обьекта" ты не Tolik!'.
# Создайте сначала экземпляр класса "game" и передайте ему имя Raychel в качестве аргумента. Далее вызовите метод set_level и передайте ему значение 5. После выведите в терминал значение атрибута "level" (так как у нас не реализован метод get_level, выведите это "нелегальным" способом). Теперь создайте экземпляр класса game2 и передайте ему имя "TOLIK" в качестве аргумента. Далее вызовите метод set_level и передайте ему значение 5. После выведите в терминал значение атрибута "level" (так как у нас не реализован метод get_level, выведите это "нелегальным" способом).
# Ожидаемый вывод: 
# Raychel ты не Tolik!
# 0
#
# 5
 
# class Game:

#     __level=0

#     def __init__(self,name):
#         self.name = self.validate_name(name)

#     def validate_name(self, name):
#         return name.capitalize()
        
#     def set_level(self,level):
#         if  self.name == 'Tolik':
#             self.__class__.__level += level
#         else:
#             print(f'{self.name} ты не Толик ебись отсюда!!!')

# game = Game('Tolik')

# game.set_level(5)

# print(Game._Game__level)

# game2 = Game("Tolik")

# game2.set_level(5)

# print(Game._Game__level)


# 😍 Необходимо написать класс Game у которого есть приватный атрибут класса level который равен нулю и атрибут экземпляра класса name (ваше имя).
# Так как атрибут класса level приватный и поэтому недоступен извне, необходимо реализовать два метода для работы с ним: get_level и set_level. Где get_level возвращает значение атрибута level и set_level принимает значение и присваивает его атрибуту level. Создайте экземпляр game класса Game. Выведите на экран значение атрибута level затем присвойте ему значение 10 и выведите его на экран.

# class Game:
#     __level = 0

#     def __init__(self,name) -> None:
#          self.name = name

#     def get_level(self,):
#         return self.__class__.__level

#     def set_level(self, level):
#         self.__class__.__level = level


# game = Game('Ведите имя')
# 

# print('Начальный уровень игры:', game.get_level())

# game.set_level(10)
# print('Уровен игры после устоновки:', game.get_level())



# 9) Необходимо написать класс Game у которого есть приватный атрибут класса level который равен нулю. Напишите метод level с использование декоратора @property для предоставления доступа к атрибуту level. Создайте экземпляр game класса Game. Выведите на экран значение атрибута level.

# class Game:
#     __level = 0 

#     @property
#     def level(self):
#         return self.__class__.__level

# game = Game()

# print('Уровень игры:', game.level)


# 10) Необходимо написать класс Game у которого есть приватный атрибут класса level который равен нулю. Напишите метод level с использованием декоратора @setter для того чтобы вы имели право на изменение приватного атрибута класса level вне класса Game. Но обратите внимание что вы не сможете написать этот метод без метода level у которого используется декоратор @property, поэтому также создайте этот метод.
# Создайте экземпляр game класса Game. Выведите на экран значение атрибута level, после 'легально' измените значение level на 10 и снова выведите это значение на экран.

# class Game:
#     __level = 0

#     @property
#     def level(self):
#         return self.__class__.__level
    
#     @level.setter
#     def level(self,new_level):
#         self.__class__.__level = new_level

# game = Game()

# print('уровен игры:', game.level)
# game.level = 10

# print('Уровен игры после изминени:', game.level)

# 11) Напишите класса Person, который будет хранить информацию о пользователе. У обьекта будут следующие атрибуты экземпляра класса: имя(name), фамилия(last_name), возраст(age), почта (email). При инициализации обьекта, передовать аргументы классу не нужно, все его атрибуты по умолчанию будут равны None и также все они будут приватными. Поэтому реализуйте для каждого атрибута методы доступа get и set не используя декораторы property и setter. У вас будут такие методы: get_name, set_name, get_last_name, set_last_name, get_age, set_age, get_email, set_email.
# Создайте экземпляр john класса Person выедите все его атрибуты, затем измените их как показано ниже и после снова выведите на экран. Пример:
# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com
# ================================================================

# class Person:
    # def __init__(self):
    #     self._name = None
    #     self._last_name = None
    #     self._age = None
    #     self._email = None

    # def get_name(self):
    #     return self._name

    # def set_name(self, name):
    #     self._name = name

    # def get_last_name(self):
    #     return self._last_name

    # def set_last_name(self, last_name):
    #     self._last_name = last_name

    # def get_age(self):
    #     return self._age

    # def set_age(self, age):
    #     self._age = age

    # def get_email(self):
    #     return self._email

    # def set_email(self, email):
    #     self._email = email

# Создаем экземпляр класса Person
# john = Person()

# # Выводим атрибуты объекта john (в начале они все равны None)
# print(john.get_name())  # None
# print(john.get_last_name())  # None
# print(john.get_age())  # None
# print(john.get_email())  # None

# # Устанавливаем значения атрибутов
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')

# # Выводим атрибуты объекта john после установки значений
# print(john.get_name())  # John
# print(john.get_last_name())  # Snow
# print(john.get_age())  # 30
# print(john.get_email())  # johnsnow@gmail.com
# ======================================================
# 12) Перепишите предыдущий класс используя декораторы property и setter. Условие: Реализуйте класс Person, который будет хранить информацию о пользователе. У обьекта будут следующие атрибуты экземпляра класса: имя(name), фамилия(last_name), возраст(age), почта (email). При инициализации обьекта, передовать аргументы классу не нужно, все его атрибуты по умолчанию будут равны None и также все они будут приватными. Поэтому реализуйте для каждого атрибута методы доступа get и set с помощью декораторов которые вы прошли.
# Создайте экземпляр john класса Person выедите все его атрибуты, затем измените их как показано ниже и после снова выведите на экран. Пример:
# john = Person()
# print(john.name) # None
# print(john.last_name) # None
# print(john.age) # None
# print(john.email) # None
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name) # John
# print(john.last_name) # Snow
# print(john.age) # 30
# print(john.email) # johnsnow@gmail.com

# Согласитесь что этот способ использования декораторы позваоляет писать более понятный и элегантный код
# class Person:
#     def __init__(self):
#         self._name = None
#         self._last_name = None
#         self._age = None
#         self._email = None

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value

#     @property
#     def last_name(self):
#         return self._last_name

#     @last_name.setter
#     def last_name(self, value):
#         self._last_name = value

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         self._age = value

#     @property
#     def email(self):
#         return self._email

#     @email.setter
#     def email(self, value):
#         self._email = value

# # Создаем экземпляр класса Person
# john = Person()

# # Выводим атрибуты объекта john (в начале они все равны None)
# print(john.name)  # None
# print(john.last_name)  # None
# print(john.age)  # None
# print(john.email)  # None

# # Устанавливаем значения атрибутов с использованием setter-методов
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'

# # Выводим атрибуты объекта john после установки значений
# print(john.name)  # John
# print(john.last_name)  # Snow
# print(john.age)  # 30
# print(john.email)  # johnsnow@gmail.com
# ================================================

# 13) Реализуйте класс Dad у которого будут следующие атрибуты класса: name который равен 'John', защищенный атрибут last_name который равен 'Snow' и приватный атрибут age равный 40. Затем реализуйте класс Me: который будет наследоваться от класса Dad и будет содержать атрибуты name равный 'Sam', защищенный атрибут last_name равный фамилии отца и приватный атрибут age равный 10. Также реализуйте 2 метода: about_me который выводит информацию об этом обьекте в виде: 'My name is Sam Snow and I am 10 years old' и about_dad который выводит информацию об этом обьекте в виде: 'My father is John Snow'. (Обратите внимание что в методе about_father мы не выводим атрибут age обьекта отца, как этот атрибут приватный а это значит что он не будет доступен в дочерних классах).
# Создайте экземпляр me класса Me и вызовите методы обьекта (их два).
# Ожидаемый результат: 
# My name is Sam Snow and I am 10 years old
# My father is John Snow


# class Dad:
#     name = "John"
#     _lastname = "Snow"
#     __age = 40

# class Me(Dad):
#     name = "Sam"
#     _age = 10

#     def about_me(self):
#         return f"My  name is {self.name} {self._lastname} and I am {self._age} year old "
    
#     def about_dad(self):
#         return f"My dad is {Dad.name} {Dad._lastname}"
    
# me = Me()

# print(me.about_me())
# print(me.about_dad())