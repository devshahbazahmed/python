my_cart = ["apples", "bananas", "milk"]
print(my_cart)

my_cart.append("bread")
print(my_cart)

my_cart.insert(0, "ketchup")
print(my_cart)

banana = my_cart.pop(2)
print(my_cart)

removed_item = my_cart.pop()
print(removed_item)

my_cart.extend(["rice", "butter"])
print(my_cart)

my_cart.sort()
print(my_cart)

my_cart.reverse()
print(my_cart)

another_list = ["juice", "jam"]
new_list = my_cart + another_list
print(new_list)

duplicated_list = my_cart * 2
print(duplicated_list)

veg_string = "tomato cucumber spinach"
veg_list = veg_string.split()
print(veg_list)

