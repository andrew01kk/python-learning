a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a < b < c or c < b < a:
    median = b
elif b < a < c or c < a < b:
    median = a
else:
    median = c
print("The median number is:", median)
