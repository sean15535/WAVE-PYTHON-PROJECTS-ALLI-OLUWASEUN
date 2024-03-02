my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict['name'])
#adding a value to a dictionary
my_dict["email"] = "john@mail.com"
#modifying a value in a dictionary
my_dict['age'] = 32
print(my_dict)
#removing elements from the dictionary using the del keyword or the pop() method:
del my_dict["age"]
print(my_dict)
#using pop method to remove elements in dictionary
my_dict.pop("city")
print(my_dict)
#Iterating Over a Dictionary using key()

