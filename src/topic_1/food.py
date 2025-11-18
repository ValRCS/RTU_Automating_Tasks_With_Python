# let us make a program that asks user for their favorite food and responds
food = input("What is your favorite food? ")  # get user input
print("Wow, I love " + food + " too! 🍽️")  # respond with a cheerful message
# now let us ask how much 1kg of that food costs
# also we will convert this input to a float number
# input always returns a string so for numerical input we need to convert!
# at the moment we trust the user to give valid input
# later on we will see how to handle invalid input too
cost_per_kg = float(input("How much does 1kg of " + food + " cost? "))  # get cost as float
# how many kg they want to buy?
quantity = int(input("How many kg of " + food + " do you want to buy? "))  # get quantity as int
# calculate total cost
total_cost = cost_per_kg * quantity
# print the total cost with 2 decimal places
print("The total cost for", quantity, "kg of", food, "is", total_cost)

# there is a nice way of formatting string out put using f-strings
print(f"The total cost for {quantity} kg of {food} is ${total_cost:} 🎉")
# we can show only 2 decimal places too
print(f"The total cost for {quantity} kg of {food} is ${total_cost:.2f} 🎉")
# we can show 4 decimal places too or anything else
print(f"The total cost for {quantity} kg of {food} is ${total_cost:.4f} 🎉")