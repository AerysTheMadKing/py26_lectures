"------------------------------------------ TUPLE() --------------------------------------"

#tuple() -> кортеж, неизменяемый тип данных. # tuple = (,)

# thistuple = ("apple")
# print(thistuple)
# print(type(thistuple))


# mytuple = ("apple", "orange")
# print(mytuple)
# print(type(mytuple))


# a, b, c = 5, 10, 15
# print(a)
# print(b)
# print(c)



# for x in range(1, 5): #x = 1  # = 3
#     print(x)          #x = 2  # = 4


# dict1 = {1: "one", 2: "two", 3: "three"}
# print(dict1.items())

# for x ,y in dict1.items():  # 1 one
#         print(x, y)         # 2 two
#                             # 3 three


# a = [(1,2), (3,4), (5,6)]
# for x , y in a:
#     print(x, y)   #1 2
#                   #3 4 
#                   #5 6




# ls = [1, 2, 3, 4, 5, 6, 7]

# tp = (1, 2, 3, 4, 5, 6, 7)


# print("LIST", ls.__sizeof__())  # LIST 104
# print("TUPLE", tp.__sizeof__()) # TUPLE 80



# ls = list(range(1, 100_001))
# tp = tuple(range(1, 100_001))

# print("LIST", ls.__sizeof__())  #LIST 800040

# print("TUPLE", tp.__sizeof__()) #TUPLE 800024


# tuple_ = (1,2,3,4,5) 
# ls = [1,2,3,4,5]
# del ls[-1]
# print(ls)  #[1, 2, 3, 4]


# tuple_ = (1,2,3,4,5) #неизменяемый
# del tuple_[-1]
# print(tuple_)  #'tuple' object doesn't support item deletion



# tuple_ = (1,2,3,4,5,6,7,8)
# print(tuple_.index(5)) # 4
# print(tuple_.count(2)) # 1


# tp = ("apple", "cherry", "banana", "john")
# for x in tp:
#     print(x)
#     print(x*3)



# i = 0
# while i<50:
#     print(i)
#     i+=1 # инкримент i i + 1
#          # дискримент i+=1


# tp = ("apple", "cherry", "banana", "john")
# x = 0
# while x < len(tp):
#     print(tp[x])

#     x += 1

" + * "

# a = (1,2,3)
# # b = (4,5,6)
# # print(a+b)  # (1, 2, 3, 4, 5, 6)
# # print(a*b) # error
# print(a*3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)




#1) input:

# tp  = (1,8,3,4,5,8,8,9,2)
# target = 8

# output: result = (8,3,4,5,8)

#2)input
# tp = (1,2,3,8,5,1,2)
# target = 8
# output: result = (8,5,1,2)


# tp  = (1,8,3,4,5,8,8,9,2)
# target = 8

# if tp.count(8) > 1:
#     first = tp.index(8)
#     second = tp.index(8, first + 1)
#     # print(first, second)

#     result = tp[first:second + 1]
#     # print(result)  # (8, 3, 4, 5, 8)

# else: 
#     first = tp.index(8)
#     result = tp[first:]
#     print(tp, target)
#     print(result)



# Given an array of integers nums and an integer target, return indices 
#  the two numbers such that they add up to target.


# nums = [2,7,11,15]
# target = 9
# for x in nums:
#     num= (target-x)
#     if num in nums:
#         print(nums.index(x),nums.index(num))

#         break








































