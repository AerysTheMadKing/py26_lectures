#list-> 0:200 -> num % 2 == 0
# ls = list(range(0,200,2))
# print(ls)



#list -> 0:300 -> num % 2 == 0 and num % 3 ==0
# ls = []
# for x in range(0,300):
#     if x % 2 == 0 and x % 3 == 0:
#         ls.append(x)
    
# print(ls)
# ls = []
# for x in range(0,100):
#     if x % 2 == 0:
#         ls.append(x**2)

#     else:
#         ls.append(x)
# print(ls)


" LIST COMPREHENSIONS " 

#генератор списков, упрощенный подход к созданию списков, который задействует цикл for, а также конструкции if else для определения условий в генерации.

#newlist = [expression for item in iterable < if condition == True> ]

# ls = [x for x in range (0,200) if x % 2 == 0]

# print(ls)


# list -> 0:300 -> num % 2 == 0 and num % 3 ==0
# ls = []
# for x in range(0,300):
#     if x % 2 == 0 and x % 3 == 0:
#         ls.append(x)


# ls = [x for x in range(0,200) if x % 2 == 0 and x % 3 ==0]
# print(ls)


# ls = []
# for x in range(0,100):
#     if x % 2 == 0:
#         ls.append(x**2)

#     else:
#         ls.append(x)
# print(ls)

#  >>>>

# ls = [x**2 if x % 2 == 0 else x for x in range(0,100)]
# print(ls)



# ls = [x**2 for x in range(1,11)]
# print(ls)

# ls = [x**3 if x % 2 !=0 else x+100 for x in range(1,11)]
# print(ls)



# ls = [for x in range(1,11)]
# ls = list(range(0,11))
# i = 0 
# for x in ls:
#     i += 1
#     if i == 4 :
#         i = 0
#         index = ls.index(x)
#         ls.insert(index+1,"John")

# print(ls)


"------------------------------------------------------------------------------------"




# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # ls = [1, 12, 9, 14, 25, 16 ...]


# result = [x+10 if x % 2 == 0 else x**2 for inner in ls for x in inner]
# print(result)

# from datetime import datetime
# from time import sleep
# start = datetime.now()
# ls = []
# for x in range (1, 100000000):
#     ls.append(x)
# finish = datetime.now()
# print(finish-start)


# fruits = ["apple", "banana", "kiwi", "mango", "limon"]

# ls = [x for x in fruits if x!="apple"]
# print(ls)


# fruits = ["apple", "banana", "kiwi", "mango", "limon" "mandarin"]
# ls = [x for x in fruits if x.startswith("m")]
# print(ls)


"-----------------------------------------------------------------------"

" DICT COMPREHENSIONS "

# a = {x: x**2 for x in range(1,15)}
# print(a)

# dict1 = {

#     "a":1,
#     "b":2,
#     "c":3,
#     "d":4,
#     "e":5,
#     "f":6,
#     "g":7,
#     "h":8
# }

# # "a": "odd", "b": "even"

# new_dict = {k: "odd" if v % 2 != 0 else "even" for k, v in dict1.items()}
# print(dict1)
# print(new_dict)

















    



































