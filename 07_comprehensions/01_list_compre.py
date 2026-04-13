menu = [
    "Masala Chai",
    "Iced lemon tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]

# iced_tea = [tea for tea in menu if "Iced" in tea]
iced_tea = [my_tea for my_tea in menu if len(my_tea) > 8]

print(iced_tea)
