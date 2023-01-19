# 3)QUESTION
# name_of_list = ["Helloworld!"]
# new_str = name_of_list[0]
# new_str = name_of_list[0][6:12] + name_of_list[0][0:6]
# new_list = list(new_str)
# print(new_list)


# 5)QUESTION
# name = ['футболка', 'шорты', 'сланцы', 'очки', 'кепка'] 
# suitcase = []
# for x in name:
#     print(x)
#     suitcase.append(x)

#     pop_element = suitcase.pop()
#     print(pop_element)

# suitcase.insert(0,"панама")
# print(suitcase)


# 1) Создайте словарь university, и заполните данными, которые бы отражали количество учащихся на разных факультетах (программирование, экономика, медицина). Внесите изменения в словарь согласно следующему: а) в одном из факультетов изменилось количество учащихся, б) в университете появился новый факультет(лингвистика), с) в университете был расформирован (удален) другой факультет (медицины). Вычислите общее количество учащихся в университете.


# dict_  =  {1: "a", 2: "b", 3: "c"}
# dict1 = {}
# for key, val in dict_.items():
#   dict1 = dict1.update({val:key})
#   print(dict1)

# obj = ["John", "Snow", 24, 500, "+79015670680" "Winterfell"]

# obj = {
# "name": "John", 
# "last name": "Snow", 
# "age":24, 
# "cash": 500, 
# "Phone number":"+79015670680"
# }

# print(obj)
# print(obj["name"])



# dict_ = {'name': 'John', 'last_name': 'Snow', 'Address': 'Winterfell'}
# print(dict_)
# dict_.pop("Address")
# dict_.pop("name")
# dict_.pop("last_name")

# print(dict_)

#3)question
# a = {'a': 1, 'b': 2, 'c': 1}
# print(a)
# a.pop("a")
# a.pop("b")
# a.pop("c")

# print(a)


# obj = ["John", "Snow", 24,5, 500, "+79015670680" "Winterfell"]

# obj = {
# "name": "John", 
# "last name": "Snow", 
# "age":24.5, 
# "cash": 500, 
# "Phone number":"+79015670680"
# }

# print(obj["name"])


# name_of_list = ["Helloworld!"]
# new_str = name_of_list[0]
# asap = (len(new_str))
# asap = new_str[0][6:12] + new_str[0][0:6]
# # new_list = list(new_str)
# print(new_str)






# new_str = name_of_list[0][6:12] + name_of_list[0][0:6]
# new_list = list(new_str)
# print(new_list)

   

# tilek = {"Dodo", "ImperiaPizza", "FreshBox"}
# timur = {"OchakKebab", "FreshBox"}
# alexander = {"FreshBox", "KFC"}
# elina = {}
# a = tilek.intersection(timur, alexander)
# if tilek.intersection(timur, alexander):
#     print(a)

# ingredients = {"cыр чеддар","грибы", "соус","шпинат"}
# ingredients.add("помидор")
# ingredients.discard("колбаса")
# ingredients.remove("шпинат")
# ingredients.add("базилик")
# ingredients.update({"cыр чеддар", "сыр моцарелла"})
# print(ingredients)


# x = int(input("Enter smt: "))
# y = int(input("Enter smt: "))

# if x % y == 0:
#     print('x делится на y')
#     print(f"Частное: {x//y}")

# else:
#      print('x не делится на y')
#      print(f"Частное: {x//y}")
#      print(f'Остаток: { x % y}')




# string = 'abracadabra'
# a = string[5]
# c = string.remove(a)
# print(c)



# hashtags = '#makers#bootcamp#программирование#it#курсы'
# c = hashtags.replace("#", " ")
# print(c.split())


# a = (input("Enter number: "))
# b = (input("Enter number: "))
# c = (input("Enter number: "))

# if (a*2 == b*2+c*2) or (b*2 == a*2+c*2)or (c*2 == b*2+c*2):
#     print("rectangular")

# elif (a*2 < b*2+c*2) or (b*2 < a*2+c*2)or (c*2 < b*2+c*2):
#     print("acute")

# elif (a*2 > b*2+c*2) or (b*2 > a*2+c*2)or (c*2 > b*2+c*2):
#     print("obtuse")

