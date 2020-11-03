# User input
percentage = float(input("Enter your marks: "))

# Program operation
if (percentage >= 90):
    print("Your grade is A1 !")
elif (percentage >= 80):
    print("Your grade is A !")
elif (percentage >= 70):
    print("Your grade is B1 !")
elif (percentage >= 60):
    print("Your grade is B !")
elif (percentage >= 50):
    print("Your grade is C, try better next time!")
elif (percentage >= 33):
    print("Your grade is D, try better next time!")
else:
    print("Your grade is E, try better next time!")