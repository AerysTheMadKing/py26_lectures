# def  sum_of_args(a, b, c, d): #parameters
#     return a + b + c + d

# result = sum_of_args
# print(result)
# print(result(5, 10 ,15,20))


"-----------------------------------------------------------------------"

# Позиционные и именованные аргументы

# def printParams(a, b, c):

#     print(a, "is stored in param a")
#     print(b, "is stored in param b")
#     print(c, "is stored in param c")

# printParams(5, 10, 15)


# def printParams(a = None, b = None, c = None):

#     print(a, "is stored in param a")
#     print(b, "is stored in param b")
#     print(c, "is stored in param c")

# printParams(a = 5,c = 15)


# def  sum_of_args(a, b, c, d): #parameters
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20)) # arguments ->> (позиционные аргументы)

# print(sum_of_args(a = 5, b = 10, c = 15, d = 20)) #keyword arguments ->> (Именованные 
# аргументы)



"-------------------------------------------------------------"


#Орератор *
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [*a, *b]
# print(c)


# (*args)  (**kwargs) в функциях

# "ARGS"

# def printScores(student, *args):
#     print(f"Student name: {student}")
#     print(args)
#     print(type(args))

# printScores("John Snow", 100, 99, 95, 91)


"KWARGS"

# def print_pet_names(owner, **pets):
#     print((f"Owner name: {owner}"))
#     # print(kwargs) 
#     # print(type(kwargs))    # {'dog': 'Rex', 'cat': 'garfild', 'fish': ['Nemo', 'Dori']}

#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f"{pet}:", *name)

#         else:
#             print(f"{pet}: {name}")
# print_pet_names("John Snow", dog = "Rex", cat = "Garfild", fish = ["Nemo", "Dori", "Alex"])



# def get_some_data(a, b, *args, **kwargs):
#     print("Parameters a and b: ", a, b)
#     print("Arguments: ", args)
#     print("KeyArguments: ", kwargs)
#     print(args[0])
#     print(args[-1])
#     print(kwargs["name"])

# get_some_data(1, 2, 3, 4, 5 , lang = "Python", name = "John Snow", car = "Mercedes Benz S-Class")


"--------------------------------------------------------------"

"Class Work"

#1)

# def generate_of_string(len_):
#     import string as s
#     import random

#     random_str = "".join(
#         random.choice(s.ascii_letters+s.digits) for i in range(0, len_)
#     )
#     return random_str

# print(generate_of_string(25))


#2)

# def add(a, b): return a + b

# def subtract(a, b): return a - b

# def multiply(a, b): return a * b

# def divide(a, b): return a / b

#     try: 
#         return a / b

#     except ZeroDivisionError:
#         return "На ноль делить нельзя"

# def calc(num1, num2):

#     operator = input("Введите оператор(+,-,*,/): ")

#     if operator == "+": return add(num1, num2)

#     elif operator == "-": return subtract(num1, num2)

#     elif operator == "*": return multiply(num1, num2)

#     elif operator == "/": return divide(num1, num2)

#     else: return "Вы ввели неверный оператор"


# def main():
#     try:
#         num1 = float(input("Введите первое число: "))
#         num2 = float(input("Введите второе число: "))

#     except ValueError:
#         print("Вы ввели некоректные данные")
#         main()

#         return

#     while True:
#         result = calc(num1,num2)
#         if type(result) == float:
#             print(f"Result: {result}")

#             break
#         else:
#             print(f"Result: {result}")

#     question = input("Хотите продолжить (Yes?No)?")
#     if question.lower() == "yes":
#         main()
    
#     else:
#         print("Спасибо за использования нашего калькулятора! Пока!")

# main()

# if __name__ == "__main__":
#     main()


"HOMEWORK-----------------------------------"




