# else:
#     print("imposible")

# 
# string = input()
# if len(string) > 5:
#     print("True")

# else:
#     print("False")




# x = int(input())
# y = int(input())

# if x % y == 0:
#     print("x делиться на y")
#     print(f"Частное:{x//y}")

# else:
#     print("x не делиться на y")
#     print(f"Частное:{x//y}")
#     print(f"Остаток:{x%y}")
    

# suitcase = []
# suitcase.append('футболка')
# suitcase.append('шорты') 
# suitcase.append('сланцы') 
# suitcase.append('очки') 
# suitcase.append('кепка')
# suitcase.pop()
# suitcase.insert(0, 'панама')

# print(suitcase)

# list1 = [11, 23, 45, 7, 9]
# list2 = [21, 4, 16, 8, 10]
# list1.extend(list2)
# print(sum(list1))
       
# 11)question

# list_ = range(0,102,2)
# print(list(list_))


# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# for x in a.values():
#     a.append(x/5)




# name_of_list = ["Helloworld!"]

# new_st1 = name_of_list[0][6:12]
# new_str2 = name_of_list[0][0:6]
# name = (new_st1+new_str2)
# new_list = list(name)
# print(new_list)

# 17)question #list
# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# tuples.remove(())
# tuples.pop(1)
# cleared_tuples = tuples
# print(cleared_tuples)

# 21)question
# str_list = ['abc', 'xyz', 'aba', '1221']
# indexs = []
# a = str_list[0]
# b = str_list[1]
# c = str_list[2]
# d = str_list[3]
# if a[0] == a[1]:
#     indexs.append(a)

# elif b[0] == b[-1]:
#     indexs.append(b)

# elif c[0] == c[-1]:
#     indexs.append(c)

# elif d[0] == d[-1]:
#     indexs.append(d)

# print(indexs)



# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# a = len(lists[0])
# b = len(lists[1])
# c = len(lists[2])
# d = len(lists[3])
# e = len(lists[4])

# f = max(a, b, c, d, e)
# print(f)

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = list(filter(None,tuples))
# print(cleared_tuples)


# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# name = list(filter(None, tuples))
# print(name)





# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {}
# for k, v in a.items(): 
#     if v%2==0:
#         b.setdefault(k, 2) 
#     else:
#         b.setdefault(k,v) 
        
# print(b)

# a = {'apple': 2, 'orange': 5, 'banana': 10} 

# for k, v in a.items():
#     if v % 2 == 0:
#         a.pop("apple")

# print(a)


# print(dir(dict))


    
# a1 = {"a": 1,"b": 2,"v": 3}
# a2 = dict(a=1, b=2, c=3)
# a3 = {}

# for k,v in a1.items():
#     a3.setdefault(k, v)


# print(a1)
# print(a2)
# print(a3)

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# dict1 = {}
# for x in dict_.values():
#     dict1.setdefault(x)

# print(min(dict1))



# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# dict2 = {}
# for k,v in dict1.items():
#     if  v % 2 != 0:
#         v = 1
#     dict2.setdefault(k, v)

# else:
#     dict2.setdefault(k,v)

# print(dict2)

# 22)question
# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# dict1 = {}
# for k, v in dict_.items():
#     if v == None:
#         dict1.setdefault(k,v)
# print(dict1)

# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# list1 = {}
# list2 = {}
# dict_ = {}

# for x in list:
#     if type(x) == str:
#         list1.append(x)

#     if type(x) == int:
#         list2.append(x)

#         dict_ = dict(zip(list1,list2))
# print(dict_)


# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = (input("Enter smt: "))
# if key in dict_:
#     print("Key is present in the dictionary")  

# else:
#     print("key is not present in dictionary")



# print(dir(dict))




# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = {}

# for i in range(len(list1)):
#         print(i)

#     dict_[list1[i]] = list2[i]

# print(dict_)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 

# new_list = [x == "shorter" if len(x) <= 4 else "longer" for x in list_name]
# print(new_list)


# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k: list(range(1,v+1)) for k, v in a.items()}
# print(dict_)


# 14 )question

# dict_ = {

