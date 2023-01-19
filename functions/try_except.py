# Обработка исключений 
# Оператор try except


# Ошибки -> связаны с кодом

# SyntaxError
# IndentationError
# TabError


# Исключения -> Invalid Value
# ZeroDivisionError
# ArithmeticError
# NameError
# KeyError
# IndexError
# ImportError
# BaseException # прородитель всех исключений

# num = int(input("Enter num: "))
# print(type(num), num)


# try: 
#     <body try>

# except <Exception>
#     <body>

# <else>
#     <body> Только если все окей

# <finally> в любом случае в конце


# num1 = int(input("Enter num: "))
# print(num1)
# print("Important")


# try: 
#     num1 = int(input("Enter num: "))
    
# except ValueError:
#     print("Invalid Value")

# else:
#     print(num1)

# finally:
#     print("Important")



# try:
#     num1 = int(input("Enter first num: "))
#     num2 = int(input("Enter second num: "))
#     print(num1 / num2)

# except (ValueError,ZeroDivisionError) as error:
#     print("You enter incorrect num")
#     print(error)



# try:
#     num1 = int(input("Enter first num: "))
#     num2 = int(input("Enter second num: "))
#     print(num1 / num2)

# except Exception as error:
#     print("You enter incorrect num")
#     # print(error)

# list_ = [1,2,3,4,5]

# try:
#     index = int(input("Enter index: "))
#     res = list_[index]
#     print(res)

# except ValueError :
#     print("ValueError!")

# except IndexError:
#     print("Index error!")



# try: 
#     num1 = int(input("Enter: "))
#     num2 = int(input("enter: "))
#     result = num1 / num2
# except ZeroDivisionError:
#     print("На 0 делит нельзя!")

# except ValueError:
#     print("Invalid symbol for int()!")

# else:
#     print(result)

# finally:
#     print("The end!")

























