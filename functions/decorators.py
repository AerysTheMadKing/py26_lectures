# Функция высшего порядка - это функция которая в качестве аргумента принимает другую функцию.



# Декоратор - это функция, которая позволяет без изменения кода обернуть другую функцию для того чтобы расширить функционально обернутой функции.


# from  datetime import datetime

# StopAsyncIteration

# start 


# finish

# def decorator(function,):
#     print(f" Called Func name: {function.__name__}")
#     return function()


# def hello():
#     print("Vsem privet!")
#     return "Hello"

# def john():
#     print("Hello my name is John Snow!")
#     return "John Snow"

# # hello()
# # john()
# decorator(hello)
# decorator(john)

# from typing import Callable


# def benchmark(func:Callable):
#     import time
#     start = time.time()
#     res = func()
#     finish = time.time()
#     print(f"Время выполнения функции {func.__name__}): заняло {finish - start}")
#     return res



# def loop():
#     i = 1
#     range_number = 100_000
#     while i <= range_number:
#         print(i)
#         i += 1
#     return i

# print(benchmark(loop))

# Pythonic way -> @decorator

# Синтаксический сахар - это кросота кода


# def benchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         res = func()
#         finish = time.time()
#         print(f"Время выполнения функции {func.__name__}): заняло {finish - start}")
#         return res
#     return wrapper

# @benchmark
# def loop():
#     i = 0
#     range_number = 1_000_000
#     while i < range_number:
#         i += 1

#     return i

# @benchmark
# def add():
#     i = 0
#     range_number = 1_000_000
#     ls = []
#     while i < range_number:
#         i += 1
#         ls.append(i)

#     return i

# print(loop())
# print(add())


# def strong(func):
#     def wrapper (*arg, **kwargs):
#         return "<strong>" + func() + "</strong>"

#     return wrapper


# def div(func):
#     def wrapper (*arg, **kwargs):
#         return "<div>" + func() + "<div>"
#     return wrapper

# @div
# @strong
# @div

# def John():

#     return "John Snow"

# print(John())


# def trace(func):
#     def wrapper (*args, **kwargs):
#         print(f"Trace: вызвана {func.__name__}(),\n {args} {kwargs}")
#         original_result = func(*args, **kwargs)
#         print(f"Trace: вызвана {func.__name__}(),\n вернула {args} {kwargs}")
#         return original_result
#     return wrapper



# @trace
# def say(name, line):
#     return f"{name}: {line}"

# print(say("John", "Snow"))


# def func():
#     print("Hello world")
#     return func

# func()()()()()

# def repeat(num):
#   def wrapper(func):
#     def wrapper1(name):
#         i = 0
#         while i < num:
#             i += 1
#             func(name)
#     return wrapper1
#   return wrapper
      
 
# @repeat(num=4)
# def function(name):
#     print(f"{name}")


# function("Python")


# def func16(km, l):
#     return(f"На 100км было расходовано {round(100*l/km)}л горючего")

# print(func16(50, 8))

# n = int(input()) 
# if n >= 11 and n <= 14: 
#     print(f'На лугу пасется {n} коров') 
# else: temp = n % 10 
# if temp == 0 or (temp >= 5 and temp <= 9): 
#     print(f'На лугу пасется {n} коров') 
# if temp == 1: 
#     print(f'На лугу пасется {n} корова') 
# if temp >=2 and temp <=4: 
#     print(f'На лугу пасется {n} коровы')


# def func18(word):
#     str_list = [x for x in word if str == type(x)]
#     num_list = [x for x in word if int == type(x)]
#     return num_list, str_list 

# print(func18([1,2,3]))