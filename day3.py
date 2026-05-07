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

user_input = input("Pick a number and I'll tell you if it's even or odd.\n")
even_or_odd = int(user_input) % 2
if even_or_odd == 0:
    print("It's even.\n")
else: 
    print("Odd.")