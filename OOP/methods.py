# Существует 3 вида методов.

# 1) class methods

# 2) instance methods

# 3) static methods

# 1) instance methods - обычные методы, которые принимает  первым аргументам self(ссылка на обьект).Нужны они для того чтобы внутри метода мы смогли работать с атрибутами обьекта.

# class A:

#     def instance_method(self):
#         print('метод обьекта')
#         print('первый аргумент:', self)

# obj_a = A()
# obj_a.instance_method() # если вызываем у обьекта, то self передается автоматически.

# A.instance_method(obj_a) # если вызываем у класса, то в self нужно передать обьект в ручную.

# 2) class methods -  методы которые принимает первым аргументам cls (ссылка на класс). Нужны они для создания обьектов или изменения аттрибутов класса. Для того тобы создать класс метод нужно воспользоваться декоратором @classmethod


# class B:

#     @classmethod
#     def class_method(cls, a):
#         print('класс метод')
#         print('первый аргумент:', cls)


# obj_b = B()
# obj_b.class_method(5)
# B.class_method(5)


# class C:
#     counter = 0

#     def __init__(self) -> None:
#         self._inc_counter()

#     @classmethod
#     def _inc_counter(cls):
#         cls.counter += 1



# obj = C()
# obj1 = C()
# obj2 = C()
# print(obj1.counter)
# print(C.counter)



# class Pizza:

#     def __init__(self, radius, *ingredients) -> None:
#         self.radius = radius
#         self.ingredients = ingredients

#     def cook(self):
#         print(f'Готовится пицца размером {self.radius * 2} см')

#     @classmethod
#     def four_cheece(cls, radius):
#         pizza = cls(radius, 'моцарела', 'чедер', 'голландский', 'брынза')
        
#         return pizza




# pizza1 = Pizza(17, 'пеперони', 'моцарела', 'грибы')

# pizza2 = Pizza(15, 'моцарела', 'чедер', 'голландский', 'брынза')

# pizza2 = Pizza(40, 'моцарела', 'чедер', 'голландский', 'брынза')

# pizza2 = Pizza.four_cheece(15)

# pizza3 = Pizza.four_cheece(20)

        

# class Person:

#     surname = 'Stark'

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_date(cls, name, date_birth):
#         from datetime import date
#         age = date.today().year - date_birth
#         return cls(name, age)


# obj = Person('John', 24)
# print(obj.name, obj.surname, obj.age)

# obj2 = Person.from_birth_date("Sansa", 1961)
# print(obj2.name, obj2.surname, obj2.age)

# 3) staticmethod - просто функции внутри класса, которые не взаимодейсктуют ни с классом, ни с обьектом. Находяться они внутри класса лишь потому что их используют только внутри класса, так как они вне бесполезны.

# @staticmethod - декоратор

# class C:

#     @staticmethod
#     def static_method():
#         print('Статический метод')


# obj = C()
# obj.static_method()
# C.static_method()


# class Cylinder:

#     def __init__(self, diameter, height) -> None:

#         self.diameter = diameter
#         self.height = height
#         self.area = self.get_area(self.diameter, self.height)

#     @staticmethod
#     def get_area(diameter, height):
#         from math import pi

#         circle = pi * (diameter/2) ** 2
#         side = pi * height * diameter
#         area =  circle * 2 + side
#         return round(area, 2)


# obj = Cylinder(10, 7)
# print(f'Area: {obj.area}')

# obj1 = Cylinder(4, 10)
# print(f'Area: {obj1.area}')




