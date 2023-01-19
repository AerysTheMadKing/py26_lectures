# Встроенные функция 
# 1) map
# 2) filter
# 3) lambda
# 4) enumerate
# 5) zip, all, any
# 6) (reduce)

# Анонимные функции - lamda, (такие же функции только без названия)

# lamda функции могут принимать сколько угодно аргументов, но всегда возвращают одно выражение.

# def sum_of_args(a, b):
#     res = a + b
#     return res

# print(sum_of_args(1, 2))

# a = sum_of_args
# print(a(5, 15))

# sum_of_args2 = lambda a, b: a + b
# print(sum_of_args2(2, 3))

# x = lambda a, b, c: (a * b) % c

# print(x(11, 5, 10))

# get_last = lambda ls: ls[-1]
# ls = [1,2,3,4,5,True, False, [123]]
# print(get_last(ls))


# def my_func(n):
#     return lambda a: a*n

# myDoubler = my_func(2)
# myTripler = my_func(3)
# print(myDoubler(50))
# print(myDoubler(100))
# print(myDoubler(20))
# print(myTripler(22))

# dict_ = {"john": 600, "Sultan": 500, "Sansa": 200, "Adil": 400}

# result = sorted(dict_.items(), key = lambda x: x[1])

# print(result)


"-----------------------------------------------------------------------"

"MAP"

# map(function, iterable) - применяет функцию к каждому элементу из последовательности и возвращает mapobject(итератор) с результатом.

# >>>>> так писать плохо
# ls = ["one", "two", "three", "four", "five"]

# for i in range(0, len(ls)):
#     ls[i] = ls[i].upper()

# print(ls)


# >>>> хорошо
# ls = ["one", "two", "three", "four", "five"]

# res = list(map(str.upper, ls))
# print(res)




# names = ["Sultan", "Jamie", "john", "Sansa"]

# res = list(map(lambda name: f"Hello mr/mrs {name}", names))
# print(res)


# dict_ = {1:2, 3:4, 5:6, 7:8}  #{1:"2", 3:"4", 5:"6", 7:"8"} 

# for k in dict_:
#     dict_[k] = str(dict_[k])

# print(dict_)


# dict_ = {1:2, 3:4, 5:6, 7:8}  #{1:"2", 3:"4", 5:"6", 7:"8"} 

# res = dict(map(lambda x:(x[0], str(x[1])), dict_.items()))

# print(res)


"--------------------------------------------------------"
"FILTER"

#filter(function, iterable) -> применяет ко всем элементам iterable функция которую мы передали и возвращает итератор с теми элементам для которых функция вернула True

# ls = ["one", "two", "three", "four", "five", "100", "1", "John"]
# res = []
# for x in ls:
#     if x.isdigit():
#         res.append(x)

# print(res)

# res = list(filter(str.isdigit, res))
# print(res)


# ls = ["John", "makers", "three", "four", "mountain", "bootcamp", "1", "Snow"]
# res = list(filter(lambda stroka: len(stroka) > 5, ls))
# print(res)

# ls = [
#     {"name": "python", "point": 10},
#     {"name": "C++", "point": 7},
#     {"name": "Java", "point": 5},
#     {"name": "Js", "point": 3},
#     {"name": "C#", "point": 0}

# ]

# res = list(filter(lambda dict_: dict_["point"] >= 7,ls))
# print(res)

# users = [
#     {'username':'John', 'comments':['I love you', 'Really good']},
#     {'username':'Raychel', 'comments':[]},
#     {'username':'Steven', 'comments':['Bishkek', 'Python']},
#     {'username':'Hello', 'comments':[]},
#     {'username':'Kira', 'comments':['The best post']}
# ]


# inactive_users = list(filter(lambda x: not x['comments'], users))
# print(inactive_users)

"-------------------------------------------------------------------------"

# names = ["Raychel", "Sultan", "Aigerim", "John", "Bob", "Kira"]

# new_names = list(
#     map(
#         lambda name: f"Your name is {name}!",
#         filter(lambda x: len(x)> 4, names))
# )
# print(new_names)

# from functools import reduce


# ls = [1,2,3,4,5]
# sum  = reduce(lambda a,b:a+b, ls)
# mult  = reduce(lambda a,b:a*b, ls)
# print(sum)
# print(mult)


"----------------------------------------------------------------------"
"ENUMERATE"

# ls = ["John", "Sultan", "Katana", "Aigerim"]
# for i, obj in enumerate(ls):
#     print(i, obj)

# import string as s
# import random

# def generate_rand_str():
#     symbols = s.ascii_letters + s.digits
#     res = ''.join(random.choice(symbols) for i in range(0, 10))
#     return res

# print(generate_rand_str())
# print(generate_rand_str())
# print(generate_rand_str())
# print(generate_rand_str())
# print(generate_rand_str())


"-------------------------------------------------------"
# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat

# symbols = "_()$+-%!@#"
# q_pass = int(input("Введите количество паролей: "))

# res = {
#     f(choices(ascii_letters, k = 10), choices(digits, k = 5), choices(symbols, k = 2))
#     for f in repeat(lambda a ,b, c: ''.join(set(a+b+c)), q_pass)
# }
# print(res)
# print(f"Quantity of password: {len(res)}")

# from statistics import mean

# dlina = [len(x) for x in res]
# print(f"Average len: {mean(dlina)}")

"-------------------------------------------------------------------------"

"ZIP"

# zip(iterable)- Она соединяет каждый элемент итерируемых обьектов между собой, по их, распорядку,в тип данных tuple и возвращает его.

# ls = [1,2,3,4,5]
# ls2 = [6,7,8,9]
# res = list(zip(ls,ls2))
# print(res)

# ls1 = [1,2,3]
# ls2 = [4,5,6]
# ls3 = [7,8,9]

# res = list(zip(ls1, ls2, ls3))
# print(res)


# Zip для создания словарей 

# a = dict([(1, 2), (3, 4)])
# print(a)


# d_keys = ["hostname", "location", "vendor", "model", "IOS", "IP"]

# d_values = ["apple_r1", "Winterfell", "Jobs", "watch", "16.0", "10.23.4"]

# result = dict(zip(d_keys, d_values))
# print(result)



# d_keys = ["hostname", "location", "vendor", "model", "IOS", "IP"]

# data = {
#     "r1": ["londone_r1", "New York", "Boston", "Chicago", "Rhode Island"],
#     "r2": ["londone_r2", "Illinoise", "Houston", "Bishkek", "Osh"],
#     "r3": ["londone_r3", "Italia", "Germany", "Australia", "Turkey"],
# }
 
# print(data)
# for k in data:
#     data[k] = dict(zip(d_keys, data[k]))
#     print()
#     print(data)



"---------------------------------------------------------------------------"

"ALL", "ANY"

#all(iterable) -  Возвращает True, если все элементы внутри обьекта истина, иначе возвращает False.


# all([1,2]) -> True
# all([[]])-> False
# all(["False", "john", 5,6,7]) -> True
# all([[1,2,3], 5, None])-> False


# ip = "10.10.10y.10"
# result = all(x.isdigit() for x in ip.split("."))
# print(result)


#any(iterable)- возвращает True, если хотябы один элемент истина.

# ls = [0,0,0, "", False]
# print(any(ls)) #False

# ls = [0,0,0, "", False, 1]
# print(any(ls)) #True


# ignore = ["rm-rf", "reset", "alias"]
# command = input("Введите команду: ")

# if any(x in command for x in ignore):
#     raise Exception("Invalid coomand")

# print("Vse ok!")




























