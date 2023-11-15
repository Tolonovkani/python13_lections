# PostgreSQL -Система управления базами данных(СУБД/DBMS)
# ЭТО ряд програм и инструментов позваляющих создовать БД,управлять ею и манипулировать данными внутри(CRUD)

# Postgres - сама база даных , она объектно реляционная , то есть данные храниться в виде таблиц, т таблицы имеют связи между собой 

# SQL (structured Query Language) - декларативный язык структированных запросов он принимаеться для создонная и получения данных при помощи 
# -----------------------------------------------

#команда вход в од через юзера postgres:
# sudo -u postgres psql

# команда для входа 
# psql

# команда для выхода 
# \q
# exit

# создания суперюзера
# CREATE ROLE 'username' SUPERUSER LOGIN PASSWORD '1';

# Изменения пороля
# ALTER USER 'username' WITH PASSWORD '1';

# Создание бд
# CREATE DATABASE 'name';

# \l - список всех бд

# \du - все юзеры

# \dt - все таблицы (нужно подключить к бд заранее)

# \d 'name' - подобная информация про таблицу (нужно подкльючит к бд заранее)

# \с 'name' - команда для подключения к бд
# --------------------------------------------------

# Типы полей в Postgresql
# Numeric Types (числовые типы)
    # a. smallint(2 bytes) -> - 32767 to 32767:
    # b. integer(4 bytes) -> - 2.147 ... to 2.147...
    # c. bigint(8 bytes) -> - ....
    # d. real(4 bytes) -> - число с плавающей точкой, вещественной
    # f. double prectision(8 bytes) -> - real но только с двойной точностью
    # g. serial(4 bytes) -> - int, auto-increment
# -=-==-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-


# Character types(символы типы (сироковые)):
# a. varchar(кол-во символов)-> если мы 50 символов, а заполним только 10, то остальные будут свободны. Макс 255 

# b. char(кол-во символов)-> если мы 50 символов, а заполним только 10, то остальные будут пробелом. Макс 255

# c. text() -> неогр  кол-во символов


# boolean Type
#     a.boolen(1 bytes) - True/Folse


# date -> каленьдарная дата(год.мецес.день)

# location -> координатная точка (x,y)- (245, -12)

# enumerate types:
 #('a','b','c')
 # CREATE TYPE <any names> AS ENUM ('Hapi', 'Sad','Mad');
# ---------------------------------------------------------------
#  Ограничения :
# 1. NOT NULL - ОБЯЗАТЕЛЬНЫЙ К ЗАПОЛНЕНИНИЮ
# 2. UNIQUE - то что будеть храниться только уникальный данные 
# 3. CHEKC -> CHECK age > -1 - Огранечения проверки на условие
# 4. PRIMARY KEY (Для устоновки индетификаторы данных в таблице)
# 5. FOREIGN KEY(Для устоновки связей между таблицами)
# 6. ON DELETE - Для устоновки поведение при удаленнии данных которые были связыны  

# Создание бд
# CREATE DATABASE 'name'; # Имеит рекомендательный команд
# create database 'name';

# команда для создания таблицы
#  CREATE TABLE <tablename>(
    # <column> <type> [<constration>],
    # <column> <type> [<constration>],
# )

# CREATE TABLE films(
#     id serial,
#     code char(5),
#     title varcher (100),
#     date date,
#     genre varchar(50),
#     budget bigint,
#     country varchar(50)
# );

# DROPE TABLE <name> - удаление таблицы

# Команда для добавления данных в таблицу
# INSTERT INTO <tablename> (columns) VALUE (data),(data);

# INSERT INTO films(code, title,date,genre,budget,country) VALUES
# ('AU56', 'Game of Thrones', '2015-05-31', 10000000, 'fantazi', ''USA )

# команда для обновлнения данных
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>;

# UBDATE films SET genre = 'Adventure' всех изменяет
# UBDATE films SET genre = 'Adventure' WHERE code = 'AY56'; изминение однонг типа

# команда для удаления  данных

# DELETE FROM <table> WHERE <column> = <value>;
# ==========================================================