# 'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}

#         }


# dict1 = {k: max(v) for x in dict_ for k, v  in dict_.items() }
# print(dict1)


# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x-x+1 for x in list_ if x < 0]
# print(int_list)

# list_ = [x for x in range(1,100,125) if x % 2 == 0 ]
# print(list_)

# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list1 = [y for k,v in dict_.items() for x,y in v.items()]
# print(list1)

# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

# dict2 = {k.replace("i",""):k.count("i") for k, v in dict1.items()}
# print(dict2)

# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]

# list_ = [x[0] for x in SPL_Patrons if x[1] > 100]
# print(list_)

# 32) question
# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# saved_amount = [x[1]*11.95 for x in SPL_Patrons]
# print(saved_amount)



# 33 question
# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]

# list_ = [x[1]*42 if x[2] == True else x[0]  for x in prairie_pirates ]
# print(list_)


# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(x)for x in str_list]
# print(int_list)


# 14 )question


# dict_ = {

# 'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}

#         }


# dict1 = {k: max(v) for x in dict_ for k, v  in dict_.items() }
# print(dict1)


# #case 1
# path = 8
# steps = "UDDDUDUU"
# result = 1

# #case 2
# path = 10
# steps = "DUDDDUUDUU"
# result = 2

#case 1


# path = 8
# steps = "UDDDUDUU"


# sea_level = 0
# valleys = 0

# for step in steps:
#     if step == "U":
#         sea_level+=1
#         if sea_level == 0:
#             valleys += 1
#     elif step == "D":
#         sea_level -=1

# print(f"Result: {valleys} count!")



# 1)Question
# num1 = input('Enter num: ')
# num2 = input('Enter num: ')
# try:
#     num1 = int(num1)
#     num2 = int(num2)
#     print(num1+num2)
# except:
#     num1 = str(num1)
#     num2 = str(num2)
#     print(num1+num2)

# 2)question

# dict_ = {1:"Asylbek", 2:"Aybek", 3:"Ali"}

# try:
#     dict1 = input("Enter username: ")
#     if dict1 in dict_.values():
#         for k, v in dict_.items():
#             if v == dict1:
#                 print(f"Hi {v}, your ID is {k}")

#     else:
#         raise Exception()

# except:
#         print("Введенного юзера нет в базе данных!")

# finally:
#     print("Спасибо!")

# 3)question
# try:
#     age = int(input("Enter your age: "))

#     if age > 0:
#         print(f"Hello your age is {age}")

#     if age <= 0:
#         raise Exception()

    
# except:
#     print("Ваш возраст должен быть больше 0")


# try:
#     cash = int(input())
#     if cash < 0:
#         raise Exception("ValueError")
#         print(cash)

# except:
#     print("Сумма не может быть отрицательной! ")

# list_ = [1, 2, 3]
# try:
#     a = list_.get(4)
#     print(a)
# except AttributeError:
#     print("Incorrect method")

# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     print(dict_['key2'])

# except:
#     print("Нет такого ключа!")


# try:
#     age = int(input())  
#     if age < 18:
#         raise Exception (ValueError,ValueError)
        
# except ValueError:
#     print("Доступ запрещён")

# except ValueError:
#     print("Введён некорректный возраст")


# else:
#     print("Спасибо")

# finally:
#     print("До свидания!")




# try:
#     age = int(input())  
#     if age < 18:
#         raise ValueError
        
        

# except ValueError:
#     print("Доступ запрещён")

# except:
#     print("Введён некорректный возраст")


# else:
#     print("Спасибо")

# finally:
#     print("До свидания!")

# try:
#     password = "12345"
#     if len(password) < 6:

#         raise ValueError
    
# except ValueError:
#     print("Error")


# password = "short"
# try:
    
#     if len(password) < 6:
#         raise ValueError
    
# except ValueError:
#     print("Error")

# else:
#     print(password)


# 14)question
# try:
#     password = "12345"
#     if len(password) < 6:
#         raise ValueError

# except ValueError:
#     print("Not found")

# else:
#     print("Correct")

# try:
    # import lamabimgo


# except:
#     print("Такого модуля нет")







