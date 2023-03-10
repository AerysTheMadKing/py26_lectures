# # # class A:
# # #     pass


# # # obj = A() 1) Экземпляр класса -> instance  2) Обьект класса -> object (они одно и тоже)



# # # """1) Напишите программу по следующему описанию. Есть класс "Снайпер". От него создаются два экземпляра. Каждому устанавливается здоровье в 100 очков. В случайном порядке они стреляют друг в друга. Тот, кто стреляет, здоровья не теряет. У того, в кого стреляют, оно уменьшается на 20 очков от одного выстрела. После каждого выстрела надо выводить сообщение, какой снайпер атаковал, и сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу."""

# # # import random
# # # class Sniper:
    
# # #     def __init__(self,name) -> None:
# # #         self.name = name
# # #         self.health = 100

# # #     def attack(self, other):
# # #         other.health -= 20
# # #         print(f"{self.name} attacked {other.name}, {other.name}'s health is now {other.health}")
    
# # #     def is_dead(self):
# # #         return self.health <= 0


# # # sniper1 = Sniper('Adilet')
# # # sniper2 = Sniper('Nuuman')



# # # while True:
# # #     attacker = random.choice([sniper1, sniper2])
# # #     defender = sniper1 if attacker == sniper2 else sniper2

# # #     attacker.attack(defender)

# # #     if defender.is_dead():
# # #         print(f"{defender.name} is dead, {attacker.name} wins")
# # #         break


# # """2) Напишите программу по следующему описанию. Есть класс Hogwarts. В нем определены следующие атрибуты-факультеты: 
# # Gryffindor, Ravenclaw, Hufflepuff, Slytherin. От класса Hogwarts создаются объекты-студенты. При создании студентов необходимо указать баллы за их следующие качества: courage (храбрость), intelligence (интеллект), justice (справедливость), ambition (амбиции). У студентов не могут быть качества одинакового уровня. В зависимости от того, какое качество студента преобладает, метод sorting_hat будет распределять студента в один из факультетов и выдавать в какой факультет поступил студент."""



# # # class Hogwarts:

# # #     gryffindor = 'Griffindor'
# # #     ravanclaw = 'Ravanclaw'
# # #     hufflepuff = 'Hufflepuff'
# # #     slytherin = 'Slytherin'


# # #     def __init__(self, courage: int, intelligence: int, justice: int, ambition: int) -> None:
# # #         self.courage = courage
# # #         self.intelligence = intelligence
# # #         self.justice = justice
# # #         self.ambition = ambition

# # #     def sorting_hat(self):
# # #         max_quality = (self.courage, self.intelligence, self.justice, self.ambition)
# # #         set_max_quality = tuple(set(max_quality))
# # #         print(set_max_quality) #-> 50, 20, 23
# # #         print(max_quality)
# # #         max_quality #-> 20, 23, 50, 50
# # #         if len(max_quality) != len(set_max_quality):
# # #             return "student can't have a same score"
# # #         max_quality = max(max_quality)

# # #         if self.courage == max_quality:
# # #             return "Gryffindor"
# # #         elif self.intelligence == max_quality:
# # #             return "Ravenclaw"
# # #         elif self.justice == max_quality:
# # #             return "Hufflepuff"
# # #         else:
# # #             return "Slytherin"
        
# # # student1 = Hogwarts(20, 23, 10, 50)
# # # student2 = Hogwarts(20, 10, 34, 41)
# # # student3 = Hogwarts(45, 34, 54, 54)
# # # student4 = Hogwarts(45, 23, 78, 90)

# # # print(student1.sorting_hat())

# # # class Hogwarts:
# # #     GRYFFINDOR = 'Gryffindor'
# # #     RAVENCLAW = 'Ravenclaw'
# # #     HUFFLEPUFF = 'Hufflepuff'
# # #     SLYTHERIN = 'Slytherin'

# # #     def __init__(self, courage: int, intelligence: int, justice: int, ambition: int):
# # #         self.courage = courage
# # #         self.intelligence = intelligence
# # #         self.justice = justice
# # #         self.ambition = ambition

# # #     def sorting_hat(self):
# # #         scores = [self.courage, self.intelligence, self.justice, self.ambition]
# # #         if len(set(scores)) < len(scores):
# # #             return "student can't have a same score"

# # #         max_quality = max(self.courage, self.intelligence, self.justice, self.ambition)

# # #         if self.courage == max_quality:
# # #             return self.GRYFFINDOR
# # #         elif self.intelligence == max_quality:
# # #             return self.RAVENCLAW
# # #         elif self.justice == max_quality:
# # #             return self.HUFFLEPUFF
# # #         else:
# # #             return self.SLYTHERIN
        
        

# # # student1 = Hogwarts(20, 23, 10, 50)
# # # student2 = Hogwarts(20, 10, 34, 41)
# # # student3 = Hogwarts(45, 34, 54, 54)
# # # student4 = Hogwarts(45, 23, 78, 90)

# # # print(student3.sorting_hat())

'''1)QUESTION'''

# class Song:
    

#     def __init__ (self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year


#     def show_title(self):
#         return f'Название этой песни {self.title}'

