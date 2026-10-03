a = int(input("Enter first column: "))
b = int(input("Enter first row: "))
c = int(input("Enter second column: "))
d = int(input("Enter second row: "))
if a == c or b == d:
    print("Rook can move from first square to second square.")
else:
    print("Rook cannot move from first square to second square.")
