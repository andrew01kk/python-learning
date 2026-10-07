color1 = input("Enter the first color (red, blue, yellow): ")
color2 = input("Enter the second color (red, blue, yellow): ")
if color1 == "red" and color2 == "blue":
    print("The resulting color is purple.")
elif color1 == "blue" and color2 == "red":
    print("The resulting color is purple.")
elif color1 == "red" and color2 == "yellow":
    print("The resulting color is orange.")
elif color1 == "yellow" and color2 == "red":
    print("The resulting color is orange.")
elif color1 == "blue" and color2 == "yellow":
    print("The resulting color is green.")
elif color1 == "yellow" and color2 == "blue":
    print("The resulting color is green.")
elif color1 == color2 and color1 in ["red", "blue", "yellow"]:
    print(f"The resulting color is {color1}.")
