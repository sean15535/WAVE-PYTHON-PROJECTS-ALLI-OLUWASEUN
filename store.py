from tkinter import *
from tkinter import messagebox
import random

# Function to display payment method selection popup
def pay_method_popup():
    # Create a new Toplevel window
    payment_window = Toplevel(root)
    payment_window.title("Select Payment Method")
    payment_window.geometry("300x200")

    # Function to handle payment method selection
    def process_payment(method):
        messagebox.showinfo("Payment", f"Payment method selected: {method}")

    # Create buttons for payment methods
    btn_cash = Button(payment_window, text="Cash", command=lambda: process_payment("Cash"))
    btn_cash.pack(pady=10)

    btn_credit_card = Button(payment_window, text="Credit Card", command=lambda: process_payment("Credit Card"))
    btn_credit_card.pack(pady=10)

    btn_cancel = Button(payment_window, text="Cancel", command=payment_window.destroy)
    btn_cancel.pack(pady=10)

# Function to add an item to the bill
def add_item():
    # Calculate the total price for the item
    total_price = rate.get() * quantity.get()
    # Append the total price to the list
    bill_items.append(total_price)
    # Insert the item details into the text area
    if item.get() != '':
        bill_text_area.insert(END, f"{item.get()}\t\t{quantity.get()}\t\t{total_price}\n")
    else:
        messagebox.showerror('Error', 'Please enter item')

# Function to generate the bill
def generate_bill():
    # Check if customer details are provided
    if c_name.get() == "" or c_phone.get() == "":
        messagebox.showerror("Error", "Customer details are required")
    else:
        # Display the total bill amount
        total_amount = sum(bill_items)
        bill_text_area.insert(END, f"\n======================================")
        bill_text_area.insert(END, f"\nTotal Paybill Amount :\t\t      {total_amount}")
        bill_text_area.insert(END, f"\n\n======================================")
       

# Function to clear all input fields
def clear_fields():
    c_name.set('')
    c_phone.set('')
    item.set('')
    rate.set(0)
    quantity.set(0)
    welcome_message()

# Function to exit the application
def exit_application():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.destroy()

# Function to save the bill to a file
def save_bill():
    if messagebox.askyesno("Save Bill", "Do you want to save the Bill?"):
        bill_details = bill_text_area.get('1.0', END)
        with open(f"bills/{bill_no.get()}.txt", "w") as file:
            file.write(bill_details)
        messagebox.showinfo("Saved", f"Bill no. {bill_no.get()} saved successfully")

# Function to display welcome message and bill number
def welcome_message():
    bill_text_area.delete(1.0, END)
    bill_text_area.insert(END, "\t  Welcome to Bokku Store")
    bill_text_area.insert(END, f"\n\nBill Number:\t\t{bill_no.get()}")
    bill_text_area.insert(END, f"\nCustomer Name:\t\t{c_name.get()}")
    bill_text_area.insert(END, f"\nPhone Number:\t\t{c_phone.get()}")
    bill_text_area.insert(END, f"\n\n======================================")
    bill_text_area.insert(END, "\nProduct\t\tQTY\t\tPrice")
    bill_text_area.insert(END, f"\n======================================\n")
    bill_text_area.configure(font='arial 15 bold')

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
bill_no.set(str(random.randint(1000, 9999)))

# List to store the prices of items in the bill
bill_items = []

# Create the main frame
main_frame = Frame(root, bg='white')
main_frame.pack(fill=BOTH, expand=True)

# Create the title label
title_label = Label(main_frame, text="Bokku Supermarket POS", bd=12, bg='#6A24FF', fg='white', font=('times new roman', 25, 'bold'), relief=GROOVE, justify=CENTER)
title_label.pack(fill=X)

# Create the Exit button
btn_exit = Button(main_frame, text='Exit', font='arial 10 bold', command=exit_application, bg='red', width=10)
btn_exit.pack(side=RIGHT, padx=(0, 10), pady=(10, 0))


# Create the customer details frame
customer_details_frame = LabelFrame(main_frame, bd=10, relief=GROOVE, text='Customer Details', font=('times new roman', 15, 'bold'), fg='gold', bg= '#6A24FF')
customer_details_frame.place(x=0, y=80, relwidth=1)

