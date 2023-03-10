# obj = ["John", "Snow", 24, 500, "+79015670680" "Winterfell"]

# obj = {
# "name": "John", 
# "last name": "Snow", 
# "age":24, 
# "cash": 500, 
# "Phone number":"+79015670680"
# }

# print(obj["name"])

'------------------------------------------------------------------------------------------'

"DICTIONARY"

# dict() - Словарь -> упорядоченная коллекция элементов (python 3.7 -> ordered). Каждый элемент внутри словаря содержится в паре ключ: значение

# Ключи должны быт неизменяемым типом данных (str, int, tuple etc.) ,тогда как значениями могут вступать любые типы данных.


# thisdict = {
#   "brand":"Ford", 
#   "model": "Mustang", 
#   "year" : 1964
# }

# print(thisdict)
# print(type(thisdict))


# Ассоциативный массив, hash table, object(js),structure   = dictionary(py)



'--------------------------------------------------------------------'
# user_info = {"name": "John", "Last_name": "Snow", "age": 23, "email": "johnsnow@gmail.com", "role": "moderator"}
# print(user_info)

# user_info = {"name": "John", "Last_name": "Snow", "age": 23, "email": "johnsnow@gmail.com", "role": "moderator", "name": "Bastard"}
# print(user_info)
# print(user_info.get("name1")) #None
# print(user_info["name1"]) # Error

'--------------------------------------------------------------------'

# user_info = {

#     "name": "John",
#     "Last_name": "Snow",
#     "age": 23,
#     "email": "johnsnow@gmail.com", 
#     "role": "moderator"

#              }
    
# # print(dir(dict))
# print(user_info.values())
# print(user_info.keys())
# print(user_info.items())

# a = (1, 2, 3)
# print(a, type(a))
# num1, num2, num3= a
# print(num1) #1
# print(num2) #2
# print(num3) #3

# for x in user_info:
#     print(x) #получаем keys


# for x in user_info.values():
#     print(x) # мы получаем values


'-----------------------------------------------------'

# dict_ = {1: 15, 2: 11, 3: 18, 4: 5, 5: 21}
# print(dict_)
# for key, value in dict_.items():
#     if key % 2 == 0:
#         print(key, "четное")

#     else:
#         print(key, "нечетное")
#         dict_[key] = value** 2

# print(dict_)
  
'-----------------------------------------------'

# изменения словаря
# dict_ = {"name": "John", "age": 24}
# print(dict_)
# dict_["age"] = 23
# dict_["address"] = "Winterfell" (добавляет)
# dict_["address"] = "Moscow"
# print(dict_)

# dict_.update({"age": 18, "adress": "Bishkek"})
# print(dict_)

"-----------------------------------------------"
"FROM KEYS"

# fromkeys - быстрое создание словаря из ключей

# keys = ["one", "two", "three"]

# new_dict = dict.fromkeys(keys, "type")
# print(new_dict)


# dict_ = {}
# ls = list(range(1, 101))

# new_dict = dict_.fromkeys(ls, "type")
# print(new_dict)

# "OR"

# ls = list(range(1, 101))

# new_dict = dict.fromkeys(ls, "type")
# print(new_dict)


"---------------------------------------------------"

"SETDEFAULT"

#setdefault - работает так же как и метод get(), но если нет такого ключа, то он создаст новый.

# dict_ = {"name": "John", "age": 24}
# print(dict_)
# print(dict_.setdefault("age",35))
# print(dict_.setdefault("name"))
# print(dict_.setdefault("adress", "Moscow"))
# print(dict_)


"----------------------------------------------"

"POP, POPITEM"

#удаление из словаря
#pop(key) - удаляет элемент по ключу

# dict_ = {'name': 'John', 'last_name': 'Snow', 'Address': 'Winterfell'}
# print(dict_)
# dict_.pop("Address")
# print(dict_)


# dict_ = {'name': 'John', 'last_name': 'Snow', 'Address': 'Winterfell'}
# print(dict_)
# removed = dict_.pop("Address")
# print(removed)
# print(dict_)



"POPITEM"
#popitem() - удаляет последний элемент

# dict_ = {'name': 'John', 'last_name': 'Snow', 'Address': 'Winterfell'}
# print(dict_)
# removed = dict_.popitem()
# print(removed)
# print(dict_)

# #OR 
# key, value = removed
# print(key, value)


# roles = {
#     0: "moderator",
#     1: "Admin",
#     2: "customer",
#     3: "Vendor"
        
# }

# users = {
#     "1": {"username": "John Snow", 'role': roles[1]},
#     "2": {'username': "JamieLanister", "role": roles[2]},
#     "3": {'username': "Mufasa", "role": roles[3]}


# }

# product = {
#     "id": 1,
#     "title": "Iphone 14 Pro Max",
#     'description': "Lorem Ipsum",
#    'price': 200
# }
# x = 0
# while x < 3:
#     i = input(("Enter smt:\n Если хотите просмотреть товар то нажимите 1\n Если хотите изменить товар то нажимите 2 \n Если хотите выйти то нажмите 3 или что то другое\n Ваш выбор"))

#     if i =="1":
#         print(product)

#     elif i =="2":
#         id_user = (input('\n Введите ваш id: '))
#         if not users.get(id_user):
#             print('Нет твкого юзера!')
#         elif users.get(id_user)["role"] == roles[1]:
#             print(users.get(id_user))
#             choice = input('Введите что изменить (title,description,price): ')
#             new = input(f'Введите новое значение {choice}: ')
#             product.update({choice:new})
#             print("Updated!")
#         else:
#             print (users.get(id_user))
#             print("Сори только админ может редактировать! У тебя нет разрешения")


# roles = {0: 'Moderator', 1: 'admin', 2: 'Custemer', 3: 'vendor'}

# users = {
#     '1': {'username': 'johnsnow', 'role': roles[1]},
#     '2': {'username': 'Jamielanister', 'role': roles[2]},
#     '3': {'username': 'Mufasa', 'role': roles[3]}
#  }


# product = {
#     'id': 1,
#     'title': 'Iphone 14 pro max',
#     'descripton': 'Lorem Ipsum',
#     'price': 200
#  }

# x = 0
# while x < 3:
#     i = input('Введите что хотите сделать:\nЕсли хотите просмотреть товар то нажмите 1\nЕсли хотите изменить товар то нажмите 2\Если хотите выйти то нажмите 3 или что то другое\nВаш выбор: ')

#     if i == '1':
#         print(product)
#     elif i == '2':
#         id_user = input('\nВведите ваш id: ')
#         if not users.get(id_user):
#             print("Такого юзера нету")
#         elif users.get(id_user)['role'] == roles[1]:
#             choice = input('Введите что изменить(title,description, price): ')
#             new = input(f'введите новое значение {choice}: ')
#             product.update({choice:new})
#             print('Updated')
#         else:
#             print(users.get)(id_user)
#             print('Сори только админ может редактировать! У тебя нет разрешение')




# print(dir(dict))

def func17(list_):

employees = [
  {'name': 'Jack', 'salary': 10000, 'overTime': 4},
  {'name': 'Tom', 'salary': 15000, 'overTime': 3},
  {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
  {'name': 'Helen', 'salary': 25000, 'overTime': 2},
  {'name': 'Peter', 'salary': 30000, 'overTime': 7}
]

for x in employees:

