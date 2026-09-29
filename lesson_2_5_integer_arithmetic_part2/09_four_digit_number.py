n = int(input("Enter a four-digit number: "))
d = n % 10
c = (n // 10) % 10
b = (n // 100) % 10
a = n // 1000
print("The digit in the thousands place is equal to", a)
print("The digit in the hundreds place is equal to", b)
print("The digit in the tens place is equal to", c)
print("The digit in the ones place is equal to", d)
