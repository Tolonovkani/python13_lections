

#     Создайте класс Notebook
#         Создайте метод __init__() и определите внутри него три динамических атрибута: ram (размер оперативной памяти, целочисленное значение), memory (Размер внутренней памяти, целочисленное значение) и cpu (количество ядер в процессоре, целочисленное значение) . Свои начальные значения они получают из параметров метода __init__ ()
#         Напишите метод info () в котором будет возвращаться через return информация о ноутбуке формата: «Ноутбук с 16 ГБ оперативной памяти, 500 ГБ внутренней памяти и с 4 ядрами процессора».
#         Создайте класс-метод add_notebook который будет принимать в себя словарь и на основе словаря будет создавать экземпляр класса.

# Пример словаря = {

#     'ram': 12,

#     'memory': 500,

#     'cpu': 4

# }.

class Notebook:
    def __init__(self,ram,memery,cpu) -> None:
        self.ram = ram
        self.memery = memery
        self.cpu = cpu

    def info(self):
        return f'Ноутбук с {self.ram} ГБ оперативной памяти, {self.memery} ГБ внутренней памяти и с {self.cpu} ядрами процессора'
    
    @classmethod
    def add_notebook(cls,notebook_dict):
         return cls(notebook_dict['ram'], notebook_dict['memory'], notebook_dict['cpu'])
    
notebook_dict = {

    'ram': 12,

    'memory': 500,

    'cpu': 4

}
new_notebook = Notebook.add_notebook(notebook_dict)
print(new_notebook.info())
