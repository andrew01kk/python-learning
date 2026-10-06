n = int(input("Enter the speed of the car: "))
k = int(input("Enter the speed of the bike: "))
if n > k:
    print("The car is faster than the bike.")
elif n < k:
    print("The bike is faster than the car.")
else:
    print("The car and the bike have the same speed.")
