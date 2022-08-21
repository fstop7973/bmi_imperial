weight_lbs = float(input("Please enter weight in pounds:"))
height_inches = float(input("Please enter height in inches:"))

weight_kg = float(weight_lbs*.453592)
height_meters = float(height_inches*.0254)
bmi = float(weight_kg/height_meters**2)
print("BMI is:", bmi)