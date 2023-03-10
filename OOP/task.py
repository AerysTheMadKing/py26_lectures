"""
5)Перепишите класс Car из предыдущего задания.
Перепишите метод set_speed() с использование декоратора @speed.setter, а метод show_speed() с использованием декоратора @property, для того чтобы можно было работать с данным классом следующим образом:

car = Car()
car.speed = 120
print(car.speed)
"""

# car = Car()
# car.speed = 120
# print(car.speed)


# class Car:

#     def __init__(self, speed) -> None:
#         self.__speed = speed

#     @property
#     def speed(self):
#         return self.__speed

#     @speed.setter
#     def speed(self, value):
#         self.__speed = value


    
# car = Car(120)
# print(car.speed)
# car.speed = 150
# print(car.speed)


def func():
    print("Hello world")
    return func
    

func()()()()

