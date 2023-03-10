# ООП - Обьектно - ориентированное программирование

# 1) Класс -> Это описание того, как должен выглядеть обьект, то есть в классе мы описываем какими свойствами (данными) и поведением(функциями) должен обладать обьект.

# 2) Обьект -> Это сущность которую мы создаем от класса, у обьекта есть состаяние свойств(данных).


# Целью создание было связать данные(атрибуты) с функциями(методы) которые использовали их.


# Свойствами(аттрибуты) - называют обычные переменные внутри класса, в которых храняться данные определенного обьекта.


# Методы - это обычные функции которые описывают поведение обьекта, функции внутри класса называют методами.


# john = ['John', 'Snow', 'King of North', 5000, 30]

# def show_info(human):
#     print(f'Name: {human[0]} {human[1]}, Age: {human[-1]}, Job: {human[2]}, Salary: {human[3]}')


# show_info(john)


# class Human:


#     def __init__(self, name, last_name, age, job, salary) -> None:
#         self.name = name + ' ' + last_name
        
#         self.age = age
#         self.job = job
#         self.salary = salary


#     def show_info(self):
#         return f'Name:{self.name}, Age: {self.age}, Job: {self.job}, Salary: {self.salary}'


# john = Human('John', 'Snow', 30, 'King of North', 5000)
# sultan = Human('Sultan', 'Katana', 19, 'Mentor', 100)

# print(john.show_info())
# print(john.name)
# print(john.age)
# print('---------')
# print(sultan.show_info())
# print(sultan.name)


'--------------------------------------------------------------'

# class Dog:

#     # аттрибуты класса (переменные)
#     age = 0
#     ushi = True

#     def __init__(self, name, color) -> None:
#         '''Инициализатор, именно здесь создаются аттрибуты обьекта'''
#         # в self пролетает ссылка на обьект от класса 
#         self.name = name # атрибуты обьекта
#         self.color = color 



#     def bark(self):
#         print(f'{self.name} лает!')


# bobik = Dog('Bobik', 'Brown')
# yumi = Dog(name = 'Yumi', color = 'white')
# aktosh = Dog('Aktosh', 'gray')


# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi: {bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi: {yumi.ushi}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ushi: {aktosh.ushi}')


# bobik.age = 2
# yumi.age = 1
# aktosh.age = 3

# aktosh.ushi = False

# print("After")


# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi: {bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi: {yumi.ushi}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ushi: {aktosh.ushi}')


# aktosh.bark()




# class Human:
#     age = 0

#     def __init__(self) -> None:
#         print('init worked')
#         self.raychel = 'raychel'

#     def method1(self):
#         self.john ='john'
#         print('method 1 worked')


# obj = Human()
# print(obj.raychel)
# obj.method1()
# print(obj.john)


