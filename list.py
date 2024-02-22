fruits = ["Apple", "Banana", "Cherry", "pineapple", "Cherry"] 
#fruit is like a box conataining objects of various data types
print(fruits)
print(len(fruits))
#the len gives the number of objects in the list constructor
print(type(fruits)) 
#the type is used to determine the type of data structure 

newlist = list(("apple", "banana", "cherry"))
print(newlist)

#accessing an object from a list
print(newlist[2])

#accesing objects using range
print(fruits[1:4])

#using for loop
for x in fruits[1:4]:
    print(x)





