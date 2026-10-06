a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))
if a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or a == c:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
