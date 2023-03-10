
# Магические методы (dunder - duble umderscore)- методы у которых два нихжних подчеркиваниях в начале ив конце . Магия в том что мы иих не вызываем напрямую, а они вызываются в опердеенной момент либо они вызывается оперделенными оператоми или функициями


# res = 5 + 5 #__add__
# print(res)

# class A(int):
#     pass

# obj = A()
# print(dir(obj))


#магические методы которые срабатывают при помощи оператораю


# __eq__(self, other) -> == : 5 == 7  self: 5   other:7
# __ne__ (self, other) -> !=
#__lt__(self, other) -> < ; __le__ -> <=
# __gt__(self, other) -> > ; __ge__ -> >=


#__sub__(self, other) -> -   __div__ -> /
#__mul__ -> *  __mod__ -> %
#__floordiv__ -> //  __add__ -> +
#__pow__ -> **                                               

# class MyClass:

#     def __init__(self, string) -> None:
#         self.string = string

#     def __add__(self, other):
#         print('add сработал')
#         print(self, '!!!')
#         print(other, '*****')
#         res = self.string + other.string
#         return MyClass(res)

#     def __str__(self) -> str:
#         return self.string

# obj1 = MyClass('John')

# obj2 = MyClass('Jamie')

# obj3 = MyClass('Lanister')

# obj4 = MyClass('Stark')
# print(obj1 + obj2 + obj3 + obj4)

# class Word(str):
    
#     def __init__(self, word) -> None:
#         self.word = word


#     def __gt__(self, other: str) -> bool:

#         print('gt сработал')
#         print(self, '!!!!!!')
#         print(other, '*****')

#         return len(self) > len(other)
        

# obj1= Word('John')
# obj2 = Word('Hello World')
        

# print(obj1 > obj2)


#--------------------------

# Конструктор -> __new__

# Инициализатор -> __init__(self)

# вызываются, когда создаем обьект



# class Converter(float):

#     def __new__(cls, __x):
#         print('new сработал')
#         print(cls, '!!!')
#         print(__x, '***')
#         return super().__new__(cls, __x)

#     def __init__(self, x) -> None:

#         print('init сработал')
#         print(self, '!!!!')
#         self.number = x 
        

# obj1 = Converter(51)
# print(obj1)


#----------------------------------

# Дандер методы строкового отображения обьектов

# __str__ -> для отобродения строки, которую будут видеть пользователи.

# __repr__ -> строковую информацию о том как создать обьект

# __len__ --> len(obj)

# __repr__ --> repr(obj)

# eval('6 + 6') --> 6 + 6

# class Base:
#     def __init__(self, string) -> None:
#         self.string = string

#     def __str__(self) -> str:
#         return f'Обьект: {self.string}'

#     def __repr__(self) -> str:
#         return f'Base("string")'
# user = Base('Hello John')
# print(user)
# print(repr(user))
# obj1 = eval(repr(user))  # Base('string')
# print(obj1)


#-----------------------------------------------


# class Person:

#     def __init__(self, attrs: dict) -> None:

#         for key, value in attrs.items():
#             setattr(self, key, value)


# alice = Person({'name': 'Alice Rose', 'income': 10000, 'eyes': 'brown'})

# john = Person({'email': 'johnsnow@gmail.com', 'last_name': 'Snow'})

# print(f'{alice.name} -- {alice.income} -- {alice.eyes}')

# print(f'{john.email} -- {john. last_name}')



# class MyList(list):

#     def __init__(self, ls):
#         self.ls = ls

#     def __getitem__(self, index):
#         print(self.ls[index - 1])


# x = MyList(['123','hello',3,4,5])
# x[1]
# x[2]
# x[3]


#---------------------------------------
 
# __iter__ --> вызывается, когда мы итерируем обьект


# class A:
#     def __iter__(self):
#         for i in range(1, 10):
#             print('iter сработал')

#             yield i


# x = A()

# for i in x:
#     print(i)
        


# a = range(10)
# print(a)
# for x in a:
#     print(x)


# def generator(num):
#     for i in range(num):
#         yield i

# a = generator(5)
# for x in a:
#     print(x)

                                                                                                                                     



#-------------------------------

# class User:

#     def __init__(self, name) -> None:
#         self.name = name

#     def __call__(self):
#         print(f'User object: {self.name}')



# user1 = User('John Snow')
# user1()

"""
1. Создайте класс Account и переопределите в нем методы __init__, __repr__, __str__ и __del__.
Объекты класса должны содержать атрибуты имени, баланса и города, где открыт счет.
Метод __init__ должен возвращать сообщение о создании счета, __repr__ только имя держателя счета
и баланс, а __str__ сообщение с приветствием и также информацией о держателе счета, 
балансе и филиале банка в котором зарегистрирован клиент, __del__ в свою очередь сообщение об удаление 
и слово "Пока!"
"""

# class Account:

#     def __init__(self, name, balance, city, ) -> None:
#         pass

#     def __repr__(self) -> str:
#         pass

#     def __str__(self) -> str:
#         pass

#     def __del__(self):
#         pass


"""
2. Определите класс MyNumber который наследуется от класса int. 
У экземпляра класса должен быть обязательный атрибут value. 
Переопределите методы сложения, вычитания, умножения и деления для класса таким  образом чтобы при при использовании операторов + - * / - результат возвращался с сообщением об использованном методе, 
например:print(num + 5)  -------> "Это сложение и Ваш результат равен 10"
"""

