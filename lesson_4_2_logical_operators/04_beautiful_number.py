num = int(input("Enter a number: "))
if 1000 <= num <= 9999 and (num % 7 == 0 or num % 17 == 0):
    print(f"{num} is a beautiful number")
else:
    print(f"{num} is not a beautiful number")
