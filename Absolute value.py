#Write a Python program to find the absolute value of an input number

number = float(input("Enter a number: "))

if number < 0:
    number = number*(-1)

print ("The absolute value of this number is " , number)