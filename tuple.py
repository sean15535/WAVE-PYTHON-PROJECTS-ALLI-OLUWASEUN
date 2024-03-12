# a = (1,2,3)
# b=(4,5,6)
# print(a+b)
fruit = ("banana", True, 23, 45.76)
new_fruit = list(fruit)
print(fruit)
print(type(fruit))
print(new_fruit)
print(type(new_fruit))

tuple = [(1,2), (2,3), (1,6), (3,2),(4,1)]
for index, value in tuple:
    print(index , value)