#     def show_author(self):
#         return f'Автор этой песни {self.author}'

#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'

# song = Song(title='Happy', author = 'Pharrell Williams', year = 2013)

# print(song.show_title())
# print(song.show_author())
# print(song.show_year())

'''2)QUESTION'''

# # class Circle:
# #     color = 'Синий'
# #     pi = 3.14

# #     def __init__(self, radius) -> None:
# #         self.radius = radius
        

# #     def get_area(self):
# #         return self.pi*self.radius**2


# # circle = Circle(2)
# # circle.color = "Green"

# # print(circle.color)

# # print(circle.get_area())

'''3)QUESTION'''

# # # class BankAccount:

# # #     def __init__(self, balance) -> None:
# # #         self.balance = balance
# # #         print(self.balance)

# # #     def deposit(self, amount):
# # #          self.balance += amount
# # #          print(f'Ваш баланс: {self.balance} сом')


# # #     def withdraw(self, amount):
# # #         self.balance -= amount
# # #         print(f'Ваш баланс: {self.balance} сом')

# # # account = BankAccount(balance = 0)

# # # account.deposit(1000) 
# # # account.withdraw(500) 

'''4)QUESTION'''

# # # class Taxi:

# # #     def __init__(self, name, cost, cost_km):
# # #         self.name = name
# # #         self.cost = cost
# # #         self.cost_km = cost_km


# # #     def get_total_cost(self, km):
        
# # #         return f'Такси {self.name}, стоимость поездки: {self.cost_km * km +self.cost} сом'


# # # taxi1 = Taxi(name = 'Namba', cost = 29, cost_km = 15)
# # # taxi2 = Taxi(name = 'Yandex', cost = 25, cost_km = 17)
# # # taxi3 = Taxi(name = 'Jorgo', cost = 28, cost_km = 15)

# # # print(taxi1.get_total_cost(10))
# # # print(taxi2.get_total_cost(6))
# # # print(taxi3.get_total_cost(14))





'''5)QUESTION'''

# # # class Phone:
# # #     ...

# # #     def __init__(self, name, last_name, phone) -> None:
# # #         self.name = name
# # #         self.last_name = last_name
# # #         self.phone = phone
        

# # #     def get_info(self):
# # #         print(f'Контакт: {self.name +" "+ self.last_name}, телефон: {self.phone}')


# # # contact = Phone('John', 'Snow', +996707707707)
# # # contact.get_info()

'''6)QUESTION'''

# # # class Salary:
# # #     percent = 8

# # #     def __init__(self, salary, experience) -> None:
# # #         self.salary = salary
# # #         self.experience = experience

# # #     def count_percent(self):
# # #         return (self.salary*self.percent /100) * self.experience

# # # obj = Salary(salary= 10000, experience=10)

# # # print(obj.count_percent())

'''7)QUESTION'''

# # # import datetime
# # # class Nobel:

# # #     def __init__(self, category, year, winner) -> None:
    
# # #         self.category = category
# # #         self.year = year
# # #         self.winner = winner

# # #     def get_year(self):

# # #         date1 = datetime.date(self.year, 1, 1)
# # #         date2 = datetime.date(2023, 1, 1)

# # #         delta = date2 - date1

# # #         difference_in_years = delta.days // 365
# # #         return f'выиграл {difference_in_years} лет назад'



# # # winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# # # winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 

# # # print(winner1.category, winner1.year, winner1.winner)

# # # print(winner1.get_year())
# # # print(winner2.category, winner2.year, winner2.winner) 
# # # print(winner2.get_year())

'''7)QUESTION'''

# # # import datetime
# # # class Nobel:

# # #     def __init__(self, category, year, winner) -> None:
# # #         self.category = category
# # #         self.year = year
# # #         self.winner = winner


# # #     def get_year(self):
# # #         a = datetime.datetime.now()
# # #         return f'выиграл {a.year - self.year} лет назад'


# # # winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# # # winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 

# # # print(winner1.category, winner1.year, winner1.winner)
# # # print(winner1.get_year())

# # # print(winner2.category, winner2.year, winner2.winner) 
# # # print(winner2.get_year())


'''8)QUESTION'''

# # # class Password:


# # #     def __init__(self, password:str) -> None:
# # #         self.password = password

# # #     def validate(self):
# # #         if len(self.password)<8 or len(self.password)>15:
# # #             return 'Password should be longer than 8, and less than 15'

# # #         elif not any(x.isdigit() for x in self.password):
# # #             return 'Password should contain numbers too'

# # #         elif not any(x.isalpha() for x in self.password):
# # #             return 'Password should contain letters as well'

# # #         elif self.password.isalnum() == True:
# # #             return 'Your password should have some symbols'

# # #         else:
# # #             return 'Ваш пароль сохранен.'

# # #     def __str__(self) -> str:
# # #         return "*" * len(self.password)


# # # password1 = Password('JohnSnow@11')
# # # print(password1)
# # # print(password1.password)
# # # print(password1.validate())


# # # Создайте класс Math, у экземпляра которого должно быть свойство number. У классa Math должно быть 3 метода:

# # # get_factorial - возвращает факториал числа(перемножить все составные числа до самого числа)

