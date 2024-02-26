# This program simulates a basic banking system for Wema Bank Plc.
# It generates a random 10-digit account number for new accounts and offers options for account opening, transfers,
# airtime purchases, Data, balance inquiries, and bill payments.

import random

# Initialize an empty string to store the account number
user_account = ""

# Generate a random account number
for _ in range(10):  # Generate 10 digits for the account number
    digit = random.randint(0, 9)  # Generate a random digit between 0 and 9
    user_account += str(digit)  # Append the digit to the account number
print("Welcome to Wema Bank Plc. \nHow maywe help you today?")
print("1. Open account\n2. Transfer\n3. Airtime\n4. Data\n5. Account Balance\n6. Bills & Utitilies")
response = str(input(">>> " )).lower()
if response == "1" or response == "open account": 
    firstname = str(input("Your firstname\n>> ")).capitalize()
    surname = str(input("Your lastname\n>> ")).capitalize()
    other_name = str(input("Your other name\n>> ")).capitalize()
    gender = str(input("Your Gender\n>> ")).capitalize()
    email = str(input("Your email\n>> ")).capitalize()
    number = int(input("Your Phone number\n>> "))
    address = (input("your address\n>> ")).capitalize()
    dob = input("Your date of birth (MM/DD/YYYY)\n>> ")
    print("\nThank you for filling out the form.")
    print("Your account has been created successfully.")
    print("Here is your account information:")
    print(f"Name: {firstname} {other_name} {surname}")
    print(f"Date of Birth: {dob}")
    print("Address:", address)
    print("Account Number:", user_account)
    print("Thank you for choosing our bank")
#Transfer section
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
#Airtime section
elif response == "3" or response == "airtime":
    print("Choose airtime type: \n1. MTN \n2. Airtel \n3. Glo \n4. 9mobile ")
    reply = input(">>> ").lower()
    if reply == "1" or reply == "mtn":
        # Process MTN airtime purchase
        phone_number = int(input("Enter your MTN phone number: "))
        amount = int(input("Enter the amount of airtime you want to buy: "))
        
        # Placeholder for airtime purchase process
        print(f"Recharging ₦{amount} airtime to MTN number {phone_number}...")
        print("Airtime purchase successful! \nThank you for banking with us! 😊")
    
    elif reply == "2" or reply == "airtel":
        # Process Airtel airtime purchase
        phone_number = int(input("Enter your Airtel phone number: "))
        amount = int(input("Enter the amount of airtime you want to buy: "))
        
        # Placeholder for airtime purchase process
        print(f"Recharging ₦{amount} airtime to Airtel number {phone_number}...")
        print("Airtime purchase successful! \nThank you for banking with us! 😊")
    
    elif reply == "3" or reply == "glo":
        # Process Glo airtime purchase
        phone_number = int(input("Enter your Glo phone number: "))
        amount = int(input("Enter the amount of airtime you want to buy: "))
        
        # Placeholder for airtime purchase process
        print(f"Recharging ₦{amount} airtime to Glo number {phone_number}...")
        print("Airtime purchase successful! \nThank you for banking with us! 😊")
    
    elif reply == "4" or reply == "9mobile":
        # Process 9mobile airtime purchase
        phone_number = int(input("Enter your 9mobile phone number: "))
        amount = int(input("Enter the amount of airtime you want to buy: "))
        
        # Placeholder for airtime purchase process
        print(f"Recharging ₦{amount} airtime to 9mobile number {phone_number}...")
        print("Airtime purchase successful! \nThank you for banking with us! 😊")
    
    else:
        print("Invalid airtime option")
# Data section
elif response == "4" or response == "data":
    print("Choose data plan: \n1. Daily Plan \n2. Weekly Plan \n3. Monthly Plan")
    reply = input(">>> ").lower()
    if reply == "1" or reply == "daily":
        # Process daily data purchase
        phone_number = int(input("Enter your phone number: "))
        amount = int(input("Enter the amount of data you want to buy (in GB): "))
        
        # Placeholder for data purchase process
        print(f"Purchasing Daily data of {amount}GB  for {phone_number}...")
        print("Data purchase successful! \nThank you for banking with us! 😊")
    
    elif reply == "2" or reply == "weekly":
        # Process weekly data purchase
        phone_number = int(input("Enter your phone number: "))
        amount = int(input("Enter the amount of data you want to buy (in GB): "))
        
        # Placeholder for data purchase process
        print(f"Purchasing Weekly Data of {amount}GB  for {phone_number}...")
        print("Data purchase successful! \nThank you for banking with us! 😊")
    
    elif reply == "3" or reply == "monthly":
        # Process monthly data purchase
        phone_number = int(input("Enter your phone number: "))
        amount = int(input("Enter the amount of data you want to buy (in MB): "))
        
        # Placeholder for data purchase process
        print(f"Purchasing Monthly Data of {amount}GB  for {phone_number}...")
        print("Data purchase successful! \nThank you for banking with us! 😊")
    
    else:
        print("Invalid data option")

elif response == "5" or response == "account balance":
     account_balance = 50000  # variable for account balance
     print("A fee of 4.00 naira will be deducted from your account for this service. \nPress 1 to proceed \nPress 2 to Cancel")
     proceed_option = int(input ( ))
     if proceed_option == 1:
        # Deduct a service fee of 4 naira
        account_balance -= 4
        
        print(f"Your Account Balance for Account Number - {user_account} is ₦{account_balance}")
        print("Thanks for banking with us! 😊")
     elif proceed_option == 2:
        print("Service canceled.")
     else:
        print("Invalid option")

elif response == "6" or response == "bills and utilities":
     print("Choose the utility you want to pay for:")
     print("1. Electricity Bill\n2. Water Bill\n3. Remitta Bill\n4. Gas Bill")
     utility_choice = input(">>> ").lower()

     if utility_choice == "1" or utility_choice == "electricity bill":
        # Process electricity bill payment
        account_number = input("Enter your electricity meter number: ")
        amount = float(input("Enter the amount you want to pay: "))

        # Placeholder for electricity bill payment process
        print(f"Processing electricity bill payment of ₦{amount} for meter number {account_number}...")
        print("Electricity bill payment successful! Thank you for banking with us! 😊")

     elif utility_choice == "2" or utility_choice == "water bill":
        # Process water bill payment
        account_number = int(input("Enter your water bill number: "))
        amount = int(input("Enter the amount you want to pay: "))

        # Placeholder for water bill payment process
        print(f"Processing water bill payment of ₦{amount} for  number {account_number}...")
        print("Water bill payment successful! Thank you for banking with us! 😊")

     elif utility_choice == "3" or utility_choice == "remitta payment":
        # Process internet bill payment
        account_number = input("Enter your Remitta  number: ")
        amount = int(input("Enter the amount you want to pay: "))

        # Placeholder for internet bill payment process
        print(f"Processing Remitta payment of ₦{amount} for Remitta number {account_number}...")
        print("Remitta payment successful! Thank you for banking with us! 😊")

     elif utility_choice == "4" or utility_choice == "gas bill":
        # Process gas bill payment
        account_number = int(input("Enter your gas account number: "))
        amount = int(input("Enter the amount you want to pay: "))

        # Placeholder for gas bill payment process
        print(f"Processing gas bill payment of ₦{amount} for gas number {account_number}...")
        print("Gas bill payment successful! Thank you for banking with us! 😊")

     else:
        print("Invalid utility choice")
else:
    print("Invalid command")


