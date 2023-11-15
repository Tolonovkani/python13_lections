# Робота с файлами

# Каретка - Указатель-Курсор

# open(<путь до файла>)

# file = open('files18.1023.py')# Относительный путь
# ~ working -> Desktop/bootcamp5/files/lections/files18.10.23.py
# files -> lections/files18.10.23.py

# base_dir = '/users/sangar/desktop/bootcamp5/files'
# file = open(base_dir + 'lections/files18.10.23.py')

# file = open('files18.10.23.py')
# data  = file.read()
# print(data,type(data))
# file.close()


# режимы  с работы с файлами
# 1 r/r+/rb -> read - для чтения файлов
# 2 w/x+/wb -> write - для записи данных
# 3 a/a+ -> для добовленние данных
# b, x

# file = open('test.txt', 'r')
# print(file.read())
# file.close() 


# file = open('test.txt', 'r')
# print(file.readlines())
# file.close() 



# file = open('test.txt', 'r')
# print(file.readline())
# print(file.readline())
# file.close() 

# file.tell() - возврашает индекс где находиться крсор(указатель)

# file.seek()- перемещает курсор на индекс  который вы передали


# file = open('test.txt', 'r')
# print(file.tell())
# data = file.read()
# print(data, '!!')
# print(file.tell())
# file.seek(0)
# print(file.tell())
# print(file.read())
# print(file.tell())
# file.close()


# контекстный менеджер
# with open ('test.txt', 'r') as file:
#     data = file.read()
#     print(data)
#     print(file, 'inside')

# print(file.read(), 'outsode')

# with open('test.txt', 'w') as file:
#     file.write('pervaya stroka!\n')
#     file.write('He is baastard of Ned Stark!\n')
#     file.write('This is lection about files!\n')
#     file.seek(0)
#     data = ['Test1 stroka!\n', 'Test 2 straka!']
#     file.writelines(data)


# with open('test.txt', 'a') as f:
#     f.seek(0)
#     f.write('\nJonh snow is king of North!')
#     f.write('\nYou know nothing John Snow!')
#     f.seek(0)
#     print(f.read())

# try:
#     from PIL import Image
# except ImportError:
#     import Image

# import pytesseract
# import re

# base_url = '/home/kanybek/Desktop/bootcamp5/files/lections/'


# def get_imei_code(image: str):
#     string = pytesseract.image_to_string(image)
#     # print(string)
#     list_of_imei = re.findall(r'IMEI\d.\s\d+',string)
#     print(list_of_imei)

#     with open('imei_codes.txt', 'w') as file:
#         for x in list_of_imei:
#             file.write(f'{x}\n')


# image = base_url + 'imei.jpg'
# get_imei_code(image)





