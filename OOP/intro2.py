# # # # class Human:
# # # #     age = 0 
    
# # # #     def __init__(self, name, last_name, weight, natinoality) -> None:
# # # #         self.name = name = name + ' ' +last_name
# # # #         self.weight = weight
# # # #         self.nation = natinoality



# # # #     def birhday(self):
# # # #         import random
# # # #         print(f'Happy birthday, {self.name}!!!')
# # # #         self.age += 1
# # # #         self.weight = random.randint(3, 6)


# # # # human1 = Human('John', 'Snow', 3.300, "American")
# # # # human2 = Human('Abu', "Bark", 3.8, "Arabic")
# # # # print(human1.name, human1.age, human1.weight, human1.nation)
# # # # print(human2.name, human2.age, human2.weight, human2.nation)
# # # # human1.birhday()
# # # # human2.birhday()
# # # # human1.birhday()
# # # # human2.birhday()
# # # # human1.birhday()


# # # # print('After 1 year:')
# # # # human1.birhday()
# # # # human2.birhday()
# # # # print(human1.name, human1.age, human1.weight, human1.nation)

# # # # print(human2.name, human2.age, human2.weight, human2.nation)


# # # '----------------------------------------------------------'


# # # class Student:
# # #     univer = "MIT"


# # #     def __init__(self, name, last_name) -> None:
# # #         self.name = f'{name} {last_name}'
# # #         self.books = []
# # #         self.language = {}
# # #         self.knowledge = 0
# # #         self.isreadytowork = False 



# # #     def add_points(self, points):
# # #         self.knowledge += points
# # #         if self.knowledge >500:
# # #             self.isreadytowork = True
# # #             print(f'{self.name} is ready to work!!')


# # #     def read_book(self, book):
# # #         self.books.append(book)
# # #         self.add_points(50)


# # #     def do_lab_work(self):
# # #         self.add_points(50)


# # #     def do_project(self):
# # #         self.add_points(100)


# # #     def lear_new_language(self, language, point):
# # #         if not point in range(70, 101):
# # #             raise Exception('Invalid points')

# # #         else:
# # #             self.language[language] = point
# # #             self.add_points(point)

# # # stud1= Student('John', 'Snow')
# # # stud2 = Student('Jamie', 'Lanister')

# # # print(stud1.name)
# # # print(stud2.name)
# # # print(f'Before study {stud1.name}',  stud1.books, stud1.language, stud1.knowledge)

# # # print(f'Ready to work: {stud1.isreadytowork}!')

# # # stud1.read_book('GOT')
# # # stud1.read_book('Martin Iden')
# # # stud1.read_book('Alghoritms and Data Structures')
# # # stud1.read_book('Eugene Onegin')

# # # stud1.do_lab_work()
# # # stud1.do_lab_work()
# # # stud1.do_project()
# # # stud1.lear_new_language('Python', 90)
# # # stud1.lear_new_language('C++', 75)


# # # print(f'After study {stud1.name}',  stud1.books, stud1.language, stud1.knowledge)

# # # print(f'Ready to work: {stud1.isreadytowork}!')

# # '--------------------------------------------------'


# # class Car:


# #     def __init__(self, brand, model) -> None:
# #         self.brand = brand
# #         self.model = model

# #     def __str__(self) -> str:
# #         return f'{self.brand} -> {self.model}'



# # obj = Car('BWM', '7 series')
# # obj1 = Car('Mercedes - Benz', 'w140')
# # obj2 = Car('KIA', 'K8')


# # print(obj)
# # print(obj1)
# # print(obj2)



# class Soda:


#     def __init__(self, ingredient = None):
#         if isinstance(ingredient,str):
#             self.ingredient = ingredient

#         else:
#             self.ingredient = None


#     def show_my_drink(self):
#         if self.ingredient:
#             print((f'Gazirovka iz {self.ingredient}'))

#         else:
#             print(f'Normal gazirovka')


# a = Soda('Malina')

# a.show_my_drink()

# b = Soda('apple')

# b.show_my_drink()
        


# class A:
#     ...



# a = A()
# b= 5
# print(isinstance(a, A))


# class TriangleCheker:
#     def __init__(self, sides:list) -> None:
#         self.sides = sides

    
#     def __str__(self) -> str:
#         if not all(isinstance (x, (int, float)) for x in self.sides):
#             return 'Нельзя построить треугольник! Так как все сторорны должны быть числами!'

#         if any (x<=0 for x in self.sides):
#             return 'Нельзя построит треугольника! Так как ысе стороны должны быть больше нуля!'

#         self.sides.sort()
#         if self.sides[0]+ self.sides[1] <= self.sides[-1]:
#             return 'Нельзя построить треугольника! Так как сумма двух сторон должна быть больше самой длинной стороны!'

        
#         else:
#             return 'Мы можем построит треуголь'




# t1 = TriangleCheker([19, 6, 8])
# print(t1)

# dict_ = {1:'one', 4:'two', 3: 'three'}
# print(sorted(dict_))