# num = 100000000
# i = 1
# while num -i == i :
#         i-=1
#         print(i)

# try:
#     num = 100000000
#     i = 0
#     while i >= num:
#         i+=1

# except KeyboardInterrupt:
#     print("Nope")



# try:
#     age = int(input())  
#     if age < 18:
#         raise ValueError
        
        

# except ValueError:
#     print("Доступ запрещён")

# except:
#     print("Введён некорректный возраст")


# else:
#     print("Спасибо")

# finally:
#     print("До свидания!")


# try:
#     age = int(input())  
#     if age < 18:
#         raise ValueError
        
# except ValueError:
#     print("Доступ запрещён")        



# except:
#     print("Введён некорректный возраст")




# else:
#     print("Спасибо")

# finally:
#     print("До свидания!")


    
    




# def sum(a, b): 
#     return a + b
 
# sum(2, 3) 
# print(sum(2, 3))


# def is_palindrome(str)-> bool:
#     for x in str:
#         if x == x[::-1]:
#             return True

#         else:
#             return False

# print(is_palindrome("apple"))

# print(dir(str))

# def is_palindrome(words:list[str])-> bool:
#     for x in words:
#         if x == x[::-1]:
#             return True

#         else:
#             return False

# print(is_palindrome(["Apple"]))



# def is_palindrome(words:str)-> bool:
#     for x in words:
#         if x == x[::-1]:
#             return True

#         else:
#             return False

# print(is_palindrome("Apple"))

# def is_palindrome(str):
#     if str.upper() == str.upper()[::-1]:
#         return True

#     else:
#             return False

# print(is_palindrome("Mom"))

# def multiply_list(list_): 
#     n = 1 
#     for i in list_: 
#         n *= i 
#     return n 
    
# print(multiply_list([1, 2, 3, 4, 5, 6]))

# def func12(list):
#     for x in list:
#         return x.lower()

# print(func12(["hEllo", "wORld"]))


# list1 = ["hEllo", "wORld"]
# for x in list1:
#     print(x)

# 13)Question

# def func13(str):
#     return "Hello"-> {f'H':str.count("H"), 'e': str.count("e"), 'l':str.count("l"), 'o': str.count("o")}
        
       

# print(func13("Hello"))

#>>>>>>>>>>>>>

# def func16(num1, num2):
#     return {f"На {num1}км было расходовано {num2}л горячего"}

# print(func16(100, 10))


# def sum_digits(num):
#     return str(num)

# print(sum_digits((105)))

# >>>>>>>>>>>>>>>>>>>>12(QUESTION)

# def func12(words:list(str)):
#     # ls = []
#     # for x in words:
#     #     a = x.upper()
#     #     ls.append(a)

#     return list(x.lower() for x in words)

# print(func12(["hEllo", "wORld"]))

# >>>>>>>>>>>>>>>>>>>>13)(QUESTION)


# def func13(str):
#     return  {f'H':str.count("H"), 'e': str.count("e"), 'l':str.count("l"), 'o': str.count("o")}
        
       

# print(func13("Hello"))


# def func13(str):
    
#     return {x:str.count(x) for x in str}
        
       
# print(func13("Hello")) 


# def func12(words):
#     return list(x.lower() for x in words)

# print(func12(["hEllo", "wORld"]))


# def add(a, b): return a + b

# def subtract(a, b): return a - b

# def multiply(a, b): return a * b

# def divide(a, b): return a / b


# def calc(num1,num2, operation):
#     if operation == "+":
#         return add(num1, num2)
#     elif operation == "-": 
#         return subtract(num1, num2)

#     elif operation == "*": 
#         return multiply(num1, num2)

#     elif operation == "/": 
#         return divide(num1, num2)



# print(calc(40, 20, operation = "+"))

# def func12(words):
#     return list(x.lower()for x in words)

# print(func12((["hEllo", "wORld"])))

# str_ = 'IT-backend developer'
# str1 = str_.startswith("IT")
# print(str1)


# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]

# a = (users[0]["work"])

# b = a.startswith("IT")
# print(b)


# 15 question
# def func15(users):
    
#     for x in users:
#         for k ,v in x.items():
#             if k == "name":
#                 b = v
#         for k, v in x.items():
#             if k == "work":
                
