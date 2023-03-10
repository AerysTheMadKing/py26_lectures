# -----------------------------ПРАКТИКА -----------------------------
# СОЗДАНИЕ ТАБЛИЦ
#1. create table blogger (
# test_db(id serial primary key,
# test_db(name varchar(50));

#2. create table post(
# id serial primary key,
# owner_id int references blogger (id),
# body text,
# created_at date);

# ЗАПОЛНЕНИЕ ДАННЫХ

#1.INSERT INTO blogger (name) VALUES 
# test_db-# ('John'), ('Sultan katana'), ('Jamie');

#2.insert into  post(owner_id, body, created_at) values
# (1, 'my first blog post! Hello world!', '2023.02.24'),
# (1, 'today is a good dat!', '2023.01.01'),
# (1, 'it is my bad-bad day', '2022.02.24');

#3.insert into  post(owner_id, body, created_at) values
# (3, 'Lanister always pays his debts!', '2023.02.24'),
# (3, 'I will be back!', '2023.01.01');

# 4.insert into  post(owner_id, body, created_at) values
# (2, 'I\m hungry!', '2023.02.24');

# shop
# 1.create table customer(
# test_db(# id serial primary key,
# test_db(# name varchar(50));

# 2.create table product(
# id serial primary key,
# title varchar(50),
# test_db(# price decimal);


# 3.create table cart (
# (# id serial primary key,
# (# customer_id int references customer(id),
# (# product_id int references product(id));


# заполнение таблиц


# 1.insert into product(title, price) values ('kks', 340),
# ('iphone 14', 70000),
# ('patato', 200),
# ('Ananas', 470),
# ('Ice-cream', 120);
# INSERT 0 5

# # 2.insert into cart(customer_id, product_id) values
# (1,1), (1,1), (1,1), (1,3), (1,3),
# (2,2), (2,2), 
# (3,4), (3,5);

# Агрегатные функции

# SUM - функция. которая считывающая сумму всех записей в с группированном поле

# ПРИМЕР ИЗ shop

# SELECT c.name, SUM(p.price) AS total price

# FROM product AS p JOIN cart ON p.id = cart.product_id
# JOIN customer AS c ON c.id = cart.customer_id GROUP BY c.name;

#ARRAY_AGG - обьединяет записи сгруппиррованного поля в массив.

# SELECT b.name, ARRAY_AGG(post.body) as posts from blogger AS b JOIN post ON b.id = post.owner_id GROUP BY b.name;


#----------------------------------------------------------------------
# Shakerspeare

# 1. Вытащить все произведения в котрых sourse = Moby и кол-во параграфов меньше 100

# SELECT title, source, totalparagraphs from work WHERE source = 'Moby' And totalparagraphs < 100;

# 2. Найти кол-во глав в каждом произведении.

# SELECT COUNT(*), work.title FROM chapter JOIN work ON work.workid = chapter.workid GROUP BY work.title ORDER BY COUNT(*) DESC

# 3. Найти сколько произведений относятся к каждому жанру.

# SELECT COUNT(*), genretype from work GROUP BY genretype ORDER BY count;

# 4.Найти кол-во параграфов в каждом произведении и вытащить названия произведений

# SELECT title, totalparagraphs FROM work;

# 5. Вытащить имена героев, чьи реплики состовляют больше 200 слов, также произведения в которых они встречаються, жанр, год выхода произдведения в порядке убывания

# SELECT ch.charname, MAX(ch.speechcount), ARRAY_AGG (work.title) FROM character_work AS ch_w JOIN character AS ch ON ch_w.charid = ch.charid JOIN work ON ch_w.workid = work.workid WHERE ch.speechcount> 200 GROUP BY ch.charname ORDER BY MAX(ch.speechcount) DESC LIMIT 10;


# 6.Вытащить героя, который чаще всех появляется в произведениях.

# SELECT ch.charname, COUNT(*) AS works_count FROM charcater_work AS ch_w JOIN character AS ch ON ch.charid = ch_w.charid 




