# Boolean

is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling # upcasting
print(f"Total actions {total_actions}")

milk_present = 1 # no-milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can serve Chai? {can_serve}")