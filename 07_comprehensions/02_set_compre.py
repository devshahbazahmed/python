favourite_chais = [
    "Masala chai", "Green tea", "Masala chai",
    "Lemon tea", "Green tea", "Ginger tea",
]

unique_chai = {tea for tea in favourite_chais}
# unique_chai = {tea for tea in favourite_chais if len(tea) > 9}

print(unique_chai)

recipes = {
    "Masala chai": ["ginger", "cardamom", "clove"],
    "Elaichi chai": ["cardamom", "milk"],
    "Spicy chai": ["ginger", "clove", "cardamom"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)