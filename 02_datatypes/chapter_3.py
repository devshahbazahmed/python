# Integer

black_tea_grams = 14
ginger_tea_grams = 3

total_grams = black_tea_grams + ginger_tea_grams

print(f"Total grams of base is {total_grams}")

remaining_tea = black_tea_grams - ginger_tea_grams

print(f"Total grams of remaining tea is {remaining_tea}")

milk_litres = 7
servings = 4
milk_per_servings = milk_litres / servings
print(f"Milk per servings is {milk_per_servings}")

total_tea_bag = 7
pots = 4
bags_per_pots = total_tea_bag // pots
print(f"Whole tea bags per pot is {bags_per_pots}")

total_cardamom_pots = 10
pots_per_cup = 3

left_over_pots = total_cardamom_pots % pots_per_cup

print(f"Leftover C pots are {left_over_pots}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavour = base_flavor_strength ** scale_factor
print(f"Scaled flavour strength {powerful_flavour}")

total_tea_leaves_harvested = 1_000_000_000
print(f"Tea leaves {total_tea_leaves_harvested}")