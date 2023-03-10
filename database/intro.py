# PostgreSQL - Система управления базами данных (СУБД/DBMS)

# Это ряд программ и инструментов позволяюхщих создавать БД, управлять ею и манипулировать данными внутри БД(CRUD).

# Postgres - Сама база данных, она реалиционная, то есть данные храняться в виде таблиц и таблицы имеют связи между собой (relation).


# SQL(Structured Query Language) - Декларативный язык структурированных запросов, он применяется для создания и управления данными.


#---------------------------------------------
# Типы полей в Postgres

# 1) Numeric types:

#     a. smallint (2 bytes) -> -32767 to 32767
#     b. integer(4 bytes) -> -2147000 to 2147000
#     c. bigint(8 bytes) -> ...
#     d. serial (4 bytes) -> auto-increment(integer, 1-2147000)
#     e. real(4 bytes) - число с плавающей точкой, вещественные число.
#     f. doubleprecision(8 bytes) -> real но только с двойной точностью.


# 2)Character types:

#     a. varchar(кол-во 255) - можем указать макс кол-во символов в ручную. Если мы указали мак кол-во символов в 50, а заполнили только 10, то остальные 40 не заполнятся.
#     b. char(255) - если не заполним все символы то остальные заполняться пробелами.
#     c.text - неограниченное кол-во символов.

# 3)Boolean types

#     boolean (1 bytes) -> True/False

# 4)date - календарная дата(год.месяц.день)

# 5)location - координатная точка -> (245, -12) (x, y)





#-------------------------------------------------------

# Связи между таблицами (relations)

    # 1. Один к одному (One - to - One)  - Человек пасспорт
    # 2. Один к многим (One - to Many) - Человек и банковские карты 
    # 3. Много к многим (Many - to - Many) - Студенты и преподы

# # constraints(ограничения):
# 1). CHECK   <column> > 5 - порверка данных по условию
# 2). UNIQUE   ->  только уникальные значения
# 3). NOT NULL   ->  обязвтельно к заполнению
# 4). PRIMERY KEY   ->  для установки идентификатора данных в таблице.
# 5). FOREIGN KEY   ->  для установки связи между таблицами.
# 6). DEFAULT<value> ->  добавляет дефолтное значение.  

# # Добавление
# ALTER TABLE cities ADD CHECK(name <> '');
# ALTER TABLE cities ADD CONSTRAINT <name_of_constr> UNIQUE (name);
# ALTER TABLE cities ALTER COLUMN location SET NOT NULL;
#---------------------------------------------------------

#Вход
#ubuntu - sudo -u postgres psql

# psql - для входа через своего юзера

# \q - выход из СУБД

# \du - список всех юзеров

# \l - список все баз данных

# \с <dbname> -> команда для подключения к БД 
#     \dt -> список таблиц в БД
#     \d -> <table name> -> подробная информация про таблицу.NameError

# ИМПОРТ данных при помощи файла.
# psql -U <username> -d <database> -f <path_to_file>

#CREATE DATABASE <dbname>; -> команда для создания бд
# DROP ... -> удаление

# CREATE TABLE <tablename> (
# <name_of_column> <type>,
# <name_of_column> <type>); команда для создания таблицы.

# DROP DATABASE <name_of_db>; - удаление бд.

# DROP TABLE <name_of_table>; - удаление таблицы.

# INSERT INTO <tablename> (<columns>) VALUES (datas_to_columns); - команда для заполнения данных в таблицу.

#INSERT INTO cities (name, location) VALUES ('Tokmok', '(43, 76.42)');

# UPDATE <tablename> SET <row> = <new_value>
# WHERE <row> = <value>; - команда для обнавления данных Указываем после WHERE то какой обьект обновить.

# DELETE FROM <tablename> WHERE <column> = <data>;- команда для удаления.

# CREATE USER <username> WITH PASSWORD '<password>'; -> команда для создания юзера.

# ALTER USER <username> WITH SUPERUSER; команда для изменения статуса юзера на суперюзера.

#SELECT = <column> FROM <table> команда для получения данных


#WHERE: используется для филтрации по полям. будут выводиться только те данные которые соответствуют условию WHERE.

# Синтаксис: SELECT: <row> FROM <tablename> WHERE <row> = 'чему либо'

# SELECT * FROM products WHERE meat = 'Becon';
# SELECT * FROM products WHERE meat in ('Becon', 'Beef');

#AND: оператор и, для множества условий
# 
# операторы сравнения: >, <, <=, >=, =, <>
# 
# BETWEEN: условие между
# 
# SELECT * FROM product WHERE id BETWEEN 3 and 8; 
# SELECT * FROM product WHERE id <= 8 and id >= 8;

#ORDER BY: сортировка по входящим данным по убиванию или возрастарию.

    #ASC(по возрастанию) и DESC(по убыванию)

# SELECT <row> FROM <table> ORDER BY <row> [ASC/DESC];

# LIMIT: Позволяет нам вернуть данные в ограниченном кол-ве

# SELECT <row> FROM <table> LIMIT 1;

# LIKE: Выводит результат который сооветствует введеному шаблону. Зависит от регистра.

# I LIKE: не зависит от регистра

# Синтаксис: SELECT * FROM products WHERE name LIKE 'S%';

# DISTINCT: Позволяет нам убрать дубликаты и возвращаеть только уникальные значения.
# 
# SELECET DISTINCT name FROM products;


#------------------------------------------------------------------

# JOIN - это специальный оператор позволяет в запросах селект брать данные из нескольких таблиц

# INNER JOIN() - достаются только те записи, у которых есть связь.

# FULL JOIN() - достаются все записи с обеих таблиц.

# LEFT JOIN() - достает все записи с левой таблицы, а с левой правой те записи у которых есть связь с левой таблицей.

# RIGHT JOIN() - достает все записи с правой таблицы, а с левой только те записи у которых есть связь с правой таблицей.

# * где "левая" таблица это та таблица которая записана до join, a 'правая' таблица которая записана после join.




