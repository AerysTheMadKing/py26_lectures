# sentence = input("Enter smt: ")
# # if sentence [-1] == "?":
#     # print("vopsitel\'noe predlojenie!")

# # else:
#     # print('normal one!')


# print("vopsitel\'noe predlojenie!" if sentence[-1]== "?" or sentence[-2:] == "?!" else "normal one!")

'-------------------------------------------------------------'

#Ternary operators (Тернарные операторы) -  это конструкция, которая по своему действию конструкции if/else, но при этом записывается в одну строчку

# number = 18
# res = "even number" if number % 2 == 0 else "odd number"
# print(res)


#<выражение если в условые True> if <Условие> else <Выражение если в условии False>

# number = int(input("Enter number: "))
# res = number -100 if number<100 else number*2 
# print(res)



# ls = [55, 65, 75, 89, 100, 15,6]
# print(ls)
# choice = input("Enter max/min: ")
# res = max(ls) if choice.lower().strip() == "max" else min(ls)
# print(res)

"---------------------------------------------------------------"
# from string import digits 
# print(digits)
# print(type(digits))
# num = input("num: ")
# if num.isdigit():
#     num = int(num)
#     print("Important!")
#     print(num)
#     print(type(num))

# from string import digits 
# symbols = digits + "-" + "."
# flag = True

# while flag:
#     is_correct_number = True
#     num1 = input("Enter first number: ")
#     for x in num1:
#         if x in symbols:
#             pass
#         else:
#             print("You enter incorrect number: ")
#             is_correct_number = True



# from string import digits 
# symbols = digits + "-" + "."
# flag = True

# while flag:
    
#     is_correct_number = True
#     num1 = input("Enter first number: ")
#     for x in num1:
#         if not x in symbols:
       
#             print("You enter incorrect number")
#             is_correct_number = True
#             break

#     if not is_correct_number:
#         continue



#     num2 = input("Enter second number: ")
#     for x in num2:
#         if not x in symbols:
#             print("You enter incorrect number")
#             is_correct_number = False
            

#     if not is_correct_number:
#         continue

#     num1 = float(num1) if "." in num1 else int(num1)
#     num2 = float(num2) if "." in num2 else int(num2)

#     operator = input("Enter operation:(+, -, * /): ")
#     if operator == "+":
#         print(f"result: {num1+num2}")

#     elif operator == "-":
#         print(f"result: {num1-num2}")

#     elif operator == "*":
#         print(f"result: {num1*num2}")

#     elif operator == "/":
#         print(f"result: {num1/num2}")


#     else:
#         print("You enter incorrect operator!")


#     choice = input("Are you want to continue(yes/no)? ")
#     if choice.lower().strip() == "no":
#         flag = False
#         print("Bye bye !")

   