# # # get_sum - возвращает сумму цифр числа

# # # get_mul_table - возвращает таблицу умножения для числа до 10 в формате:

# # # from functools import reduce

'''9)QUESTION'''
# class Math:

#     def __init__(self, number) -> None:
#         self.number = number
        

#     def get_factorial(self):
#             a = range(1, self.number+1)
#             c= 1
#             for x in a:
                
#                 c*=x
#             return c
        


#     def get_sum(self):
#         a = str(self.number)
#         b = []
#         for x in a:
#             b.append(int(x))
#         return sum(b)

#     def get_mul_table(self):
#         i = 1
#         str_ = ''
#         while i <= 10:
#             result = self.number * i
#             str_ += f"{self.number} x {i} = {result}\n"
#             i += 1 
#         return str_
        

# math = Math(0)

# print(math.get_factorial())
# print(math.get_sum())
# print(math.get_mul_table())


'''10)QUESTION'''

# class ToDo:
#     instances = {}

#     def __init__(self, str_) -> None:
#        self.str_ = str_

#     def give_priority(self, prioroty):
#         ToDo.instances[prioroty] = self.str_

    
#     def list_of_tasks(self):
#         return sorted(ToDo.instances.items())



    
# to = ToDo('сходить в кино')
# to1 = ToDo('сделать домашку')
# to2 = ToDo('выгулять собаку')

# to.give_priority(1)
# to1.give_priority(4)
# to2.give_priority(3)

# print(ToDo.instances)
# print(to.list_of_tasks())



"""INHERITENCE"""


'''1)QUESTION'''

# class Class1:

#     def first(self):
#         pass

#     def second(self):
#         pass


# class Class2(Class1):


#     def third(self):
#         pass

#     def fourth(self):
#         pass

# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()

'''2)QUESTION'''

# class A:

#     def method1(self):

#         print('Основной функционал')

    

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')


# obj = B()
# obj.method1()

'''3)QUESTION'''

# class MyString(str):

#     def __init__ (self, word):
#         self.word = word

#     def append(self, str_):
#         self.word += str_
    

#     def pop(self):
#         last_v = self.word[-1]
#         self.word = self.word[:-1]
#         return last_v

#     def __str__(self) -> str:
#         return self.word

        



# example = MyString('String')
# example.append('hello')
# print(example)
# print(example.pop())
# print(example)

'''4)QUESTION'''

# class MyDict(dict):

#     def __init__(self, dict_):
#         self.dict_ = dict_

#     def get(self, word):
#         for x, y in self.dict_.items():
#             if word != x:
#                 return 'Are you kidding?'
#             else:
#                 return y 


# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some_title'))

'''5)QUESTION'''

# class Person:

#     def __init__(self,name, age):
#         self.name = name
#         self.age = age


#     def display(self):
#         print(f'name:{self.name}, age:{self.age}')


# class Student(Person):

#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         print(f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')

# obj_student = Student('Rick', 21, 'science')        
# obj_student.display() 
# obj_student.display_student() 

'''5)QUESTION  Also TRUE'''
# class Person:

#     def __init__(self,name, age):
#         self.name = name
#         self.age = age


#     def display(self):
#         return f'name:{self.name}, age:{self.age}'


# class Student(Person):

#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         info = super().display()
#         info += f', faculty:{self.faculty}'
#         return info


# obj_student = Student('Rick', 21, 'science')
# print(obj_student.display()) 
# print(obj_student.display_student())


'''6)QUESTION'''


# class ContactList(list):

#     def __init__(self, list_):
#         self.list_ = list_

#     def search_by_name(self, name):
#         a = []
#         for x in self.list_:
#             if name in x:
#                 a.append(x)
#         return a





# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
# print(all_contacts.search_by_name('Olya')) 


'''7)QUESTION'''

# class SmartPhones:
#     def __init__(self, name, color, memory) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0
        

#     def __str__(self) -> str:
#         return f'{self.name} {self.memory}'

#     def charge(self, battery):
#         self.battery+=battery




# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, version) -> None:
#         super().__init__(name, color, memory)
#         self.version = version

#     def send_imessage(self, word):
#         return f'sending {word} from {self.name} {self.memory}'

# import datetime
# class Samsung(SmartPhones):

#     def __init__(self, name, color, memory, version) -> None:
#         super().__init__(name, color, memory)

#     def show_time(self):
#         a = datetime.datetime.now()
#         return (a.time())

# phone = SmartPhones('generic', 'blue', '128GB')
# print(phone) 

# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 


# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello')) 

# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time()) 

'''8)QUESTION'''

# class CustomError(Exception):

#     def __init__(self, message):
#         self.message = message


# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')


# def check_letters(message1):
#     if message1 == message1.upper():

#         return f'ВСЕ ОТЛИЧНО! {message1}'

#     else:
#         raise capitals_error


# print(check_letters("HELLO"))  



