OUTSIDE_FEE = 30
try:
    weight = float(input("Weight (kg): "))
except ValueError:
    print("Please enter a valid weight")
    exit()
if weight <= 0:
    print("Please enter a valid weight")
    exit()
if weight > 20:
    print("Too heavy (max 20 kg)")
    exit()
destination = input("Destination (bangkok/other): ")
if destination != "bangkok" and destination != "other":
    print("Unknown destination")
    exit()
express = input("Express? (yes/no): ")
if weight <= 1:
    price = 40
elif weight <= 5:
    price = 80
else:
    price = 150
if destination == "other":
    price += OUTSIDE_FEE
if express == "yes":
    price *= 2
print("Shipping cost:", price, "baht")