# Create labels and entry fields for customer details
cname_lbl = Label(customer_details_frame, text='Customer Name', font=('times new roman', 18, 'bold'), bg='#6A24FF', fg='white')
cname_lbl.grid(row=0, column=0, padx=20, pady=5)
cname_txt = Entry(customer_details_frame, width=15, textvariable=c_name, font='arial 15 bold', relief=SUNKEN, bd=7)
cname_txt.grid(row=0, column=1, padx=10, pady=5)

cphone_lbl = Label(customer_details_frame, text='Phone No.', font=('times new roman', 18, 'bold'), bg='#6A24FF', fg='white')
cphone_lbl.grid(row=0, column=2, padx=20, pady=5)
cphone_txt = Entry(customer_details_frame, width=15, textvariable=c_phone, font='arial 15 bold', relief=SUNKEN, bd=7)
cphone_txt.grid(row=0, column=3, padx=10, pady=5)

# Create the product details frame
product_details_frame = LabelFrame(main_frame, text='Products Brought', font=('times new roman', 18, 'bold'), fg='gold', bg='#6A24FF')
product_details_frame.place(x=20, y=180, width=630, height=500)

# Create labels and entry fields for product details
itm_lbl = Label(product_details_frame, text='Product Name', font=('times new roman', 18, 'bold'), bg='#6A24FF', fg='lightgreen')
itm_lbl.grid(row=0, column=0, padx=30, pady=20)
itm_txt = Entry(product_details_frame, width=20, textvariable=item, font='arial 15 bold', relief=SUNKEN, bd=7)
itm_txt.grid(row=0, column=1, padx=10, pady=20)

rate_lbl = Label(product_details_frame, text='Product Rate', font=('times new roman', 18, 'bold'), bg='#6A24FF', fg='lightgreen')
rate_lbl.grid(row=1, column=0, padx=30, pady=20)
rate_txt = Entry(product_details_frame, width=20, textvariable=rate, font='arial 15 bold', relief=SUNKEN, bd=7)
rate_txt.grid(row=1, column=1, padx=10, pady=20)

n_lbl = Label(product_details_frame, text='Product Quantity', font=('times new roman', 18, 'bold'), bg='#6A24FF', fg='lightgreen')
n_lbl.grid(row=2, column=0, padx=30, pady=20)
n_txt = Entry(product_details_frame, width=20, textvariable=quantity, font='arial 15 bold', relief=SUNKEN, bd=7)
n_txt.grid(row=2, column=1, padx=10, pady=20)

# Create the bill area frame
bill_area_frame = Frame(main_frame, relief=GROOVE, bd=10)
bill_area_frame.place(x=700, y=180, width=500, height=500)

# Create the bill area title
bill_title_label = Label(bill_area_frame, text='Bill Area', font='arial 15 bold', bd=7, relief=GROOVE)
bill_title_label.pack(fill=X)

# Create the scroll bar for the bill text area
scroll_y = Scrollbar(bill_area_frame, orient=VERTICAL)
scroll_y.pack(side=RIGHT, fill=Y)

# Create the text area to display the bill
bill_text_area = Text(bill_area_frame, yscrollcommand=scroll_y)
scroll_y.config(command=bill_text_area.yview)
bill_text_area.pack(fill=BOTH, expand=True)

# Display the welcome message and bill number
welcome_message()

# Create buttons for various actions
btn_add_item = Button(product_details_frame, text='Add Item', font='arial 15 bold', command=add_item, padx=5, pady=10, bg='lime', width=15)
btn_add_item.grid(row=3, column=0, padx=10, pady=30)

btn_generate_bill = Button(product_details_frame, text='Generate Bill', font='arial 15 bold', command=generate_bill, padx=5, pady=10, bg='lime', width=15)
btn_generate_bill.grid(row=3, column=1, padx=10, pady=30)

btn_clear_fields = Button(product_details_frame, text='Clear', font='arial 15 bold', command=clear_fields, padx=5, pady=10, bg='lime', width=15)
btn_clear_fields.grid(row=4, column=0, padx=10, pady=30)



btn_pay = Button(product_details_frame, text='Pay', font='arial 15 bold', command=pay_method_popup, padx=5, pady=10, bg='lime', width=15)
btn_pay.grid(row=4, column=1, padx=10, pady=30)

# Start the Tkinter event loop
root.mainloop()
