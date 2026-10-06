a = int(input("Enter a month number (1-12): "))
if a == 2:
    print("28 days")
elif a in [4, 6, 9, 11]:
    print("30 days")
else:
    print("31 days")
