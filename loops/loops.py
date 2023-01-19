# while<expression>:
#     <body>

# i = 0
# while i<=10:
#     i+=1
#     print(f"Цикл исполнился {i} раз!")

# name1 = ""
# name2 = ""
# i = 0
# while name1.lower() != "john" and name2.lower() != "raychel":

#     name1 = input("Enter first name: ")
#     name2 = input("Enter second name: ")

#     i+=1
#     if i>=5:
#         print("Sicl stopped!")
#         breakpoint
    

# else:
#     print("You enter correct name!")

"----------------------------------------------"

# "Моржовый оператор"

# user = {"username": "john", "password": "bastart"}

# i = 3
# password = None
# while password != user['password']:
    
#     if i == 0:
#         print("you blocked!")
#         break

#     i -= 1

#     password = input(f'{user["username"]} Введите пароль\': ')

    
    

# else:
#     print(f'{user["username"]} you enter the system!')



# for <variable> in <iterable object>:
# <body>


# list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# i = iter(list_[::-1])
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# import random
# ls = []
# for x in range(1,101):
#     ls.append(random.randint(1,150))
# ls.sort()
# print(ls)
# set1 = set(ls)
# ls = list(set1)
# ls.sort()
# res = []
# set1 = set(ls)
# ls = list(set1)

# for x in ls:
#         if x % 2 == 0:
#             res.append(x)  


# print(res)


x = 100
res = [1, x]

for i in range(2,int(x**0.5)+1):
    if x % i == 0:
        res.extend({i, x//i})
        
res.sort()
print(res)

