# #creating a new line in python
# print(" this is a line \nthis is another new line")
# #If you don’t want characters prefaced by \ to be interpreted as special characters, 
# #you can use raw strings by adding an r before the first quote:
# print("C:\some\name")
# print(r"C:\some\name")
# # using triple-quotes: """...""" or '''...'''. and add \
# #you can use it to print multiple lines
# print("""\ 
#       This is  a line                           AS YOU GO
#       this is another line       as you go 
      
#      """ )
# #you can repeat a string using *
# print(3 * "processing ")


# from tkinter import *

# window = Tk()
# window.title("Grid Layout Example")

# label1 = Label(window, text="Label 1")
# label1.grid(row=0, column=0)

# label2 = Label(window, text="Label 2")
# label2.grid(row=0, column=1)

# button = Button(window, text="Click Me!")
# button.grid(row=1, columnspan=2)

# window.mainloop()


from tkinter import *

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

def mark_completed():
    selected = listbox.curselection()
    if selected:
        listbox.itemconfig(selected, bg="green")

# Create the main window
root = Tk()
root.title("To-Do List")

# Create the task entry widget
task_entry = Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Create buttons for adding, deleting, and marking tasks as completed
add_button = Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=5, pady=5)

mark_button = Button(root, text="Mark Completed", command=mark_completed)
mark_button.grid(row=0, column=3, padx=5, pady=5)

# Create the listbox to display tasks
listbox = Listbox(root, width=50, height=10)
listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Run the main event loop
root.mainloop()