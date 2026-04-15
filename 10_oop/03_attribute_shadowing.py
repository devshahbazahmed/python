class Chai:
    temperature = "Hot"
    strength = "Strong"

cutting_chai = Chai()

print(cutting_chai.temperature)

cutting_chai.temperature = "Mild"
cutting_chai.cup = "Medium"
print(f"After changing {cutting_chai.temperature}")
print(f"Cup size is {cutting_chai.cup}")
print(f"Direct look into the class {Chai.temperature}")

del cutting_chai.temperature
del cutting_chai.cup
print(cutting_chai.temperature)
print(cutting_chai.cup)