'''>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''
'''CLASSWORK'''

'''1)QUESTION'''

# import datetime
# class Smartphone:
#     def call(self):
#         print('calling: +996 700 96 46 66')

#     def where_to_wear(self):
#         print('You can keep me anywhere')

# class Watch:
#     def see_time(self):
#         a = datetime.datetime.now()
#         print(a.time())

#     def where_to_wear(self):
#         print('You should wear me on your hand')

# class SmartWatch(Smartphone, Watch):

#     def where_to_wear(self):
#         print('You should wear me on your hand')

# obj = SmartWatch()

# obj.call()
# obj.see_time()
# obj.where_to_wear()

# '''2)QUESTION'''


# class SocialNetwork:

#      def __init__(self,username,password) -> None:
#         self.username = username
#         self.password = password
#         self.post = 0

# class CheckerMixin:
#     def check(self,username,password):
#         return self.username == username and self.password == password 


                
            
# class Instagram(CheckerMixin, SocialNetwork):
    
#     def post_post(self,post_title, username, password):
#         if self.check(username, password):
#             self.post += 1

#             return f'Post {post_title} successfully created'

#         else:

#             return 'Invalid username or password'

        


# class TikTok(CheckerMixin, SocialNetwork):

#     def post_video(self,post_video, username, password):
#         if self.check(username, password):
#             self.post +=1
#             return f'Post {post_video} Succesfully created'
            
#         else:
#             return 'Invalid username or pasword'

# obj = Instagram('Aigerim', 'Mentor')
# print(obj.post_post('Django','Aigerim', 'Mentor'))

# obj1 = TikTok('Sultan', 'Katana')
# print(obj1.post_video('OOP', 'Sultan', 'Katana'))

'''>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''

'''CLASSWORK2'''

"""Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water.
Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.
"""

'''1)QUESTION'''

# class Auto:

#     def ride(self):
#         print('Riding on the ground')


# class Boat:

#     def swim(self):
#         print('Floating on water')


# class Amphibian(Auto, Boat):
#     pass


# obj = Amphibian()

# obj.ride()
# obj.swim()

'''2)QUESTION'''

"""Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина"""


# class RadioMixin:
#     def play_music(self, title):
        
#         print(f'Playing {title} music')

# class Auto(RadioMixin):
#     pass


# class Boat(RadioMixin):
#     pass

# class Amphibian(RadioMixin):
#     pass
# auto = Auto()
# auto.play_music("Rap God")

# boat = Boat()
# boat.play_music('Mockingbird')
# obj = Amphibian()
# obj.play_music("Dancing with your ghost")


'''3)QUESTION'''

"""Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник."""

# class Clock:
#     def current_time(self):
#         import datetime
#         dt_new = datetime.datetime.today().strftime('%H:%M:%S')
#         print(dt_new)

# class Alarm:
#     @staticmethod
#     def on():
#         print('Будильник включён')

#     @staticmethod
#     def off():
#         print('Будильник выключен')

# class AlarmClock(Clock, Alarm):
#     @staticmethod
#     def alarm_on():
#         Alarm.on()

# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()

    
'''4)QUESTION'''

"""Разработчики
Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). 
Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы."""



"""
Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 15%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
"""

'''5)QUESTION'''

# class Square:
#     def __init__(self, side):
#         self.side = side
    
#     def get_area(self):
#         return self.side**2

# class Triangle:
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base

    
#     def get_area(self):
#         return int(1/2*self.base*self.height)


# class Pyramid(Triangle, Square):
#     def __init__(self, height, base):
#         super().__init__(height, base)

#     def get_volume(self):
#         return int(1/3*self.base**2 * self.height)
    

# obj = Square(3)
# print(obj.get_area())

# obj1 = Triangle(3, 5)
# print(obj1.get_area())

# obj2 = Pyramid(5, 5)
# print(obj2.get_volume())


'''6)QUESTION'''

# class CreateMixin:
#     def create(self, key, todo):
#         if key in self.todos.keys():
#             return 'Задача под таким ключом уже существует'
#         self.todos[key] = todo
#         return self.todos
            
# class DeleteMixin:
#     def delete(self, key):
#         delete_ = self.todos.pop(key, 'нет такого ключа')
#         if 'нет такого ключа' == delete_:
#             return delete_
#         return delete_
            
# class UpdateMixin:
#     def update(self, key, new_value):
#         self.todos[key] = new_value
#         return self.todos
        
# class ReadMixin:
#     def read(self):
#         res = [x for x in self.todos.items()]
#         return sorted(res)
    
# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}
#     def set_deadline(self, deadline):
#         import datetime
#         time_ = datetime.datetime.now().strftime('%d/%m/%Y')
#         deadline = deadline.split('/')
#         time_ = time_.split('/')
#         deadline = list(map(int, deadline))
#         time_ = list(map(int, time_))
#         time_ = sum((time_[0], time_[1]*30, time_[2]*365))
#         deadline = datetime.date(deadline[2], deadline[1], deadline[0])
#         time_ = datetime.date.today()
#         return (deadline - time_).days
    
# task = ToDo() 
# print(task.set_deadline('31/12/2022'))
# print(task.create(1, 'todo'))
# print(task.delete(3))
# print(task.update(1, 'todo'))
# print(task.read())
# print(task.create(1, 'Do housework'))
# print(task.create(1, 'Do housework'))
# print(task.create(2, 'Go for a walk'))
# print(task.update(1, 'Do homework'))
# print(task.delete(2))
# print(task.read())
# print(task.set_deadline('31/12/2021'))


