# User input 
year = int(input("Enter the year: "))

# Program operation & Computer output
if (year % 400 == 0):
    print(str(year) + " is a leap year.")
elif (year % 4 == 0) and (year % 100 != 0):
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is not a leap year.")