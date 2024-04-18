from tkinter import *
from tkinter import messagebox
import random

# Create the main Tkinter window
root = Tk()
root.title("Bokku Supermarket POS")
root.geometry('1280x720')
bg_color = 'white'


# Initialize Tkinter variables
c_name = StringVar()
c_phone = StringVar()
item = StringVar()
rate = IntVar()
quantity = IntVar()
bill_no = StringVar()
bill_no.set(f"{random.randint(1000, 9999)}")

# List to store the prices of items in the bill
bill_items = []

# Create the main frame
main_frame = Frame(root, bg='white')
main_frame.pack(fill=BOTH, expand=True)

# Create the title label
title_label = Label(root, text="Bokku Supermarket POS", bg='#6A24FF', fg='white', font=('times new roman', 25, 'bold'), justify=CENTER)
title_label.pack(fill=X)

# Start the Tkinter event loop
root.mainloop()