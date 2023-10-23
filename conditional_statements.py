
# Condtional Statements
print("Condtional Statements")

temperature = 67

if temperature > 37:
    print("It is too Hot!")
else:
    print("It is too Cold!")

# A program that checks three numbers and returns the largest
num1 = 67
num2 = 24
num3 = 6

if num1 > num2 and num1 > num3:
    print(num1,"is the Largest")
elif num2 > num1 and num2 > num3:
    print(num2,"is the Largest number")
else:
    print(num3,"is the largest number")


# Program that checks whether a number is Even or Odd
number= 37
if number % 2 == 0:
    print(number, "is an Even Number")
else:
    print(number, "is an Odd Number")
