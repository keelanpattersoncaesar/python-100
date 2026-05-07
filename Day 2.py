# print("hello world hehe :)")
# print("132_456_789")
# print(132_456_789)

# print(type(123))
# print(type("string"))
# print(type(True))
# print(type(123.456))

# print("Number of letters in your name: " + str((len(input("Enter your name, please.\n")))))




# height = 1.65 
# weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
# weight = input("What is your weight? \n")
# height = input("What is your height? \n")
# weight = float(weight)
# height = float(height)
# bmi = weight / height**2

# print(f"Your bmi is {round(bmi,2)}")

print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? \n")
print(f"Great, so the total was ${total_bill}.")
total_bill = float(total_bill)
tip_amount = input("And what percentage would you like to tip? \n")
print(f"Gotcha, so you want to tip {tip_amount}%.")
tip_amount = float(tip_amount)
party_size = input("Lastly, how many people are in your party? \n")
print(f"Okay, {party_size} people.")
party_size = int(party_size)
tip_conversion = int(tip_amount) / 100
final_amount = (total_bill + (total_bill * tip_conversion)) / party_size
print(f"Each person should pay ${final_amount:.2f}")