'''7)QUESTION'''

# class ExtensionMixin:
#     def add_extension(self, extension_name):
#         self.extensions.append(extension_name)
#         return f'Добавлено новое расширение {extension_name} для игры {self.name}.' 

#     def remove_extension(self, extension_name):
#         if extension_name in self.extensions:
#             self.extensions.remove(extension_name)
#             return f'{extension_name} был отключен от {self.name}'
        
#         else:
#             return 'Такого расширения нет в списке.'

# class Game(ExtensionMixin):
#     def __init__(self, game_type, name):
#         self.type = game_type
#         self.name = name
#         self.extensions = []
    
#     def get_description(self, description):
#         return f"{self.name} это {description}"
    
#     def get_extensions(self):
#         if len(self.extensions) == 0:
#             return "Нет подключенных расширений"
#         else:
#             return self.extensions





# game = Game('CS_GO', 'Minencraft')

# print(game.get_description('инди-игра в жанре песочницы с элементами выживания и открытым миром'))
# print(game.add_extension('Multiverse-Core'))
# print(game.add_extension('Multiverse-Core1'))
# game.extensions
# print(game.get_extensions())
# print(game.remove_extension('Multiverse-Core'))
# print(game.get_extensions())

'''8)QUOESTION'''

# class WalkMixin:

#     def walk(self):
#         print("я могу ходить")


# class FlyMixin:

#     def fly(self):
#         print("я могу летать")


# class SwimMixin:

#     def swim(self):
#         print("я могу плавать")

# class Human(WalkMixin, SwimMixin):
#     pass


# class Fish(SwimMixin):
#     pass

# class Exocoetidae(FlyMixin, SwimMixin):
#     pass

# class Duck(WalkMixin, FlyMixin, SwimMixin):
#     pass

# human = Human()
# human.walk
# human.swim
# fish = Fish()
# fish.swim

# exocoetidae = Exocoetidae()
# exocoetidae.fly
# exocoetidae.swim

# duck = Duck()
# duck.walk
# duck.fly
# duck.swim


# class CreateMixin:

#     def create(self, todo, key):
#         if key in self.todos.keys():
#             return "Задача под таким ключём уже существует"

#         else:
#             self.todos['key'] =todo
            
#             return self.todos



    

# class DeleteMixin:
#     def delete(self, todo, key):
#         self.todos.pop

# class UpdateMixin:
#     pass

# class ReadMixin:
#     pass

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}


'''SNIPER'''
# class Sniper:
#     health = 100

#     def __init__(self, name) -> None:
#         self.name = name

#     def shoot(self,other):
#         other.health-=20
#         print(f'Атоковал {self}')
#         print(f'Жертва: {other}, осталось здоровья: {other.health}')

#     def __str__(self) -> str:
#         return self.name


# sniper1 = Sniper('John')

# sniper2 = Sniper('Jamie')

# print(sniper1, sniper1.health)
# print(sniper2, sniper2.health)

# import random


# while sniper1.health and sniper2.health:
#     choice = random.randint(1,2)

#     if choice ==1:
#         sniper1.shoot(sniper2)

#     else:
#         sniper2.shoot(sniper1)

# if sniper1.health:
#     print(f'{sniper1} победиль!')

# else:
#     print(f'{sniper2} победиль!')



# class Person:
#     name = 'John'
#     def __init__(self, name, phone_number, card_number) -> None:
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number
#     def __validate_name(self):
#         if len(self.name) < 2:
#             return 'john'
#         else:
#             return self.name.capitalize()
            
#     def get_number(self):
#         return self.__card_number



# sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(f'{sam._Person__validate_name()}\n{sam._phone_number}\n{sam.get_number()}')

'''Incapsulation'''

'''3)QUESTION'''

# class Car:
#     __speed = 0

#     def set_speed(self, new):
#         self.__speed = new
#         return self.__speed


    
#     def show_speed(self):
#         return self.__speed


# car1 = Car()

# print(car1.show_speed())
# car1.set_speed(20)
# print(car1.show_speed())
 
'''4)QUESTION'''

# class Car:
#     __speed = 0
        
#     @property
#     def speed(self):
#         return self.__speed
    
#     @speed.setter
#     def speed(self, value):
#         self.__speed = value
        
    
#     def show_speed(self):
#         return self.speed

# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed) 


'''5) QUESTION'''

# class Person:
#     name = 'John'
#     _phone_number = '+996 557 55 17 57'
#     __card_number = '9999 9999 9999 9999'

#     def name1(self):
#         return self.name

#     def phone_number(self):
#         return self._phone_number


#     def card_number(self):
#         return self.__card_number



# john = Person()

# print(john.name1())
# print(john.phone_number())
# print(john.card_number())


'''6)QUESTION'''


# class Person:

#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number

# john = Person("John", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)


'''6)QUESTION also correct'''


# class Person:

#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number

#     def name1(self):
#         return self.name

#     def phone_number(self):
#         return self._phone_number

#     def card_number(self):

#         return self.__card_number

