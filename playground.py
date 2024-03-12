#creating a new line in python
print(" this is a line \nthis is another new line")
#If you don’t want characters prefaced by \ to be interpreted as special characters, 
#you can use raw strings by adding an r before the first quote:
print("C:\some\name")
print(r"C:\some\name")
# using triple-quotes: """...""" or '''...'''. and add \
#you can use it to print multiple lines
print("""\ 
      This is  a line                           AS YOU GO
      this is another line       as you go 
      
     """ )
#you can repeat a string using *
print(3 * "processing ")