#                 if v.startswith("IT"):

#                     print(f"{b}, скидки в магазине компьютерной техники!")


                    
# func15(users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ])
# Внесите изменения в функции bar таким образом чтобы при вызове функции foo и при попытке распечатать переменную var в глобальной области видимости, выводился следующий результат:

# var = 'переменная в foo' 
# def foo(): 
#     global var 
#     var = 'переменная foo' 
#     print('переменная в foo: ', var) 
#     def bar(): 
#         global var 
#         var = 'переменная bar' 
#     bar() 
# foo() 
# print('переменная в foo: ', var)

# def func16(a ,b):
#     return (f"'На 100км было расходовано {a/b} горючего'")

# print(func16(20,5))


# x =  "Я глобальная переменная!"
# def my_func():
#     global x
#     print(x)
#     x = "Я могу изменяться"
    
    

# my_func()
# print(x)

# var = 100
# def increment():
#     global var
#     print(var)
#     var += 1

# increment() 
# print(var)

# num = 3
# def mul():
#     global num
#     num = num**2
    

# mul()
# mul()
# mul()
# print(num)

# balance = 0
# def get_salary(amount):
#     global balance
#     balance = amount
#     print(f"У вас на счету {amount} сом")

# balance = 0
# def get_salary(amount):
#     global balance
#     balance = balance + amount
#     # print(f"У вас на счету {amount} сом")

# def pay_bills(amount, long_name):
#     global balance 
#     balance = balance - amount
    
#     print(f"Вы заплатили {amount} сом за {long_name}")
#     return balance

# def get_balance():
#     global balance
    
#     print(f"У вас на счету {balance} сом")


# get_salary(1000)
# get_balance()

# pay_bills(400, "кабельное тв")
# get_balance()

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# def age():
#     global a
#     for k, v in a.items():
#         if v >+ 17:
#             print(f"{k}, Вы можете войти в клуб")

#         else:
#             print(f"{k}, извините, Вы не проходите по age-control")

# age()

# a = ['pipi', 'papa', 'mama']
# b = []
# for x in a:
#     b.append(x.capitalize())

# print(b)

# a = ['pipi', 'papa', 'mama']
# b = []

# def name():
#     global b
#     for x in a:
        
#         b.append(x)

# print(b)
# name()

# def count_symbols(word):
#     glasnye = 0
#     soglasnye = 0
#     drugie = 0
#     for x in word:
#         if x.lower() in 'аяуюоеёэиы': 
#             glasnye +=1
                
#         elif x.lower() in 'бвгджзйклмнпрстфхцчшщ':
#             soglasnye += 1
               
                
#         else:
#             drugie += 1
                
#             return (f"Количество гласных: {glasnye}, согласных: {soglasnye}, остальных символов: {drugie}")
                



# print(count_symbols('Мурат супер!'))


# def count_symbols(word): 
#     glasnye = 0 
#     soglasnye = 0 
#     drugie = 0 
#     for letter in word: 
#         if letter.lower() in 'аяуюоеёэиы': 
#                 glasnye += 1 
#         elif letter.lower() in 'бвгджзйклмнпрстфхцчшщ': 
#                 soglasnye += 1 
#         else: 
#                 drugie += 1 
#     return (f'Количество гласных: {glasnye}, согласных: {soglasnye}, остальных символов: {drugie}')

# print(count_symbols('Мурат супер!'))

# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]

# def lower_7():
#     b = []
#     for x in a:
#         if x < 7:
#             b.append(x)
#     return b

# print(lower_7())

# var = 'переменная в foo' 
# def foo(): 
#     global var 
#     var = 'переменная foo' 
#     print('переменная в foo: ', var) 
#     def bar(): 
#             global var 
#             var = 'переменная bar' 
#     bar() 
# foo() 
# print('переменная в foo: ', var)

# var = 'переменная в foo' 
# def foo():
#     global var
#     var = 'переменная foo'
#     print(f'переменная в foo:', var)
#     def bar():
#         global var
#         var = "переменная bar"
#         print(f'переменная в foo:', var)
#     bar()
    



# foo()


