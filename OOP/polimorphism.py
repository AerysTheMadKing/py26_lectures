# функция полиморфизма - len()

# print(len('makers'))

# print(len([1,2,3,4,5]))
# print(len({1: 2, 3: 4}))

# +(__add__) метод полимофизма

# print(5 + 5)

# print('hello' + 'world')

# print([1,2,3,4] + [5,6,7,8])


# Полиморфизм - способность метода обрабатываеть данные разных типов(обьектов от класса), обычно это реализуется путем создания базового класса и наличия двух или более подклассов, которые все реализуют(переопределяют) методы с одинаковой сигнатурой(названием)
# 
# Широко распрастраненное определениие:'Один интерфейс - много реализации' 



# class Animal:

#     def info(self):
#         pass

#     def make_sound(self):
#         pass


# class Dog(Animal):
    
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s a dog. Dogs name is {self.name}, age {self.age}')


#     def make_sound(self):
#         print('Bark bark')



# class Cat(Animal):
    
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s a cat. Cats name is {self.name}, age {self.age}')


#     def make_sound(self):
#         print('meow meow')



# cat = Cat('Garfild', 5)

# dog = Dog('Pluto', 9)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()
#     print()




# class A:

#     def __len__(self):
#         return  123



# a = A()
# str1 = 'makers'
# print(len(str1))
# print(len(a))

# Абстракция(Абстрактный класс) - его можно рассматривать как набор методов, которорые должны быть реализованы во всех дочерний классах, которые  будуть унаследованы от абстрактного класса.

# Абстрактный метод - это метод у которого есть обьявление но нет реализации.

# from abc import ABC, abstractmethod

# from math import pi


# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name

#     @abstractmethod
#     def area(self):
#         pass


#     @abstractmethod
#     def info(self):
#         pass


# class Square(Shape):

#     def __init__(self, lenght) -> None:
#         super().__init__('Квадрат')
#         self.lenght = lenght

#     def area(self):
#         return self.lenght**2

#     def info(self):
#         print(f'Я {self.name}, у меня все углы равны 90 градусам!!')

    

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Окружность')
#         self.radius = radius

#     def area(self):
#         return pi * self.radius**2

#     def info(self):
#         print(f'Я {self.name}, и я фигура в двумерной плосткости !') 

# a = Square(4)
# b = Circle(4)

# for x in (a, b):
#     x.info()
#     print(x.area())

#     print()


# from abc import ABC, abstractmethod

# class ChessPiece(ABC):

#     def take(self):
#         print('Take a chess piece !')

#     # Abstract method  - который необходимо переопределять для каждого наследника.
#     @abstractmethod
#     def move(self):
#         pass






# class Queen(ChessPiece):

#     def move(self):
#         print('Queen moves where she wants diagonally, vertically and horizontally !')

# class Pawn(ChessPiece):
#     def move(self):
#         print('The pawn can move directly to one cell !')

# q = Queen()
# p = Pawn()

# q.move()
# q.take()
# print()
# p.move()
# p.take()




# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.


# class Phone:
#     def __init__(self, os, imei):
#         self.__imei = imei
#         self.__battery_level = 100
#         self.__os = os

#     @property
#     def battery_level(self):
#         if self.__battery_level < 0.5:
#             self.__battery_level = 0
#             raise Exception('Telefon razryazhen!')
#         self.__battery_level -= 0.5
#         print(self.__battery_level)
        
#     @property
#     def get_info(self):
#         if self.__battery_level < 0.5:
#             self.__battery_level = 0
#             raise Exception('Telefon razryazhen!')
#         self.__battery_level -= 0.5
#         print(f'OS: {self.__os}, IMEI: {self.__imei}')

#     def play_music(self):
#         if self.__battery_level <= 5:
#             self.__battery_level = 0
#             raise Exception ('Telefon razryazhen!')
#         self.__battery_level -= 5
#         print('Slushaem Mirbeka Atabekova!')

#     def play_video(self):
#         if self.__battery_level <= 10:
#             raise Exception ('Nedopustimyi uroven zaryada!')
#         self.__battery_level -= 7
#         print('Smotrim Toples!')

#     def charge_battery(self, sec):
#         from time import sleep
#         i = 1
#         while i <= sec:
#             sleep(1)
#             if self.__battery_level <100:
#                 self.__battery_level += 1
#                 if self.__battery_level > 100:
#                     self.__battery_level = 100
#             print(f'Zaryad idet! Vash uroven zaryada: {self.__battery_level}')
#             i += 1

# phone = Phone('IOS 15', '241325-113')
# phone.battery_level
# phone.get_info
# phone.play_music()
# phone.play_video()
# phone.battery_level
# phone.charge_battery(20)
# phone.battery_level

    


``


"""
1) Реализуйте программу по следующему описанию. Есть классы WhatsApp, SnapChat, Telegram. При регистрации в WhatsApp и SnapChat необходимо передавать свой номер телефона, который должен быть int. При регистрации в Telegram необходимо передавать номер телефона и username. Во всех классах есть метод send, в WhatsApp он принимает только text и выдает строку “I am sending a text ...” и вместо … должен быть сам текст сообщения. В SnapChat send принимает image и text, при этом image должен быть булевым типом данных. Если image True, то выдается сообщение “I am sending a text … with some image ”, если  False - сообщение “I am sending a text … without image”. В Telegram метод send принимает voice message в виде строки и выдает сообщение “I am sending a voice message ...”. Создайте объекты от этих классов и вызовите метод send у всех объектов.
"""

# class WhatsApp:

#     def registration(self):
#         date = int(input('Enter your number for WhatsApp registration: '))
#         print(date)


#     def send(self, text):
#         if isinstance(text, str):
#             print(f'I am sending a text {text}')
#         else:
#             print(None)

# class SnapChat:

#     def registration(self):
#         date = int(input('Enter your number for SnapChat registration: '))
#         print(date)

#     def send(self, image, text):
#         if isinstance(image, bool) and (text, str):
#             if image == True:
#                 print(f'I am sending a text {text} with some image')
                
#             else:
#                 print(f'I am sending a text {text} without image')

#         else:            print(None)

# class Telegram:
#     def registration(self):
#         date = int(input('Enter your number for Telegram registration: '))
#         date1 = input('Enter your Telegram username: ')
#         print(date, date1)
        

#     def send(self, voice_message):
#         if isinstance(voice_message, str):
#             print(f'I am sending a voice message "{voice_message}"')
#         else:
#             print(None)

# whatsApp = WhatsApp()

# snapChat = SnapChat()

# telegram = Telegram()



# whatsApp.registration()
# whatsApp.send('Hello World')
# print()
# snapChat.registration()
# snapChat.send(False, 'Future')
# print()
# telegram.registration()
# telegram.send('Lectures')

"""
2) Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count, а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов и вызовите этот метод у каждого объекта.
"""

# class A:

#     def count(self,text):
#         vowels = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
#         number_of_vowels = []
#         for x in vowels:
#             if x in text:
#                 number_of_vowels.append(x)

#         return f'Количество гласных {len(number_of_vowels)}'
        

# class B:

#     def count(self,text):
#         consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с',   'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
#         number_of_consonants = []
#         for x in consonants:
#             if x in text:
#                 number_of_consonants.append(x)

#         return f'Количество согласных {len(number_of_consonants)}'


# a = A()
# b = B()

# for x in (a, b):
#     print(x.count('apple'))
    


    