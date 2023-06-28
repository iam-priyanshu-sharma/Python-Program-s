print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill = 99
    if add_pepperoni == "Y":
        bill += 50

    if extra_cheese == "Y":
        bill += 25

    print(f"Your final bill is: ₹{bill}.")

elif size == "M":
    bill = 150
    if add_pepperoni == "Y":
        bill += 75

    if extra_cheese == "Y":
        bill += 25

    print(f"Your final bill is: ₹{bill}.")

else:
    bill = 200
    if add_pepperoni == "Y":
        bill += 75

    if extra_cheese == "Y":
        bill += 25

    print(f"Your final bill is: ₹{bill}.")