# balance = 0
# def get_salary(amount):
#     global balance
#     balance = balance + amount

# def pay_bills(amount, long_name):
#     global balance
#     balance = balance - amount
#     print(f"Вы заплатили {amount} сом за {long_name}")

# def get_balance():
#     global balance
#     print(f"У вас на счету {balance} сом")

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# def count_symbols(words):
#     глассные = 0
#     согласные = 0
#     символы = 0
#     for x in words:
#         if x.lower() in 'аяуюоеёэиы':
#             глассные += 1

#         elif x.lower() in 'бвгджзйклмнпрстфхцчшщ':
#             согласные +=1

#         else:
#             символы += 1

#     return (f"Количество гласных: {глассные}, согласных: {согласные}, остальных символов: {символы}")

# print(count_symbols('Мурат супер!'))

# def count_symbols(word): 
#     glasnye = 0 
#     soglasnye = 0 
#     drugie = 0 
#     for letter in word: 
#         if letter.lower() in 'аяуюоеёэиы': 
#                 glasnye += 1 
#         elif letter.lower() in 'бвгджзйклмнпрстфхцчшщ': 
#                 soglasnye += 1 
#         else: 
#                 drugie += 1 
#     return (f'Количество гласных: {glasnye}, согласных: {soglasnye}, остальных символов: {drugie}')

# print(count_symbols('Мурат супер!'))


# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# def lower_7():
#     b = []
#     global a
#     for x in a:
#         if x < 7:
#             b.append(x)
#     return b

# print(lower_7())

# def func15(users):
    
#     for x in users:
#         for k ,v in x.items():
#             if k == "name":
#                 b = v
#         for k, v in x.items():
#             if k == "work":
                
#                 if v.startswith("IT"):

#                     print(f"{b}, скидки в магазине компьютерной техники!")


                    
# func15(users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ])


# def func15(users):
    
#     for x in users:
#         for k ,v in x.items():
#             if k == "name":
#                 b = v
#                 for k, v in x.items():
#                     if k == "work" and v.startswith("IT"):
                        
                
#                         print(f"{b}, скидки в магазине компьютерной техники!")


# func15(users=[
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ])


                    
# (func15([
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]))

# def func17(employees):
#     for x in employees:
#         for k, v in x.items():
#             if "salary" in k:
#                 print(v)

        

        

        
            





# func17(employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ])




# string1 = "America"
# string2 = "Japan"

# a = string1[0]
# b = string1[3]
# c = string1[6]

# d = string2[0]
# e = string2[2]
# f = string2[4]

# print(a+d+b+e+c+f)

# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list = []

# for i in range(len(list_)):

# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for x in list_:
#     new_list.append(str(x))

# print(new_list)

# list_ = [1, 2, 3]
# for x in list_:
#     if x  in list:
#         print("Yes")
#     else:
#         print("No")

# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list1 = [list_[i::step] for i in range(len(list_))if i <step]

# print(list1)


# size = 3
# list_ = []

# for x in range(size):
#     list_.insert(x, [0, 0, 0])

# print(list_)

# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]




# inp = input()
# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# list1 = []

# for x in list_:
#     if x.startswith(inp):
#         list1.append(x)

# print(list1)



# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# max_ = max(dict_.values())
# for k in dict_.keys():
#     if dict_[k]== max_:
#         print(k)

# string1 = "America"
# string2 = "Japan"
# print(string1[:1] + string2[:1] + string1[int(len(string1)/2)] + string2[int(len(string2)/2)] + string1[-1] + string2[-1])

# count = 0


# count = 0
# number = str(input())
# if number.isdigit():
#     number = int(number)
#     count = count+number

# print(count)



# c = int(number)
# count1 = count+c
# print(count1)

# str_list = ['abc', 'xyz', 'aba', '1221']
# indexs = []
# for x in str_list:
#     if x == x[::-1]:
#         indexs.append(x)

# print((indexs))

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list = []
# min_list = []
# for x in lists:
#     max_list.append(x)
#     min_list.append(x)
# print(f"max_list {max(max_list)}")
# print(f"min_list {min(min_list)}")



