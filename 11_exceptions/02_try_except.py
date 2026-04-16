chai_menu = {"masala": 30, "ginger": 40}

print(chai_menu["masala"])
try:
    print(chai_menu["elaichi"])
except KeyError:
    print("The key that you are trying to access does not exist")

print(chai_menu["ginger"])