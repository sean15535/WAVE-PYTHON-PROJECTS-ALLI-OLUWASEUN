def purchase():
    purchase_cost = int(input("How much was your meal? $ "))
    return tip_calculator()

def tip_calculator():
    tip = 0.03 * purchase()
    print(f"Our restaurant charges 3% for total purchase, which is #{tip}")
    total_cost = tip + purchase()

    return tip

def greetings():
    print("good day, hope you enjoyed your meal")
    print("a. Yes")
    print("b. No")
    response = str(input(" "))
    if response == "a" or "Yes":
        print("❤💖")
        return purchase()
    else:
        print("😢")
        return purchase()
def payment():
    print("Are you making a single or joint payment?")
    print("a. Single payment")
    print("b. Joint payment")
    reply = str(input()).lower()
    if reply == "a":
        print(f"Your total costs is #{total_cost}")
    elif reply == "b":
        print("How many of you are paying?")
        no_of_people = int(input())
        each_pays = total_cost / no_of_people
        print(f"You are to pay #{each_pays}")
    else:
        print("Invalid request")
    print("Thanks for eating here 💖💖")

greetings()
  





