a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))
if a + b > c and a + c > b and b + c > a:
    print("The triangle is valid")
else:
    print("The triangle is not valid")