# john = Person("John", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(john.name1())
# print(john.phone_number())
# print(john.card_number())


'''7)QUESTION'''


# class Person:
#     name = 'John'
#     _phone_number = "+996 557 55 17 57"
#     __card_number =  "9999 9999 9999 9999"
#     @property
#     def name1(self):
#         return self.name

#     @name1.setter
#     def name1(self, new):
#         self.name = new
#         return self.name
#     @property
#     def phone_number(self):
#         return self._phone_number

#     @phone_number.setter
#     def phone_number(self, new):
#         self._phone_number = new
#         return self._phone_number

#     @property
#     def card_number(self):
#         return self.__card_number

#     @card_number.setter
#     def card_number(self, new):
#         self.__card_number = new
#         return self.__card_number


# john = Person()
# john.name = None
# john.card_number = None
# john.phone_number = None
# print(john.name)
# print(john.card_number)
# print(john.phone_number)

'''8)QUESTION'''

# class Person:

#     def __init__(self, name, phone_number, card_number):
#         self.name = self.__validate_name(name)
#         self._phone_number = phone_number
#         self.__card_number = card_number

#     def __validate_name(self, name):
#         if len(name) < 2:
#             return  'John'

#         else:
#             return name.title()

#     def get_card_number(self):
#         return self.__card_number


# sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")

# print(f'{sam.name}\n{sam._phone_number}\n{sam.get_card_number()}')

'''9)QUESTION'''

# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = self._validate_phone_number(phone_number)
#         self.__card_number = self.__validate_card_number(card_number)

#     def _validate_phone_number(self, phone_number):
#         if isinstance(phone_number, int):
#             if str(phone_number).startswith('996'):
#                 return phone_number
#         return None

#     def __validate_card_number(self, card_number):
#         if isinstance(card_number, int):
#             if len(str(card_number)) == 16:
#                 return card_number
#         return None

# tolik = Person('Tolik', '996 15 97 14', '9999 9999 9999 9999')

# print(tolik.name)
# print(tolik._phone_number)
# print(tolik._Person__card_number)


'''10)QUESTION'''

# class Game:
#     __level = 0

#     def __init__(self, name):
#         self.name = name

#     def play(self, hours):
#         if hours > 2:
#             self.__level+=1

#         else:
#             pass

#     def get_level(self):
#         return self.__level

# game = Game("Nuuman")
# print(game.get_level())
# print(game.play(3))
# print(game.play(3))
# print(game.get_level())

'''11)QUESTION'''

# class Game:
#     __level = 0

#     def __init__(self, name):
#         self.name = self.__validate_name(name)


#     def set_level(self, level):
#         if self.name == 'Tolik':
#             self.__level = level

#         else:
#             print(f"{self.name} ты не Tolik!")

#     def __validate_name(self, name):
#         return name.title()


# game = Game('Raychel')
# print(game.set_level(5))
# print(game._Game__level)

# game2 = Game('TOLIK')
# game2.set_level(5)
# print(game2._Game__level)


'''12)QUESTION'''


# class Game:
#     __level = 0

#     def __init__(self, name):
#         self.name = name

#     def get_level(self):
#         return self.__level

#     def set_level(self, value):
#         self.__level = value
#         return self.__level

# game = Game('Nuuman')
# print(game.get_level())
# print(game.set_level(5))
# print(game.get_level())


'''13)QUESTION'''

# class Game:
#     __level = 0

#     @property
#     def level(self):
#         return self.__level

# game = Game()
# print(game._Game__level)



'''14)QUESTION'''

# class Game:
    
#     __level = 0

#     @property
#     def level(self):
#         return self.__level

#     @level.setter
#     def level(self, value):
#         self.__level = value
#         return self.__level

# game = Game()
# print(game.level)
# game.level = 10
# print(game.level)


'''15)QUESTION'''


# class Person:

#     def __init__(self):
#         self.__name = None
#         self.__last_name = None
#         self.__age = None
#         self.__email = None

#     def get_name(self):
#         return self.__name

#     def set_name(self, value):
#         self.__name = value
#         return self.__name

#     def get_last_name(self):
#         return self.__last_name

#     def set_last_name(self, value):
#         self.__last_name = value
#         return self.__last_name

#     def get_age(self):
#         return self.__age

#     def set_age(self, value):
#         self.__age = value
#         return self.__age

#     def get_email(self):
#         return self.__email

#     def set_email(self, value):
#         self.__email = value
#         return self.__email

# john = Person()
# print(john.get_name())
# print(john.get_last_name()) 
# print(john.get_age())
# print(john.get_email())
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name())
# print(john.get_last_name()) 
# print(john.get_age()) 
# print(john.get_email()) 


'''16)QUESTION'''


# class Person:
#     def __init__(self):
#         self.__name = None
#         self.__last_name = None
#         self.__age = None
#         self.__email = None
    
#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, value):
#         self.__name = value
    
#     @property
#     def last_name(self):
#         return self.__last_name
    
#     @last_name.setter
#     def last_name(self, value):
#         self.__last_name = value
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, value):
#         self.__age = value
    
#     @property
#     def email(self):
#         return self.__email
    
