print("Welcome to Sportybet")
print("Please Sign up\nNote that the site is only eligible for people above 18+")

name = input("Enter your Name: ").upper()
gender = input("Enter your Gender: ").upper()

valid_age = False
while not valid_age:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        if 18 <= age <= 60:
            print("You are eligible. Kindly proceed to the website.")
            valid_age = True
        else:
            print("Sorry, you are not eligible due to age restrictions (must be between 18 and 60).")
    else:
        print("Please enter a valid age (must be a number).")
