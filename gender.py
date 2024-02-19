gender = str(input("Whats Your Gender: ")).lower()
print(gender)
if gender == "Male":
    print("You are a He/His")
elif gender == "Female":
    print("You are a She/Her")
else:
    print("Invalid request")
