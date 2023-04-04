weight = float(input("What is your weight? "))
unit = input("Enter P for pounds or K for kilograms: ")

if unit.lower() == 'p':
    weight *= 10
    print(f"Your weight is: {weight} kilos")
elif unit.lower() == 'k':
    weight *= 0.45
    print(f"Your weight is: {weight} pounds")
else:
    print('Invalid Input.')