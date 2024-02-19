import time  # Import the time module

print("Hi, Welcome to Taxify")
print("Whats your Name?")
name = str(input("Enter your name: ")).upper()
print(f" Hi {name}. Where are you heading today?")
print("a. Work")
print("b. Home")
print("c. Meeting")
print("d. Event")
movement = str(input(" "))

print("Which city is it located?")
print("a. Lagos State")
print("b. Ogun State")
city = str(input(" ")).lower()

if city == "a" or city == "lagos state" or city == "lagos":
    print("Which Part in Lagos?")
    print("a. Ikeja")
    print("b. Egbeda")
    respond = str(input(" ")).lower()
    if respond == "a" or respond == "ikeja":
        print(" Our fee for trip to Ikeja is $9000")
        print("How much are you paying?")
        amount = int(input("$ "))
        if amount >= 9000:
            change = amount - 9000
            print(f"Your change is ${change}.")
            print("How would you like to pay?")
            print("1. Cash")
            print("2. Card")
            payment_method = str(input("Choose payment method (1 or 2): ")).lower()
            if payment_method == "1" or payment_method == "cash":
                print(f"Please have $9000 ready for your trip to Ikeja and you get ${change} from the Driver.")
                print("Your trip to Ikeja has started. Enjoy your ride!")
                print(f"{name}, You have arrived to your destination. Have a nice day!😊")
                time.sleep(10)  

            elif payment_method == "2" or payment_method == "card":
                print("Please proceed to pay $9000 with your card and you get ${change} from the Driver..")
                print("Your trip to Ikeja has started. Enjoy your ride!")
                print(f"{name}, You have arrived to your destination. Have a nice day!😊")
                time.sleep(10)
            else:
                print("Wrong payment method, Try again ") 
        else:
            print("Insufficient payment. Your trip to Ikeja is canceled. ")


    elif respond == "b" or respond == "egbeda":
        print(" Our fee for trip to Egbeda is $4000")
        print("How much are you paying?")
        amount = int(input("$ "))
        if amount >= 4000:
            change = amount - 4000
            print(f"Your change is ${change}.")
            print("How would you like to pay?")
            print("1. Cash")
            print("2. Card")
            payment_method = str(input("Choose payment method (1 or 2): ")).lower()
            if payment_method == "1" or payment_method == "cash":
                print(f"Please have $4000 ready for your trip to Egbeda and you get ${change} from the Driver.")
                print("Your trip to Egbeda has started. Enjoy your ride!")
                print(f"{name}, You have arrived to your destination. Have a nice day!😊")
                time.sleep(10)  

            elif payment_method == "2" or payment_method == "card":
                print("Please proceed to pay 49000 with your card and you get ${change} from the Driver..")
                print("Your trip to Egbeda has started. Enjoy your ride!")
                print(f"{name}, You have arrived to your destination. Have a nice day!😊")
                time.sleep(10)
            else:
                print("Wrong payment method, Try again ") 
        else:
            print("Insufficient payment. Your trip to Egbeda is cancelled. ")
    else:
        print("City not found, Try Again")
elif city == "b" or city == "ogun state" or city == "ogun" :
    print("Which Part in Ogun State?")
    print("a. Abeokuta")
    print("b. Ifo")
    respond = str(input(" ")).lower()
    if respond == "a" or respond == "abeokuta":
        print(" Our fee for trip to Abeokuta is $8000")
        print("How much are you paying?")
        amount = int(input("$ "))
        if amount >= 8000:
            change = amount - 8000
            print(f"Your change is ${change}.")
            print("How would you like to pay?")
            print("1. Cash")
            print("2. Card")
            payment_method = str(input("Choose payment method (1 or 2): ")).lower()
            if payment_method == "1" or payment_method == "cash":
                print(f"Please have $8000 ready for your trip to Abeokuta and you get ${change} from the Driver.")
                print("Your trip to Abeokuta has started. Enjoy your ride!")
                print(f"{name}, You have arrived to your destination. Have a nice day!😊")
                 

            elif payment_method == "2" or payment_method == "card":
                print("Please proceed to pay $8000 with your card and you get ${change} from the Driver..")
                print("Your trip to Abeokuta has started. Enjoy your ride!")
                print(f"{name}, You have arrived to your destination. Have a nice day!😊")
                 
            else:
                print("Wrong payment method, Try again ")
        else:
            print("Insufficient payment. Your trip to Abeokuta is cancelled. ")
    elif respond == "b" or respond == "ifo":
        print(" Our fee for trip to Ifo is $5000")
        print("How much are you paying?")
        amount = int(input("$ "))
        if amount >= 5000:
            change = amount - 5000
            print(f"Your change is ${change}.")
            print("How would you like to pay?")
            print("1. Cash")
            print("2. Card")
            payment_method = str(input("Choose payment method (1 or 2): ")).lower()
            if payment_method == "1" or payment_method == "cash":
                print(f"Please have $5000 ready for your trip to Ifo and you get ${change} from the Driver.")
                print("Your trip to Ifo has started. Enjoy your ride!")
                print(f"{name}, You have arrived to your destination. Have a nice day!😊")
                 

            elif payment_method == "2" or payment_method == "card":
                print("Please proceed to pay $5000 with your card and you get ${change} from the Driver..")
                print("Your trip to Ifo has started. Enjoy your ride!")
                print(f"{name}, You have arrived to your destination. Have a nice day!😊")
                
            else:
                print("Wrong payment method, Try again ")
        else:
            print("Insufficient payment. Your trip to Ifo is cancelled. ")
    else:
        print("City not found, Try Again")
else:
    print("State not found. Please try again")
