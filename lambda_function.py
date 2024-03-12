# A lambda function is defined using the keyword `lambda`, followed by the arguments and the expression.
# x = lambda a: a + 10
# print(x(5))
# Lambda functions can take multiple arguments.
# x = lambda a, b: a * b
# print(x(5, 6))

#lambda can take a variable and act as a function
# def myfunc(n):
#     return lambda a: a * n

# x = myfunc(2)
# print(x(11))
# y = myfunc(3)
# print(y(11))
# #using lambda in loop
# for i in range(1,6):
#     x = lambda i:i*5
#     print (x(i))

# numbers = [1,2,3,4,5,6,7,8,9]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

numbers = [1,2,3,4,5,6,7,8,9]
for x in numbers:
    even_numbers = lambda x: x % 2 == 0
    a = even_numbers(x)
    print(list[a])

# numbers = [1,2,3,4,5,6,7,8,9]
# for x in numbers:
#     even_numbers =  x % 2 == 0
#     print(even_numbers)