# employees = [ {'name': 'Jack', 'salary': 10000, 'overTime': 4}, {'name': 'Tom', 'salary': 15000, 'overTime': 3}, {'name': 'Jessica', 'salary': 20000, 'overTime': 9}, {'name': 'Helen', 'salary': 25000, 'overTime': 2}, {'name': 'Peter', 'salary': 30000, 'overTime': 7} ] 
# def func17(lsofdict:dict): 
#     for x in lsofdict: 
#         if 'overTime' in x: 
#             x['salary']+=x['overTime']*200 
#             x.pop('overTime') 
       
#     return lsofdict



# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]

# def func19(students_list:dict):
#     for x in students_list:
#         if "marks" in x:
#             sorted(x)
#     return students_list



        
        

# def calc(a, b, operation):
#     if operation == "+":
#         return add_(a, b)

#     elif operation == "-":
#         return sub_(a, b)

#     elif operation == "/":
#         return div_(a, b)

#     elif operation == "*":
#         return mult_(a, b)
# def add_(a, b):
#     return a+b

# def sub_(a, b):
#     return a-b

# def div_(a, b):
#     return a / b

# def mult_(a, b):
#     return a*b

# print(calc(5, 6, "+"))

# balance=9_999_999 
# def spent(a,b,c): 
#     if c-b>=0: 
#         c-=b 
#         return ({'target':a,'spend':b},c) 
#     else: 
#         print(spent('neger',20000,balance))
#         return 'Недостаточно средств'  
# def deposit(a,b): 
#     b+=a 
#     return b

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list1 = []
# min_list2 = []

# for x in lists:

#     max_list1.append(x)
#     min_list2.append(x)

# print(f"max_list {max(max_list1)}")
# print(f"min_list {min(min_list2)}")

# 3) Создайте список с буквами. Напишите программу, которая склеит все буквы с вписке в строку. Не использовать метод join() и циклы.

# import functools 
# list_ = ["a", "p", "p", "l", "e"]

# list1 = functools.reduce(lambda x, y: x+y, list_)
# print(list1)

# 2) Реализуйте следующую программу: есть студенты, которые сдали экзамен. Вам необходимо сохранить имена и баллы тех студентов, которые не прошли проходной балл (<60). Далее каждому студенту вам необходимо отправить письмо, которое говорит о том, что этого студента собираются отчислить.
# dict_ = [
#     {"username":"Sanzhar", "point": 55},
#     {"username": "Sultan", "point": 54},
#     {"username": "Aigerim", "point": 61},
#     {"username":"Erkayim", "point":65}
# ]

# list1 = list(map(lambda x:f"{x['username']}, вас собираются отчислить", filter(lambda x:x["point"]<60, dict_)))
# print(list1)


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# list2 = len(list(map(lambda x: x%2 == 0, list_)))
# list3 = len(list(map(lambda x: x%2 != 0, list_)))
# result = (f"even: {list2}, odd: {list3}")
# print(result)

# import functools
# list_ = ["paul", "George", "Ringo", "John"]
# result = functools.reduce(lambda x, y: x if len(x)> len(y) else y, list_)
# print(result)


# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# result = list(map(lambda x:f"{x} Python" if len(x)>5 else f"{x} JavaScript", names))
# print(result)

# string = 'hello'
# result = tuple(enumerate(string))
# print(result)


# list_ = [0.334, 23.3443, 43.4, -13.44, 22.03, -11.033, 267.993, -3.24]
# result = list(map(lambda x: round(x**2,3), list_))

# print(result)
# import functools
# list_ = ['a', 'n', 'n', 'a']
# result = functools.reduce(lambda x, y: x+y, list_)


# print(result)

# # a = 1
# # print(a)

# ls = [1,2,3,4]
# (lambda x: x, ls)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 

# new_list = ["shorter" if len(x) <= 4 else "longer "for x in list_name]
# print(new_list)

# dict_ = {x:x**2 for x in range(1,11)}
# print(dict_)

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {x:list(range(1, y+1)) for x ,y in a.items()}
# print(dict_)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [x for x in string_ if x == int]
# print(list_)



list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10]
list2 = [x for x in list1 if type(x)== str]
print(list2)

   




























    

    



    








 



























