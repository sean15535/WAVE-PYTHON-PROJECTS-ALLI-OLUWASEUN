print("Welcome to Sportybet")
print("Please Sign up \nNote that the site is only eligible for people above 18+")

response = str(input("Enter your Name: ")).upper()
print("Enter your Gender")
response = str(input("Gender: ")).upper()

valid = False
while not valid:
    age = input("Enter your age: ")
    if age.isdigit() and int(age) >= 18:
        print("You are eligible.Kindly proceed to the website")
        valid = True
    else:
        print("Please enter a valid age (must be at least 18 years old).")
    