#     @email.setter
#     def email(self, value):
#         self.__email = value

# john = Person()
# print(john.name)
# print(john.last_name) 
# print(john.age) 
# print(john.email)
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name) 
# print(john.last_name) 
# print(john.age) 
# print(john.email)



'''17)QUESTION'''

# class Dad:

#     name = "John"
#     _last_name = "Snow"
#     __age = 40

# class Me(Dad):


#     name = "Sam"
#     __last_name = "Snow"
#     __age = 10


#     def about_me(self):

#         print(f'My name is {self.name} {self._last_name} and I am {self.__age} years old')

#     def about_my_father(self):

#         print(f'My father is {Dad.name} {self._last_name}')


# me = Me()
# me.about_me()
# me.about_my_father()



# class MyString(str):
#     def __init__(self,word):
#         self. word = word

#     def append(self, str_):

#         self.word+=str_

#     def pop(self):

#         last_v = self.word[-1]
#         self.word = self.word[:-1]

#         return last_v

#     def __str__(self) -> str:
#         return self.word

# example = MyString('String') 
# example.append('hello')
# print(example.pop())
# print(example)



'''POLIMORPHISM'''

'''1)QUESTION'''

# a = 'makers'
# b = [1,2,3,4,5]
# c = {'a':1, 'b': 2, 'c': 3}

# list_ = [a, b, c]
# for x in list_:
#     print(len(x))


'''2)QUESTION'''

# class Dog:

#     def voice(self):
#         print('Гав')

# class Cat:

#     def voice(self):
#         print('Мяу')


# rex = Dog()
# barsik = Cat()

# def to_pet(animal):
#     animal.voice()

# to_pet(barsik) 
# to_pet(rex)


'''3)QUESTION'''

# class Person:

#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'


# class Employee(Person):

#     def __init__(self, name, last_name, work, status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status
    
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}'


# class Student(Person):

#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе'

# def get_human_info(value):

#     print(value.get_info())

# person = Person('Иван', 'Петров')

# employee = Employee('Иван', 'Петров', 'Рога и Копыта', 'директор')

# student = Student('Иван', 'Петров', 'КГТУ', 3)



# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person)


'''4)QUESTION'''

# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass

# class Triangle(Shape):

#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def get_area(self):

#         return 1/2*self.base*self.height


# class Square(Shape):
#     def __init__(self, base):
#         self.base = base
        

#     def get_area(self):

#         return self.base*self.base



# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):

#         return pi*self.radius**2


# triangle = Triangle(2, 4)
# square = Square(5)
# circle = Circle(3)

# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area())
 

'''5)QUESTION'''

# class OS:

#     def __init__(self, version):

#         self.version = version

    
# class Windows(OS):
    
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + C'



# class MacOS(OS):

#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами COMMAND + C'

# class Linux(OS):

#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'




# win = Windows(12)

# mac = MacOS(23)

# lin = Linux(45)

# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
 
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
 
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))


'''6)QUESTION'''


# class Language:

#     def __init__(self, level, type):
#         self.level = level
#         self.type = type


# class Python(Language):

#     def write_function(self, func_name, arg):
#         return f'def {func_name}({arg}):'

#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             return f"{var_name} = '{value}'"
#         else:
#             return f"{var_name} = {value}"


# class JavaScript(Language):

#     def write_function(self, func_name, arg):
#         return f'function {func_name}({arg}) {{     }};'

#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             return f"let {var_name} = '{value}';"

#         else:
#             return f"let {var_name} = {value};"


# py = Python('dfg', 'vb')
# js = JavaScript('dfgh0', 'cvb')

# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))

# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', 'john@123'))


'''7)QUESTION'''

# class Money:

#     def __init__(self, country, symbol):
#         self.country = country
#         self.symbol = symbol

    
# class Dollar(Money):
#     rate = 84.40
#     def exchange(self, amount):
#         return f'$ {amount} равен {amount*self.rate} сомам'



# class Euro(Money):
#     rate = 98.40

#     def exchange(self, amount):
#         return f'€ {amount} равен {amount*self.rate} сомам'

# dollar = Dollar("America", 'Dollar')

# euro = Euro('London', 'Euro')

# print(dollar.exchange(100))
# print(euro.exchange(80))


'''8)QUESTION'''

# class Planet:

#     def __init__(self, orbit):
#         self.orbit = orbit

# class Mercury(Planet):
#     def get_age(self, earth_age):
        
#         return  f'на Меркурии ваш возраст составляет {int(earth_age*365/self.orbit)} лет'
# class Venus(Planet):

#     def get_age(self, earth_age):
#         return f'на Венере ваш возраст составляет {round(earth_age*365/self.orbit*365)} дней'
# class Jupiter(Planet):                           
#     def get_age(self, earth_age):
#         return f'на Юпитере ваш возраст составляет {earth_age*365//self.orbit*365*24} часов'
        


# venus = Venus(225)
# print(venus.get_age(20))

# mercury = Mercury(88)
# print(mercury.get_age(20))

# jupiter = Jupiter(12)
# print(jupiter.get_age(20))


'''Методы класса, static, instance, class '''

