# fruits = ["Apple", "Banana", "Cherry", "pineapple", "Cherry"] 
# #fruit is like a box conataining objects of various data types
# print(fruits)
# print(len(fruits))
# #the len gives the number of objects in the list constructor
# print(type(fruits)) 
# #the type is used to determine the type of data structure 

# newlist = list(("apple", "banana", "cherry"))
# print(newlist)

# #accessing an object from a list
# print(newlist[2])

# #accesing objects using range
# print(fruits[1:4])

# #using for loop
# for x in fruits[1:4]:
#     print(x)

#adding to a list : append
# fruits = ['grape', 'cherry', 'apple']
# fruits.append('pawpaw')
# print(fruits)

#clear a list
# fruits = ['grape', 'cherry', 'apple', 'pawpaw']
# fruits.clear()
# print(fruits)

#pop
my_list =[1,2,3]
print(my_list.pop(2))

#index
# my_list = [1,2,3,4,]
# print(my_list.index(3))

#sort
# city = ["abule", "berger", "agege"]
# city.append("akowonjo")
# city.sort()

#reverse
# city.reverse()
# print(city)

#copy list
# original_list = [1,2,3]
# copied_list = original_list.copy()

# #count
# my_list = [1,2,3,2]
# count= my_list.count(2)
# print(count)

# #remove
# my_list = [1,2,3,2]
# count= my_list.remove(2)
# print(count)

# #enumerate
# my_list = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(my_list):
#     print(f"Index: {index}, Fruit: {fruit}")