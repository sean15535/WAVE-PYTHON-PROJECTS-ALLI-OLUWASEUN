# from tkinter import *
# from tkinter import ttk

# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

from tkinter import *
from tkinter import messagebox

def message():
    response  = "Message Saved"
    # word.config(text=response)
    messagebox.showinfo("Message", response)

window = Tk()
window.minsize(width=500, height=500)
window.title('Python App')
word = Label(text = "Enter Username")
word.pack()
input = Entry()
input.pack()
button =Button(text="Click", command=message)
button.pack()
window.mainloop()