# ORDER BY: Позваляет нам сартировать выодящие данные по уьиваннию или возрастанию. ASC(по вазрастанию) и DESC(по убыванию)
# Синтаксис: SELECT <row> FROM <tablename> ORDER BY <row> [ASC/DESK]
# ===================================
# WHERE: Используется для фильтрации по полям.БУДУТ выводиться только те данные которое соотвествуют условию оператора WHERE
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> = 'чему либо';
# ================================

# BETWEEN- условые между 
# SELECT * FROM films WHERE id BETWEEN 3 and 8
# ================================

# LIKE- выводит результат который соотвествует введенному шоблону для строк.Чувствилен к регистру
# ILIKE : ТОЖЕ САМОЕ ТОЛЬКО НЕ ЗАВИСИТЬ ОТ РЕГИСТРА
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> LIKE/ILIKE 'Чему либо';

# ===============================
# экспорт бд (дамп):
# pg-dump -U <username> -d 'dbname'> 'file.sql'

#  Импорт:
# psql -U <username> -d <dbname> -f <filename>
# =========================================

# northwind_db= select count(product_name), c.category_name from products as p,categories as c
#  where p.category_id = c.catedory_id group by c.category_name;
# count | category_name  
# -------+----------------
#     12 | Beverages
#      5 | Produce
#     12 | Condiments
#      7 | Grains/Cereals
#      6 | Meat/Poultry
#     13 | Confections
#     10 | Dairy Products
#     12 | Seafood
# ==================================================
# northwind_db=# select product_name, category_id,  unit_price from products;
# northwind_db=# select *  from categories;
#  category_id | category_name  |                        description                         | picture 
# -------------+----------------+------------------------------------------------------------+---------
#            1 | Beverages      | Soft drinks, coffees, teas, beers, and ales                | \x
#            2 | Condiments     | Sweet and savory sauces, relishes, spreads, and seasonings | \x
#            3 | Confections    | Desserts, candies, and sweet breads                        | \x
#            4 | Dairy Products | Cheeses                                                    | \x
#            5 | Grains/Cereals | Breads, crackers, pasta, and cereal                        | \x
#            6 | Meat/Poultry   | Prepared meats                                             | \x
#            7 | Produce        | Dried fruit and bean curd                                  | \x
#            8 | Seafood        | Seaweed and fish                                           | \x
# (8 rows)
# ===============================
# northwind_db=# select product_name, unit_price, units_in_stock from products order by unit_price desc limit 3;
#       product_name       | unit_price | units_in_stock 
# -------------------------+------------+----------------
#  Côte de Blaye           |      263.5 |             17
#  Thüringer Rostbratwurst |     123.79 |              0
#  Mishi Kobe Niku         |         97 |             29
# ======================================
# northwind_db=# \dt
#                  List of relations
#  Schema |          Name          | Type  |  Owner  
# --------+------------------------+-------+---------
#  public | categories             | table | kanybek
#  public | customer_customer_demo | table | kanybek
#  public | customer_demographics  | table | kanybek
#  public | customers              | table | kanybek
#  public | employee_territories   | table | kanybek
#  public | employees              | table | kanybek
#  public | order_details          | table | kanybek
#  public | orders                 | table | kanybek
#  public | products               | table | kanybek
#  public | region                 | table | kanybek
#  public | shippers               | table | kanybek
#  public | suppliers              | table | kanybek
#  public | territories            | table | kanybek
#  public | us_states              | table | kanybek
# ================================
# Join; выборка данных  из двух таблиц соединние двух таблиц

# LEFT JOIN: ВЫБОРКА БУДЕТЬ СОДЕРЖАТЬ ВСЕ СТРОКИ ИЗ ПРАВОЙ ТАБЛИЦЫ

# SELECT p1.title,p1.price,o1quantity, p1.price * o1.quantani as total__sum FROM products p1, orders o1 WHERE p1.id = o1.product_id;
# -запрос сразу в две таблицы

#  SELECT p1.title, p1.price, o1.quantity, p1.pricce * O1.quantity as total_sum FROM products p1 JOIN orders o1 ON p1.id = o1.product_id;