'''1)QUESTION'''

# class Product:
#     base_price = 20000

#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
        
#     def has_garantiya(self, year):

#         a = year- self.year
#         if a>2:

#             return 'Ваша гарантия истекла'

#         else:
#            return 'Гарантия действительна'
#     @classmethod
#     def change_price(cls, rate):
#         cls.base_price  += cls.base_price*rate //100


# obj = Product('A218', 2008, 'red') 
# obj.change_price(2) 
# print(obj.has_garantiya(2010)) 
# print(obj.base_price)  

'''2)QUESTION'''

# class User:

#     def __init__(self, name, lastname, email):
#         self.name = name
#         self.lastname = lastname
#         self.email = email

#     @staticmethod
#     def validate_email(email):
#         return '@' in email

#     def __str__(self) -> str:
#         if self.validate_email(self.email):
#             return f'{self.name}:{self.email}'
#         else:
#             return 'email в неправильном формате'

#     @classmethod
#     def create_user(cls, str_):
#         a = str_
#         b = a.split(',')
#         name = b[0]
#         lastname = b[1]
#         email = b[2]
        
#         return cls(name, lastname, email)


# user1 = User.create_user('John, Snow, john@email.com')
# user2 = User.create_user('Sansa, Stark, sansaemail.com')

# print(user1)
# print(user2) 


'''3)QUESTION'''

# class Makers:
#     student_count = 0

#     def __init__(self, name, language, kpi):
#         self.name = name
#         self.language = language
#         self.kpi = kpi
#         Makers.student_count += 1

#     @classmethod
#     def new_student(cls, name, language, kpi):
#         return cls(name, language, kpi)
        
        

#     def get_info(self):
#         return f'Student name: {self.name}, Language: {self.language}'

#     def set_kpi(self, value):
#         self.kpi = value
#         return self.kpi

# student1 = Makers.new_student('vlad', 'Python', 26)
# student2 = Makers.new_student('Malik', 'JavaScript', 56)

# print(student1.set_kpi(89)) 
# print(student1.get_info()) 
# print(student2.set_kpi(89)) 
# print(student2.get_info()) 
# print(Makers.student_count) 


'''4)QUESTION'''


# class Bike:

#     def __init__(self, cost, make, model, year, min_profit):
#         self.cost  = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self._sale_price = None
#         self.sold = False
#         self.min_profit =min_profit 

#     def set_cost(self, price):
#         if self.cost < price:
#             self._sale_price = price
#         else:
#             self._sale_price = price + self.min_profit

#     def service(self, remont):
#         self._sale_price += remont
#         return self._sale_price

#     def sell(self):
#         self.sold = True
#         return self.cost - self._sale_price
        

#     @classmethod
#     def get_default_bike(cls):
#         bike = cls(10000, "Author", "Basic ASL", 2020, 2000)
#         return bike
    
# bike = Bike.get_default_bike() 
# bike.set_cost(6000) 
# bike.service(300) 
# print(bike.sell()) 
# print(bike.cost) 
# print(bike.make) 
# print(bike.year) 
# print(bike._sale_price) 
# print(bike.sold) 
# print(bike.min_profit) 


'''5)QUESTION'''

# class  MoneyFmt:
#     def __init__(self, amount) -> None:
#         self.amount = amount

#     @staticmethod
#     def dollarize(float_num): 
#         if float_num >= 0:
#             return "${:,.2f}".format(float_num)
#         else:
#             return "-${:,.2f}".format(-float_num)

#     def update(self, new_amount):
#         self.amount = new_amount
#         return self.amount

#     def __repr__(self) -> str:
#         return str(self.amount)
    
#     def __str__(self) -> str:
#         return self.dollarize(self.amount)

# cash = MoneyFmt(12345678.021) 
# print(cash) 
# cash.update(100000.4567) 
# print(cash) 
# cash.update(-0.3) 
# print(cash) 
# print(repr(cash))



# class Language:

#     def __init__(self, level, type):
#         self.level = level
#         self.type = type


# class Python(Language):
    
#     def write_function(self, func_name, arg):

#         return f'def {func_name}({arg}):'

#     def create_variable(self, var_name, value):
        
#         if isinstance(value, str):
#             return f'{var_name} = "{value}"'

#         else:
#             return f'{var_name} = {value}'





# class JavaScript(Language):

#     def write_function(self, func_name, arg):

#         return f'function {func_name}({arg}){{    }};'


#     def create_variable(self, var_name, value):
        
#         if isinstance(value, str):
#             return f'{var_name} = "{value}"'

#         else:
#             return f'let {var_name} = {value}'

# py = Python('dfg', 'fggh')
# js = JavaScript('ert', 'erty')

# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))

# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', 'john@123'))



# class Product:

#     base_price = 20000
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color

#     def has_garantiya(self, year):

#         garanty = year- self.year
#         if garanty >2:
#            return 'Ваша гарантия истекла'

#         return 'Гарантия действительна' 

#     def change_price(self, rate):
#         self.base_price *= rate


# obj = Product('A218', 2008, 'red') 
# obj.change_price(2) 
# print(obj.has_garantiya(2010)) 
# print(obj.base_price) 