# class MyNumber(int):

#     def __init__(self, value) -> None:
#         self.value = value

#     def __add__(self,other: int) -> int:
#         res = self.value + other.value
#         return f'Это сложение и Ваш результат равен {MyNumber(res)}'

#     def __sub__(self,other: int) -> int:
#         res = self.value - other.value
#         return f'Это вычитание и Ваш результат равен {MyNumber(res)}'

#     def __div__(self,other: int) -> int:
#         res = self.value / other.value
#         return f'Это деление и Ваш результат равен {MyNumber(res)}'

#     def __mul__(self,other: int) -> int:
#         res = self.value * other.value
#         return f'Это умножение и Ваш результат равен {MyNumber(res)}'


# obj = MyNumber(65)
# obj1 = MyNumber(20)

# print(obj*obj1)


"""
3. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
элементов начиналась с 1. Например:
x = MyList([1,2,3,4,5])
x[1] → 1
"""

# class MyList(list):

#     def __init__(self, list_):
#         self.list_ = list_

#     def __getitem__(self, index):
#         print(self.list_[index-1])

# obj = MyList([1,2,3,4,5])
# obj[1]


"""
4. Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: имя, фамилия, класс, и оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
"""



"""
5. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
Также в методе __new__ напишите условие для удаления
пробелов и пустых строк в созданных словах.
"""

# class Word(str):
#     def __new__(cls, string):
        
#         string = '\n'.join(x.strip() for x in string.split('\n') if x.strip())

        
#         return str.__new__(cls, string)


#     def __gt__(self, other):
#         return len(self) > len(other)

#     def __lt__(self, other):
#         return len(self) < len(other)

#     def __ge__(self, other):
#         return len(self) >= len(other)

#     def __le__(self, other):
#         return len(self) <= len(other)

    

        


# word = Word('makers')
# word1 = Word('bootcamp')

# print(word < word1)


'''MAGIC METHODS'''

'''1)QUESTION'''


# class Account:

#     def __init__(self, name, balance, city):
#         self.name = name
#         self.balance = balance
#         self.city = city
#         print("Счет создан")

#     def __repr__(self):
#         return f'{self.name} {self.balance}'

#     def __str__(self):
#         return f'Hello {self.name} {self.balance} {self.city}'

#     def __del__(self):
#         print('Пока')

# obj_account = Account("Rick", 2013, 'Bishkek')  
# print(obj_account)  
# print(repr(obj_account)) 


'''2)QUESTION'''

# class MyNumber(int):

#     def __init__(self, value) -> None:
#         self.value = value

#     def __add__(self,other: int) -> int:
#         res = self.value + other
#         return f'Это сложение и результат равен: {res}'

#     def __sub__(self,other: int) -> int:
#         res = self.value - other
#         return f'Это вычитание и результат равен: {res}'

#     def __truediv__(self,other: int) -> int:
#         res = self.value / other  
#         return f'Это деление и результат равен: {res}'

#     def __mul__(self,other: int) -> int:
#         res = self.value * other
#         return f'Это умножение и результат равен: {res}'


# obj_int = MyNumber(5)
# print(obj_int + 5)  
# print(obj_int - 5)  
# print(obj_int * 5)  
# print(obj_int / 5)    


'''3)QUESTION'''

# class MyList(list):

#     def __init__(self, list_):
#         self.list_ = list_

#     def __getitem__(self, index):
#         return self.list_[index-1]

# obj_list = MyList([1,2,3,4,5])
# print(obj_list[1])

'''4)QUESTION'''


# class Student:

#     def __init__(self, name, class_name, ball) -> None:
#         self.name = name
#         self.class_name = class_name
#         self.ball = ball

#     def operation(self):
#         res = []
#         for v in self.ball.values():
#             res.append(v)

#         average = (sum(res))/ len(res)
#         return average

#     def __gt__ (self, other):
#         return f'> {self.operation() > other.operation()}'

#     def __lt__ (self, other):
#         return f'< {self.operation() < other.operation()}'

#     def __ge__ (self, other):
#         return f'>= {self.operation() >= other.operation()}'

#     def __le__ (self, other):
#         return f'<= {self.operation() <= other.operation()}'


# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88}) 
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88}) 

# print(obj_student1 > obj_student2)  
# print(obj_student1 < obj_student2)  
# print(obj_student1 >= obj_student2)  
# print(obj_student1 <= obj_student2)


'''6)QUESTION'''

# class Kopilka:

#     def __init__(self):
#         self.__total = 0
#         self.__coins = []

#     def add_moneta(self, moneta):
#         self.__total += moneta
#         self.__coins.append(moneta)

#     def __len__(self):
#         return len(self.__coins)

#     def __getitem__(self, index):
#         return self.__coins[index]
        

# obj = Kopilka() 
# obj.add_moneta(25)
# obj.add_moneta(30)

# print(len(obj))
# for i in obj: 
#      print(i)


'''7)QUESTION'''

# class Anagram(str):
#     def __init__(self, value):
#         self.value = value

#     def __eq__(self, other):
#         list1 = list(map(lambda x: x, self.value))
#         list1.sort()
#         list2 = list(map(lambda x: x, other.value))
#         list2.sort()
#         return list1 == list2

#     def __mul__(self, other):
#         return self.value[::-1] * other
    

    
# word1 = Anagram('hello') 
# word2 = Anagram('olleh') 
# print(word1 == word2)
# print(word1 * 3)





