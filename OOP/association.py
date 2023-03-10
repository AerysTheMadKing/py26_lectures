# Ассоcaция - означает что внутри одного обьекта будет существовать другой обьект в качестве аттрибута.

# 1)Композиция - сильная связь

# 2)Агрегация - слабая связь


# Композиция это когда стена не существует отдельно от комнаты. Она создается при создании комнаты и польностью управляется классом комнаты.


# class Wall:

#     def __init__(self, direction) -> None:
#         self.type = direction


#     def __str__(self) -> str:
#         return f'{self.type} wall'

#     def info(self):
#         print('White wall')


# class Room:

#     def __init__(self) -> None:
        
#         self.west_wall = Wall('west')
#         self.east_wall = Wall('east')
#         self.south_wall = Wall('south')
#         self.north_wall = Wall('north')



# room = Room()

# print(room.west_wall)
# print(room.north_wall)
# print(room.north_wall.type)
# room.north_wall.info()


# Агрегация это когда экземпляр двигателя создается где то в другом месте, и передается в класс Авто в качестве параметре.

# class Engine:

#     country = 'Germany'

#     def __init__(self, power) -> None:
#         self.power = power

#     def __str__(self) -> str:
#         return f"Engine: {self.power}"

    

# class Car:

#     model = 'Audi'
#     country = 'Germany'

#     def __init__(self, type, engine) -> None:
#         self.type = type
#         self.engine = engine

         
#     def __str__(self) -> str:
#         return f'{self.model} {self.type} -> Engine: {self.engine} {self.engine.country}'


# engine = Engine(500)
# car = Car('A8', engine)
# print(car)
        
#-----------------------------------------------

# class Battery:

#     _power = 100

#     def power(self):

#         if self._power < 100:
#             self._power = 100

    
# class Iphone:

#     def __init__(self, color) -> None:
#         self.color = color
#         self.battery = Battery()
#         # Когда мы создаем обьект внутри - Это композиция

# class Nokia:

#     def __init__(self, color: str, battery: Battery) -> None:
#         self.color = color
#         self.battery = battery
#         # Когда принимаем в качестве параметра - это агрегация

# iphone = Iphone('Gray')
# del iphone

# # при удалении iphone вместе с ним удаляется и battery

# battery = Battery()
# nokia= Nokia('black', battery)
# del nokia

# # при удалении нокии батарейка остается

# nokia = Nokia('white', battery)


        


        