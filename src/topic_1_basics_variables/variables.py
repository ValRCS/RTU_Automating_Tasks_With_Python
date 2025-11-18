# variable let us persist data in memory for later use
# we use the assignment operator = to assign a value to a variable
# in Python we do not need to declare variable types explicitly
# Python is a dynamically typed language
# Python decides automatically the type of variable based on the value assigned
# let us create some variables
a = 10  # assigning integer value 10 to variable a
b = 25  # assigning integer value 25 to variable b
result = a + b  # adding values of a and b and storing in result
print("The sum of", a, "and", b, "is", result)
# now that program ends the variables a, b, and result are lost
# if we run the program again the variables will be re-created
# we can still use the variables as long as the program is running
print("Let us do more calculations...")
difference = b - a
print("The difference between", b, "and", a, "is", difference)

# so valid variable names in Python are starting with a letter or underscore _
# followed by letters, digits or underscores
MY_PI = 3.14159  # constant variable by convention uppercase
radius = 5
area = MY_PI * radius * radius
print("The area of a circle with radius", radius, "is", area)