num = int(input("Enter a number: "))
a = num % 10
b = (num // 10) % 10
c = (num // 100) % 10
d = (num // 1000) % 10
if a + d == c - b:
    print("YES")
else:
    print("NO")
