weight = float(input("Weight: "))
unit = input("(K)g or (L)bs ")

if unit == "k":
    convert = weight / 0.454
    print("Weight in Lbs: " + str(convert))
elif unit == "L":
    convert = weight * 0.454
    print("Weight in Kgs: " + str(convert))
else:
    print("Invalid choice")

