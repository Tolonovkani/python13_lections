
# Нужно создать to_do_list.txt, куда будут записываться задачи.
# У пользователя 3 выбора

# 1.добавить новую задачу

# 2.удалить задачу. Если нет - сообщить об этом.

# 3.Посмотреть свои задачи

# Использовать try/except , r/w в файл.


# while True:
#     print()
#     a = input('Для добавления новой задачи или удаления введите "w", для просмотра своих задач введите "r"\nДля завершения работы введите exit ').lower()
#     print()
#     if a == 'exit':
#         print('Пока!')
#         break
#     try:

#         with open('to_do_list.txt', 'r') as file:
#             r = file.read()
#             file.seek(0)
#             a3 = file.readlines()
        
#     except FileNotFoundError:
#         with open('to_do_list.txt', 'w+') as file:
#             file.write('')
#             r = file.read()
#             file.seek(0)
#             a3 = file.readlines()
#     count = 1 
#     couny_ = 1
#     try:
        
#         with open('to_do_list.txt', f'{str(a)}+') as file:
#             if str(a) == 'w':
#                 a1 = input('Для выхода на главную введите: home \nХодите добавить задачу?  Y/N: ').lower()
                
#                 if a1 == 'y':
#                     a2 = input('Для выхода на главную введите: home\nНапишите свою задачу сюда: ')
#                     if a2 == 'home':
#                         continue
#                     for line in a3:
#                         count += 1
#                     file.write(r + str(count) + ') ' + a2 + '\n')
                
#                 elif a1 == 'n':
#                     del_ = input('Введите номер строки: ') + ')'
#                     b = []
#                     net = 0
#                     for lines in a3:
#                         line = lines.split()
#                         if line[0] != del_:
#                             b.append(lines)
#                         else:
#                             net += 1
#                             continue
#                     if net == 0:
#                         print('Такой строки нет')
#                     file.writelines(''.join(b))
                    
#                     file.seek(0)
#                     a4 = file.readlines()
#                     p = []
#                     for line in a4:
#                         lines = line.strip()
#                         i = line.index(')')
#                         p.append(str(couny_))
#                         lines = lines[i::]
#                         lines = ''.join(lines)
#                         p.append(lines + '\n')    
#                         couny_ += 1    
#                     file.seek(0)
#                     file.writelines('')
#                     file.writelines(''.join(p))
                    
                    
                
#                 else:
#                     file.write(r)
#                     print()

                
                    
#             elif str(a) == 'r':
#                 print('Ваши задачи: ')
#                 print()
#                 print(file.read())  
#             else:
#                 print('Вводите w, r!')
            
#     except ValueError:
#         print('Введите только w или r либо home/exit')