temperature = float(input("Temperature: "))

if temperature > 30: #if temp above 30
    print("It's a hot day!")
    print("Drink plenty of water!")
elif temperature > 20: #if temp between 20-30
    print("It's a nice day!")
elif temperature > 10: #if temp between 20-10
    print("It's a bit cold!")
else:
    print("It's freezing, wrap up warm!")

print("Done!")
