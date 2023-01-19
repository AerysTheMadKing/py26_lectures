# №1 Операторы сравнения
# №2 Условные операторы
# №3 Логические операторы

#==========================================================================================
#№1 Операторы сравнения

#<,>, ==, <=, >=, != (не равно)
# num1 = 18
# num2 = 15
# print(num1<num2) # False

# num1 = 18
# num2 = 15
# print(num1 != num2) #True

# num1 = 18
# num2 = 15
# print(num1 >= num2) #True


# stroka1 = "Hello!"
# stroka2 = "World!"
# print(stroka1 < stroka2) #True #Ascii code
# print(ord("H")) #72
# print(ord("W")) #87
# print(chr(90)) #Z

# text = "Hello world! My name is John!"
# if text[0]==72:
#     print("Yes")
# else:
#     print("Nooo!") #Noo!

#     text = "Hello world! My name is John!"

# if ord(text[5])==72:
#     print("Yes")
# else:
#     print("Nooo!")


#Условные операторы - они созданы чтобы программма могла выполнять
# разные участки кода в зависимости от условия.

#    <body if>-*
#    <body if> #сработает только если True

# elif<condition>:
#     <body elif>
# elif<condition>  #сработает только если True
#      <body elif>
# else:
#     <body else> #Сработает только если во всех остальных False



# string = input('Enter smt:')
# if string == "Hello":
#  print("Hello stranger!")
# elif string == "John":
#  print("Welcome back John Snow!")
# elif string == "Mercedes":
#  print("Mercedes Benz S Class!")
# else:
#  print("Совпадений не найдено")
#  print("The end!")



# name = input("Enter smt: ")
# if name == "Askat":
#     print("Hello Askat")
# elif name =="Almaz":
#     print("Have a nice day Almaz")
# elif name == "Alibek":
#     print("Good night Alibek")
# else:
#     print("Нету такого")
#     print("the end")



# email = input("Enter Email:")
# password1 = input("Enter password: ")


# if len(password1)<8:
#     raise Exception ("Password too short! (password need at least 8 characters!)")


# password2 = input("Enter password confirmation: ")

# if password1 != password2:
#     raise Exception ("Passwords did\'t match!")
# else:
#     print("Succesfully signed up!")



# age = input("Enter your age: ")

# if age.isdigit():
#     age = int(age)
#     print(f"Your age; {age}!")

# else:
#     raise Exception ("Enter the valid age (only digits!)")

# if age>170:
#     raise Exception ("Invalid age!")

# if age < 21:
#     print(f"Чувак приходи через {18 - age} лет!")

# else:
#     print("Ты проходишь \' по возрасту , Welcome!")


# Логические операторы
# and -> логическое и
# or ->  лог и
# not -> лог отрицание

# операторы идентификации
# in -> проверят наличие элемента внутри массива либо строки
# is -> сравнивает ячейки памяти
# == сравнивает значения
# is not -> отрицательное сравнение двух ячеек





# my_age = 20
# other_age = 18
# result = my_age == 21 and other_age == 18
#            #False          #True
#                    #False
#                    my_age = 20


# my_age = 20
# other_age = 18
# result = my_age == 20 and other_age == 18
#            #True          #True
#                    #True

# print(result)


# my_age = 20
# other_age = 18
# result = my_age == 21 or other_age == 18
#            #False          #True
#                    #True

# print(result)


# my_age = 20
# other_age = 18
# result = my_age == 21 and other_age == 19
#            #False          #False
#                    #False 
  
# print(result)   

# result = not my_age == 21
# print(result)


# cash = int(input("Enter your cash: "))

# if cash >1000 and cash<10000:
#     print(("Средне!"))
# elif cash>10000 and cash<100000:
#     print("Много")
# elif cash >= 100_000:
#     print("Красавчик!")
# else:
#     print("печально!")



# is_google_user = True
# is_github_user = True
# is_age_less_21 = True
# user_coin = 3000


# if (is_google_user or is_github_user) and (is_age_less_21 or user_coin > 5000):
#     print("You enter the system")
# else:
#     print("Sorry, you couldn\'t enter!")

























 
