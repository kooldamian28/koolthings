# User input 
number = float(input("Enter your number: "))

# Program operation
if number > 0:
    print("The number you have entered is a positive number")
elif number < 0:
    print("The number you have entered is a negative number")
elif number == 0:
    print("Great, you're perfect!")
else:
    print("I'm not sure I understand")
