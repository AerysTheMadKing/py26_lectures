# # Принципы ООП:

# # 1.Наследование
# # 2.Инкапцуляции
# # 3.Полиморфизм

# # 4 Абстракция
# # 5.Композиции
# # 6.Агрегация


# # Наслодование - Позволяет принимать родительские методы и атрибуты для дочерного класса.

# # 1) Родительский класс
# # 2) Дочерний класс

# #----------------------------------------------

# class Animal:
#     def print_info(self):
#         print('i\'m an animal!!')

# class Croco(Animal):
#     pass




# croco = Croco()
# croco.print_info()


# class Animal:
#     name = None
#     golos = None
#     meal = None

#     def say(self):
#         print(f'This animal is {self.name}: {self.golos}')



#     def eat(self):
#         print(f'This animal is {self.name}: {self.meal}')


# class Lion(Animal):
#     name = 'lion'
#     golos = 'roar'
#     meal = 'meat'
#     griva = True

#     def info(self):
#         print(f'{self.name} griva: {self.griva}')

# class Dog(Animal):
#     name = 'dog'
#     golos = 'bark'
#     meal = 'meat'


# class Koala(Animal):
#     name = 'koala'
#     golos = 'roar'
#     meal = 'efkalit'

# rex = Dog()
# simba = Lion()
# julian = Koala()


# rex.say()
# rex.eat()

# simba.say()
# simba.eat()
# simba.info()

# julian.say()
# julian.eat()


# class Person:
#     def info(self):
#         print('I\'m person from Bishkek')


# class Student(Person):
#     def info(self):
#         super().info()
#         print('I am study at Manas University!')

# obj = Student()
# obj.info()

# obj2 = Person()
# obj2.info()



# class Laptop:


#     def __init__(self, brand, model, price) -> None:
#         self.brand = brand
#         self.model = model
#         self.price = price


#     def get_info(self):
#         return {'brand': self.brand, 'model': self.model, 'price': self.price}



# class MacBook(Laptop):

#     def __init__(self, brand, model, price, year, display) -> None:

#         super().__init__(brand, model, price)
#         self.year = year
#         self.display = display

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['display'] = self.display
#         return repr

# class Acer(Laptop):
#     def __init__(self, brand, model, price, videocard, display) -> None:
#         super().__init__(brand, model, price)
#         self.videocard = videocard
#         self.display = display

#     def get_info(self):
#         repr = super().get_info()
#         repr['videocard'] = self.videocard
#         repr['display'] = self.display
#         return repr

# mac = MacBook('Apple', 'Air', 1000, 2022, 13)

# print(mac.get_info())


# acer = Acer('Acer', 'swift', 600, 'ge force 3040', 'xRGB14')

# print(acer.get_info())

        
# -----------------------------------------------------

# class Employee:
#     bonus = 1.5

#     def __init__(self, first_name, last_name, salary) -> None:
#         self.name = f'{first_name} {last_name}'

#         self.salary = salary

#     def get_info(self):
#         return f'FIO: {self.name}, Salary: {self.salary}'


#     def give_increase(self):
#         self.salary = self.salary*self.bonus

#     def __str__(self) -> str:
#         return self.get_info()


# class Developer(Employee):
#     def __init__(self, first_name, last_name, salary, language) -> None:
#         super().__init__(first_name, last_name, salary)
#         self.programming_lang = language


#     def get_info(self):
#         info =  super().get_info()
#         info+= f', Prog Language: {self.programming_lang}'
#         return info

    


# class Manager(Employee):
#     def __init__(self, first_name, last_name, salary, devs = []) -> None:
#         super().__init__(first_name, last_name, salary)
#         self.devs = devs



#     def add_devs(self, developer):
#         self.devs.append(developer)

#     def show_devs(self):
#         return [x.get_info() for x in self.devs]

# dev1 = Developer('John', 'Snow', 1500, 'Python')

# dev2 = Developer('Steve', 'Jobs', 3000, 'C++')

# dev3 = Developer('Lary', 'Page', 1500, 'JS')

# dev4 = Developer('Tirion', 'Lanister', 1000, 'Python')

# man1 = Manager('Jamie', 'Lanister', 2000)

# man2 = Manager('Dastan', 'Katana', 4000, [dev3, dev2])

# print(f'Manager: {man1.get_info()}, has {man1.show_devs()} developers!')

# print(f'Manager: {man2.get_info()}, has {man2.show_devs()} developers!')

# print("Before")

# man1.add_devs(dev1)
# man1.add_devs(dev4)
# man2.add_devs(dev1)

# print("After")

# print(f'Manager: {man1.get_info()}, has {man1.show_devs()} developers!')

# print(f'Manager: {man2.get_info()}, has {man2.show_devs()} developers!')


# dev1.give_increase()
# man2.give_increase()

# print(dev1)
# print(man2)






