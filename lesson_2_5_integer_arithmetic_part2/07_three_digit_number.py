n = int(input("Enter a three-digit number: "))
a = n % 10
b = (n // 10) % 10
c = n // 100
print("The sum of the digits is:", a + b + c)
print("The product of the digits is:", a * b * c)
