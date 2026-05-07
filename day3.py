# if condition:
#     print("do this")
# else: 
#     print("do that instead")

# print("Welcome!")
# how_many = input("How many idiots do you have?\n")

# if how_many != 5:
#     print("you're normal")
# else:
#     print("wtf bro?")

# print(10 % 3)

# even_or_odd = float(input("Pick a number.\n"))
# try:
#     int(even_or_odd)
# except ValueError:
#     try: 
#         float(even_or_odd)
#     except ValueError:
#         print("It must be a number...")

# print("kthnx")

# even_or_odd = input("Pick a number.\n")

# try:
#     val = float(even_or_odd)
#     if val.is_integer():
#         number =
# except ValueError:
#     print("That is not a number, silly.")

# user_input = input("Pick a number and I'll tell you if it's even or odd.\n")
# even_or_odd = int(user_input) % 2
# if even_or_odd == 0:
#     print("It's even.\n")
# else: 
#     print("Odd.")

bill = 0
print("Welcome to Python Pizza Deliveries!")

# todo: work out how much they need to pay based on their size, pepperoni, and extra cheese choices.
while True:
    size = input("What size pizza do you want? Please choose S, M, or L: \n").upper()
    if size == "S" or size == "M" or size == "L":
        break
    else:
        print("Please choose S, M, or L. \n")

while True:
    pepperoni = input("Do you want pepperoni? Y or N: \n").upper()
    if pepperoni == "Y" or pepperoni == "N":
        break
    else:
        print("Please choose Y or N. \n")


while True:
    extra_cheese = input("Would you like extra cheese? Y or N: \n").upper()
    if extra_cheese == "Y" or extra_cheese == "N":
        break
    else:
        print("Please choose Y or N. \n")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pepperoni == "Y" and size == "S":
    bill += 2
elif pepperoni == "Y" and (size == "M" or size == "L"):
    bill += 3
else: 
    bill += 0

if extra_cheese == "Y":
    bill += 1
else:
    bill += 0

print(f"Your final bill is: ${bill:.2f}.")