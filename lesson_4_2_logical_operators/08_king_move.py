a = int(input("Enter first column: "))
b = int(input("Enter first row: "))
c = int(input("Enter second column: "))
d = int(input("Enter second row: "))
if -1 <= c - a <= 1 and -1 <= d - b <= 1:
    print("king can move from first square to second square.")
else:
    print("king cannot move from first square to second square.")
