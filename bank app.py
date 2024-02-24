# This program simulates a basic banking system for Wema Bank Plc.
# It generates a random 10-digit account number for new accounts and offers options for account opening, transfers,
# airtime purchases, internet banking, balance inquiries, and bill payments.

import random

# Initialize an empty string to store the account number
user_account = ""

# Generate a random account number
for _ in range(10):  # Generate 10 digits for the account number
    digit = random.randint(0, 9)  # Generate a random digit between 0 and 9
    user_account += str(digit)  # Append the digit to the account number
print("Welcome to Wema Bank Plc. \nHow maywe help you today?")
print("1. Open account\n2. Transfer\n3. Airtime\n4. Internet\n5. Balance\n6. Bills & Utitilies")
response = str(input( )).lower()
if response == "1" or response == "open account": 
    firstname = str(input("Your firstname\n>> ")).upper()
    surname = str(input("Your lastname\n>> ")).upper()
    other_name = str(input("Your other name\n>> ")).upper()
    gender = str(input("Your Gender\n>> ")).upper()
    email = str(input("Your email\n>> ")).upper()
    number = int(input("Your Phone number\n>> "))
    address = (input("your address\n>> ")).upper()
    dob = input("Your date of birth (MM/DD/YYYY)\n>> ")
    print("\nThank you for filling out the form.")
    print("Your account has been created successfully.")
    print("Here is your account information:")
    print(f"Name: {firstname} {other_name} {surname}")
    print(f"Date of Birth: {dob}")
    print("Address:", address)
    print("Account Number:", user_account)
    print("Thank you for choosing our bank")
elif response == "2" or response == "transfer":
    print("Choose the bank you are Transfering to: \n1. GT Bank \n2. Eco Bank \n3. Access Bank \n4. Wema Bank \n5. United Bank For Africa \n6. Other Options ")
    reply = input(">> ").lower()
    if reply == "1" or reply == "gtb" or reply == "gt bank" or reply == "gtbank":
        # Transfer to GT Bank
        recipient_account_number = int(input("Enter the recipient's GT Bank account number: "))
        amount = int(input("Enter the amount you want to transfer: "))

        # Placeholder for transfer process
        print(f"Transferring ₦{amount} to GT Bank account number {recipient_account_number}...")
        print("Transfer successful! \nThnaks for banking with us😉")
    elif reply == "2" or reply == "eco bank" or reply == "eco":
        # Transfer to Eco Bank
        recipient_account_number = int(input("Enter the recipient's Eco Bank account number: "))
        amount = int(input("Enter the amount you want to transfer: "))

        # Placeholder for transfer process
        print(f"Transferring ₦{amount} to Eco Bank account number {recipient_account_number}...")
        print("Transfer successful! \nThanks for banking with us😉")
    elif reply == "3" or reply == "access bank" or reply == "access" :
        # Transfer to Access Bank
        recipient_account_number = int(input("Enter the recipient's Access Bank account number: "))
        amount = int(input("Enter the amount you want to transfer: "))

        # Placeholder for transfer process
        print(f"Transferring ₦{amount} to Access Bank account number {recipient_account_number}...")
        print("Transfer successful! \nThanks for banking with us😉")
    elif reply == "4" or reply == "wema" or reply == "wema bank":
        # Transfer to Wema Bank
        recipient_account_number = int(input("Enter the recipient's Wema Bank account number: "))
        amount = int(input("Enter the amount you want to transfer: "))

        # Placeholder for transfer process
        print(f"Transferring ₦{amount} to Wema Bank account number {recipient_account_number}...")
        print("Transfer successful! \nThanks for banking with us😉")
    elif reply == "5" or reply == "uba" or reply == "united bank for africa":
        # Transfer to United Bank For Africa
        recipient_account_number = int(input("Enter the recipient's United Bank For Africa account number: "))
        amount = int(input("Enter the amount you want to transfer: "))

        # Placeholder for transfer process
        print(f"Transferring ₦{amount} to United Bank For Africa account number {recipient_account_number}...")
        print("Transfer successful! \nThanks for banking with us😉")
    elif reply == "6" or reply == "other transfer options":
        # Other transfer options (placeholder)
        print("Choose Other transfer options:\n7. First Bank \n8. Globus Bank \n9.Opay \n10.Palmpay")
        choice = input(">> ").lower()
        if choice == "7" or reply == "first bank":
            # Transfer to First Bank
                recipient_account_number = int(input("Enter the recipient's First Bank account number: "))
                amount = int(input("Enter the amount you want to transfer: "))

            # Placeholder for transfer process
                print(f"Transferring ₦{amount} to First Bank  account number {recipient_account_number}...")
                print("Transfer successful! \nThanks for banking with us😉")
        elif choice == "8" or reply == "globus bank":
            # Transfer to Globus Bank
                recipient_account_number = int(input("Enter the recipient's Globus Bank account number: "))
                amount = int(input("Enter the amount you want to transfer: "))

            # Placeholder for transfer process
                print(f"Transferring ₦{amount} to Globus Bank  account number {recipient_account_number}...")
                print("Transfer successful! \nThanks for banking with us😉")
        elif choice == "9" or reply == "opay":
            # Transfer to OPAY
                recipient_account_number = int(input("Enter the recipient's OPAY account number: "))
                amount = int(input("Enter the amount you want to transfer: "))

            # Placeholder for transfer process
                print(f"Transferring ₦{amount} to OPAY  account number {recipient_account_number}...")
                print("Transfer successful! \nThanks for banking with us😉")
        elif choice == "10" or reply == "palmpay":
            # Transfer to Palmpay
                recipient_account_number = int(input("Enter the recipient's Palmpay account number: "))
                amount = int(input("Enter the amount you want to transfer: "))

            # Placeholder for transfer process
                print(f"Transferring ₦{amount} to Palmpay account number {recipient_account_number}...")
                print("Transfer successful! \nThanks for banking with us😉")
        else:
                print("invalid bank choice")
    else:
        print("Invalid bank choice")

elif response == "3" or response == "airtime":
    print("Choose airtime type: \n1. MTN \n2. Airtel \n3. Glo \n4. 9mobile ").lower()
    reply = input(">>> ")
    if reply == "1" or reply == "mtn":
         print("")
else:
    print("Invalid command")


