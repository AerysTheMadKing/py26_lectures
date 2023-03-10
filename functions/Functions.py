# user = int(input("Emter smt: "))
# n = 0
# while n<user:
#     n+=1
#     print(n* "*")




# 2)
# user = int(input("Enter number: "))
# for x in range(0, user+1):
#     if x % 2 == 0:
#         print(f"{x} is EVEN")

#     else:
#         print(f"{x} is ODD")
 
from functools import reduce
list_ = ['a', 'n', 'n', 'a']
result = reduce(lambda x, y: x+y, list_)

if result == result[::-1]:
    print("YES")

else:
    print("NO")