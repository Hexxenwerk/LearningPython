weight = float(input("Enter your body weight: "))
unit = input("Weight in (K)g or (L)bs: ")

if unit.lower() == "k":
    print("Weight in kg: {:.2f}".format(weight * 2.20462))
elif unit.lower() == "l":
    print("Weight in lbs: {:.2f}".format(weight / 2.20462))
else:
    print(f"Invalid weight unit: '{unit}'. Enter 'k' or 'l' as unit.")
