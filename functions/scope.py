# def func():
#     var = 15
#     return var * 2

# print(var)

# print(func())


# Область видимости и пространство имен или scopes определяет контекст переменной, в рамках которого мы можем ее использовать.

# a = 5
# print(a)
# def func():
#     print(a)

# func()

# built-in - (встроенная)- print len max librarires

# global(глобальная)

# enclosed (не локальная, nonlocal)

# local (локальная)


# x = 200 #(global)


# def func():
#     print(x, "!")
#     x+= 100 #UnboundLocalError:

# func()


# a = 10 #(global)
# print() # built-in

# def hello(): # (global)
#     a = "Hello World" # (local)
#     print(a, "local inside at func")

# hello()
# print(a, "global")


# #LEGB

# >>>>>>>>>

# local -> enlosed -> global -> built-in


# x = "global"
# print(x, "1")


# def enclosed():
#     x = "enclosed"
#     def local():
#         x = "local"
#         print(x, "3")
#     print(x, "2")
#     local()
#     print(x, "4")

# enclosed()
# print(x, "5")



# a = 10
# def func():
#     print(a)
#     a = "local"
#     print(a)
# func()

# i = 0
# def incriment():
#     i = i+1

# incriment()

# global -> позволяет изменять значение  глобальный переменной находясь в локальной или замкнутой области видимости .


# nonlocal -> позволяет изменять значение не локальной переменной находясь в локальной области видимости .



# var = 100
# def increment():
#     global var
#     var += 1
# print(var)
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var)  100
#             105


# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c = counter()
# # print(c)  <function counter.<locals>.increment at 0x7f8553dd2050>

# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())


# b = counter()
# print(c())
# print(b())
# print(c())
# print(b())


# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment


# i = counter()

# for x in range(0, 100000):
#     if x % 3 == 0 and x % 5 == 0:
#         res = i()
#         print(res)

# print(f"Result: {res}")

# print(dir(__builtins__))
# print(len(dir(__builtins__)))


# a = 5
# b = 6
# c = 7

# def func():
#     john = "john Snow"
#     print(locals())

# print(globals())
# print()
# func()

"---------------------------------------------------------------------------------"

# Дан список внутри которого список из трех чисел. Нужно найти максимальную сумму среди всех списков.
# [[1,2,3], [3,3,5], [5,5,5,5]] -> 6, 11, 20 -> 20

ls = [[1,2,3], [3,3,5], [5,5,5,5]]

result = max(sum(x) for x in ls)
print(result)









